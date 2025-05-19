import os
import sys
import tkinter as tk
import threading
import speech_recognition as sr
from tkinter import ttk

# Define Warp-inspired color scheme
COLORS = {
    'background': '#1E1E1E',
    'text': '#D4D4D4',
    'accent': '#007ACC',
    'prompt': '#00FF00',
    'button_bg': '#2D2D2D',
    'button_fg': '#FFFFFF',
}

# Shell functions with string outputs
def removeDirectory(directories):
    messages = []
    for dir in directories:
        try:
            os.rmdir(dir)
            messages.append(f"Directory '{dir}' removed.")
        except FileNotFoundError:
            messages.append(f"Directory '{dir}' not found.")
        except OSError:
            messages.append(f"Cannot delete '{dir}'. Directory is not empty.")
    return "\n".join(messages) if messages else "No directories specified."

def removeFile(files):
    messages = []
    for file in files:
        try:
            os.remove(file)
            messages.append(f"File '{file}' removed.")
        except FileNotFoundError:
            messages.append(f"File '{file}' not found.")
        except PermissionError:
            messages.append("Permission denied.")
        except OSError:
            messages.append(f"Cannot delete '{file}'. Directory is not empty.")
    return "\n".join(messages) if messages else "No files specified."

def makeFile(file_name):
    try:
        with open(file_name, 'x') as f:
            pass
        return f"File '{file_name}' created."
    except FileExistsError:
        return f"File '{file_name}' already exists."
    except PermissionError:
        return f"Permission denied: Unable to create '{file_name}'."
    except Exception as e:
        return f"An error occurred: {e}"

def makeDirectory(directory_name):
    try:
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created."
    except FileExistsError:
        return f"Directory '{directory_name}' already exists."
    except PermissionError:
        return f"Permission denied: Unable to create '{directory_name}'."
    except Exception as e:
        return f"An error occurred: {e}"

def changeDirectory(path):
    try:
        os.chdir(path)
        return f"Changed to {os.getcwd()}"
    except FileNotFoundError:
        return "The system cannot find the path specified."

def getPresentWorkingDirectory():
    return os.getcwd()

def list_directory():
    return "  ".join(os.listdir(os.getcwd()))

# Redirect stdout to Text widget
class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert("end", string)
        self.text_widget.see("end")

    def flush(self):
        pass

# Voice command mappings
voice_commands = {
    "list processes": "ls",
    "present working directory": "pwd",
    "change directory to": "cd",
    "make directory": "mkdir",
    "touch file": "touch",
    "remove file": "rm",
    "remove directory": "rm -r"
}

commands_with_args = ["cd", "mkdir", "touch", "rm", "rm -r"]

# Special character replacements
replacements = [
    (" dot ", "."),
    (" period ", "."),
    (" underscore ", "_"),
    (" underline ", "_"),
    (" slash ", "/"),
    (" backslash ", "\\"),
    (" dash ", "-"),
    (" hyphen ", "-"),
]

def process_argument(text):
    for spoken, char in replacements:
        text = text.replace(spoken, char)
    return text.strip()

# Execute commands with block styling
def execute_command(command):
    text.insert("end", f"{command}\n", "command")
    text.see("end")

    if command == "pwd":
        output = getPresentWorkingDirectory()
    elif command == "ls":
        output = list_directory()
    elif command.startswith("cd "):
        output = changeDirectory(command[3:].strip())
    elif command.startswith("mkdir "):
        output = makeDirectory(command[6:].strip())
    elif command.startswith("touch "):
        output = makeFile(command[6:].strip())
    elif command.startswith("rm -r "):
        output = removeDirectory(command.split()[2:])
    elif command.startswith("rm "):
        output = removeFile(command.split()[1:])
    else:
        output = "Unknown command"

    text.insert("end", f"{output}\n\n", "output")

# Run command and insert prompt
def run_command(cmd):
    execute_command(cmd)
    insert_prompt()

# Voice recognition
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")
            for voice_cmd, shell_cmd in voice_commands.items():
                if shell_cmd in commands_with_args:
                    if text.startswith(voice_cmd):
                        arg = text[len(voice_cmd):].strip()
                        processed_arg = process_argument(arg)
                        full_command = f"{shell_cmd} {processed_arg}"
                        root.after(0, lambda cmd=full_command: run_command(cmd))
                        break
                else:
                    if voice_cmd in text:
                        root.after(0, lambda cmd=shell_cmd: run_command(cmd))
                        break
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# GUI Setup
root = tk.Tk()
root.title("My Shell")
root.configure(bg=COLORS['background'])

# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

customize_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Customize", menu=customize_menu)

def open_customize_window():
    customize_window = tk.Toplevel(root)
    customize_window.title("Customize Voice Commands")
    customize_window.configure(bg=COLORS['background'])
    entries = {}
    for shell_cmd in voice_commands.values():
        label = tk.Label(customize_window, text=f"Voice Command for {shell_cmd}:", bg=COLORS['background'], fg=COLORS['text'])
        label.pack()
        entry = tk.Entry(customize_window, bg=COLORS['button_bg'], fg=COLORS['button_fg'])
        current_voice_cmd = [k for k, v in voice_commands.items() if v == shell_cmd][0]
        entry.insert(0, current_voice_cmd)
        entry.pack()
        entries[shell_cmd] = entry

    def save_voice_commands():
        global voice_commands
        voice_commands = {entry.get(): shell_cmd for shell_cmd, entry in entries.items()}
        customize_window.destroy()

    save_button = tk.Button(customize_window, text="Save", command=save_voice_commands, bg=COLORS['button_bg'], fg=COLORS['button_fg'])
    save_button.pack()

customize_menu.add_command(label="Edit Voice Commands", command=open_customize_window)

# Main terminal frame
frame = tk.Frame(root, bg=COLORS['background'])
frame.pack(fill="both", expand=True)

text = tk.Text(frame, wrap="word", bg=COLORS['background'], fg=COLORS['text'],
               insertbackground=COLORS['text'], font=("Consolas", 10), borderwidth=0)
text.pack(side="left", fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame, command=text.yview)
scrollbar.pack(side="right", fill="y")
text.config(yscrollcommand=scrollbar.set)

sys.stdout = TextRedirector(text)

# Configure tags for styling
text.tag_configure("command", foreground=COLORS['accent'])
text.tag_configure("output", foreground=COLORS['text'])
text.tag_configure("prompt", foreground=COLORS['prompt'])

# Insert prompt
def insert_prompt():
    prompt = f"{os.getcwd()} $ "
    text.insert("end", prompt, "prompt")
    text.mark_set("input_start", "end-1c")
    text.mark_gravity("input_start", "left")

insert_prompt()

# Voice button
def start_voice_recognition():
    threading.Thread(target=recognize_voice, daemon=True).start()

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background=COLORS['button_bg'], foreground=COLORS['button_fg'], font=("Helvetica", 10))
voice_button = ttk.Button(root, text="Speak", command=start_voice_recognition, style='TButton')
voice_button.pack(pady=10)

# Handle key presses
def on_key_press(event):
    if event.keysym == "Return":
        command = text.get("input_start", "end-1c").strip()
        if command == "exit":
            root.quit()
        else:
            text.insert("end", "\n")
            execute_command(command)
            insert_prompt()
        return "break"
    elif event.keysym == "Backspace":
        if text.compare("insert", "<=", "input_start"):
            return "break"
    elif event.keysym == "Left":
        if text.compare("insert-1c", "<", "input_start"):
            return "break"
    elif event.keysym == "Home":
        text.mark_set("insert", "input_start")
        return "break"
    elif event.keysym in ("Up", "Down"):
        return "break"

text.bind("<Key>", on_key_press)
text.focus_set()

root.mainloop()