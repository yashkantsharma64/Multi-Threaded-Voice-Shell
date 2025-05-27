# import os

# def removeDirectory(directory_to_delete):
#     for dir in directory_to_delete:
#         try:
#             os.rmdir(dir)
#         except FileNotFoundError:
#             print(f"Directory '{dir}' not found.")
#         except OSError:
#             print(f"Cannot delete '{dir}'. Directory is not empty.")

# def removeFile(files_to_delete):
#     for file in files_to_delete:
#         try:
#             os.remove(file)
#         except FileNotFoundError:
#             print(f"Directory '{file}' not found.")
#         except PermissionError:
#             print("Permission denied.")
#         except OSError:
#             print(f"Cannot delete '{file}'. Directory is not empty.")

# def makeFile(file_name):
#     try:
#         os.mkdir(file_name)
#     except FileExistsError:
#         print(f"File '{file_name}' already exists.")
#     except PermissionError:
#         print(f"Permission denied: Unable to create '{file_name}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def makeDirectory(directory_name):
#     try:
#         os.mkdir(directory_name)
#     except FileExistsError:
#         print(f"Directory '{directory_name}' already exists.")
#     except PermissionError:
#         print(f"Permission denied: Unable to create '{directory_name}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def changeDirectory(path):
#     try:
#         os.chdir(path)
#     except FileNotFoundError:
#         print("The system cannot find the path specified.")

# def getPresentWorkingDirectory():
#     print(os.getcwd())

# def list():
#     directory_list = os.listdir(os.getcwd())
#     print("  ".join(directory_list))

# # os.chdir("C:/Users/yashk")
# command = ""
# while command != "exit":
#     command = input(f"{os.getcwd()} $ ")
#     if command == "pwd":
#         getPresentWorkingDirectory()
#     elif(command == 'ls'):
#         list()
#     elif(command[:3] == 'cd '):
#         changeDirectory(command.split(" ")[-1])
#     elif(command[:6] == 'mkdir '):
#         makeDirectory(command.split(" ")[-1])
#     elif(command[:6] == 'touch '):
#         makeFile(command.split(" ")[-1])
#     elif(command[:6] == 'rm -r '):
#         removeDirectory(command.split(" ")[2:])
#     elif(command[:3] == 'rm '):
#         removeFile(command.split(" ")[1:])






























































































































































































































































































































































































































































































































































































































# import os
# import sys
# import tkinter as tk
# import threading
# import speech_recognition as sr

# # Your original shell functions
# def removeDirectory(directory_to_delete):
#     for dir in directory_to_delete:
#         try:
#             os.rmdir(dir)
#         except FileNotFoundError:
#             print(f"Directory '{dir}' not found.")
#         except OSError:
#             print(f"Cannot delete '{dir}'. Directory is not empty.")

# def removeFile(files_to_delete):
#     for file in files_to_delete:
#         try:
#             os.remove(file)
#         except FileNotFoundError:
#             print(f"File '{file}' not found.")
#         except PermissionError:
#             print("Permission denied.")
#         except OSError:
#             print(f"Cannot delete '{file}'. Directory is not empty.")

# def makeFile(file_name):
#     try:
#         with open(file_name, 'x') as f:
#             pass
#     except FileExistsError:
#         print(f"File '{file_name}' already exists.")
#     except PermissionError:
#         print(f"Permission denied: Unable to create '{file_name}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def makeDirectory(directory_name):
#     try:
#         os.mkdir(directory_name)
#     except FileExistsError:
#         print(f"Directory '{directory_name}' already exists.")
#     except PermissionError:
#         print(f"Permission denied: Unable to create '{directory_name}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def changeDirectory(path):
#     try:
#         os.chdir(path)
#     except FileNotFoundError:
#         print("The system cannot find the path specified.")

# def getPresentWorkingDirectory():
#     print(os.getcwd())

# def list_processes():
#     directory_list = os.listdir(os.getcwd())
#     print("  ".join(directory_list))

# # Custom class to redirect stdout to the Text widget
# class TextRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert("end", string)
#         self.text_widget.see("end")

#     def flush(self):
#         pass

# # Default voice command mappings
# voice_commands = {
#     "list processes": "ls",
#     "make directory": "mkdir",
#     "touch file": "touch",
#     "change directory": "cd",
#     "present working directory": "pwd",
#     "remove file": "rm",
#     "remove directory": "rm -r"
# }

# # Function to execute shell commands
# def execute_command(command):
#     if command == "pwd":
#         getPresentWorkingDirectory()
#     elif command == "ls":
#         list_processes()
#     elif command.startswith("cd "):
#         changeDirectory(command[3:].strip())
#     elif command.startswith("mkdir "):
#         makeDirectory(command[6:].strip())
#     elif command.startswith("touch "):
#         makeFile(command[6:].strip())
#     elif command.startswith("rm -r "):
#         removeDirectory(command.split()[2:])
#     elif command.startswith("rm "):
#         removeFile(command.split()[1:])

# # Function to recognize voice and execute command
# def recognize_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio).lower()
#             print(f"Recognized: {text}")
#             for voice_cmd, shell_cmd in voice_commands.items():
#                 if voice_cmd in text:
#                     execute_command(shell_cmd)
#                     break
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

# # GUI Setup
# root = tk.Tk()
# root.title("My Shell")

# frame = tk.Frame(root)
# frame.pack(fill="both", expand=True)

# text = tk.Text(frame, wrap="word", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
# text.pack(side="left", fill="both", expand=True)

# scrollbar = tk.Scrollbar(frame, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)

# sys.stdout = TextRedirector(text)

# # Function to insert prompt
# def insert_prompt():
#     prompt = f"{os.getcwd()} $ "
#     text.insert("end", prompt)
#     text.mark_set("input_start", "end-1c")
#     text.mark_gravity("input_start", "left")

# insert_prompt()

# # Voice command editing frame
# edit_frame = tk.Frame(root)
# edit_frame.pack(fill="x")

# def update_voice_commands():
#     global voice_commands
#     voice_commands = {entry.get(): cmd for entry, cmd in zip(voice_entries, shell_commands)}

# voice_entries = []
# shell_commands = list(voice_commands.values())

# for voice_cmd, shell_cmd in voice_commands.items():
#     label = tk.Label(edit_frame, text=f"Voice Command for {shell_cmd}:")
#     label.pack(side="left")
#     entry = tk.Entry(edit_frame)
#     entry.insert(0, voice_cmd)
#     entry.pack(side="left")
#     voice_entries.append(entry)

# update_button = tk.Button(edit_frame, text="Update Voice Commands", command=update_voice_commands)
# update_button.pack(side="left")

# # Voice input button
# def start_voice_recognition():
#     threading.Thread(target=recognize_voice, daemon=True).start()

# voice_button = tk.Button(root, text="Speak", command=start_voice_recognition)
# voice_button.pack()

# # Handle key presses for text input
# def on_key_press(event):
#     if event.keysym == "Return":
#         command = text.get("input_start", "end-1c").strip()
#         if command == "exit":
#             root.quit()
#         else:
#             text.insert("end", "\n")
#             execute_command(command)
#             insert_prompt()
#         return "break"
#     elif event.keysym == "Backspace":
#         if text.compare("insert", "<=", "input_start"):
#             return "break"
#     elif event.keysym == "Left":
#         if text.compare("insert-1c", "<", "input_start"):
#             return "break"
#     elif event.keysym == "Home":
#         text.mark_set("insert", "input_start")
#         return "break"
#     elif event.keysym in ("Up", "Down"):
#         return "break"

# text.bind("<Key>", on_key_press)
# text.focus_set()

# root.mainloop()






















# import os
# import sys
# import tkinter as tk
# import threading
# import speech_recognition as sr

# # Shell functions returning output instead of printing
# def removeDirectory(directories):
#     messages = []
#     for dir in directories:
#         try:
#             os.rmdir(dir)
#         except FileNotFoundError:
#             messages.append(f"Directory '{dir}' not found.")
#         except OSError:
#             messages.append(f"Cannot delete '{dir}'. Directory is not empty.")
#     return "\n".join(messages) if messages else None

# def removeFile(files):
#     messages = []
#     for file in files:
#         try:
#             os.remove(file)
#         except FileNotFoundError:
#             messages.append(f"File '{file}' not found.")
#         except PermissionError:
#             messages.append("Permission denied.")
#         except OSError:
#             messages.append(f"Cannot delete '{file}'. Directory is not empty.")
#     return "\n".join(messages) if messages else None

# def makeFile(file_name):
#     try:
#         with open(file_name, 'x') as f:
#             pass
#         return None
#     except FileExistsError:
#         return f"File '{file_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{file_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def makeDirectory(directory_name):
#     try:
#         os.mkdir(directory_name)
#         return None
#     except FileExistsError:
#         return f"Directory '{directory_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{directory_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def changeDirectory(path):
#     try:
#         os.chdir(path)
#         return None
#     except FileNotFoundError:
#         return "The system cannot find the path specified."

# def getPresentWorkingDirectory():
#     return os.getcwd()

# def list_directory():
#     return "  ".join(os.listdir(os.getcwd()))

# # Custom class to redirect stdout to the Text widget
# class TextRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert("end", string)
#         self.text_widget.see("end")

#     def flush(self):
#         pass

# # Default voice command mappings
# voice_commands = {
#     "list processes": "ls",
#     "make directory": "mkdir",
#     "touch file": "touch",
#     "change directory": "cd",
#     "present working directory": "pwd",
#     "remove file": "rm",
#     "remove directory": "rm -r"
# }

# # Function to execute shell commands and insert output
# def execute_command(command):
#     if command == "pwd":
#         output = getPresentWorkingDirectory()
#         if output:
#             text.insert("end", output + "\n")
#     elif command == "ls":
#         output = list_directory()
#         if output:
#             text.insert("end", output + "\n")
#     elif command.startswith("cd "):
#         result = changeDirectory(command[3:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("mkdir "):
#         result = makeDirectory(command[6:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("touch "):
#         result = makeFile(command[6:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("rm -r "):
#         result = removeDirectory(command.split()[2:])
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("rm "):
#         result = removeFile(command.split()[1:])
#         if result:
#             text.insert("end", result + "\n")

# # Function to run command and insert prompt (for voice commands)
# def run_command(cmd):
#     execute_command(cmd)
#     insert_prompt()

# # Function to recognize voice and execute command
# def recognize_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio).lower()
#             print(f"Recognized: {text}")
#             for voice_cmd, shell_cmd in voice_commands.items():
#                 if voice_cmd in text:
#                     root.after(0, lambda: run_command(shell_cmd))
#                     break
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

# # GUI Setup
# root = tk.Tk()
# root.title("My Shell")

# # Menu bar with Customize option
# menubar = tk.Menu(root)
# root.config(menu=menubar)

# customize_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Customize", menu=customize_menu)

# def open_customize_window():
#     customize_window = tk.Toplevel(root)
#     customize_window.title("Customize Voice Commands")

#     entries = {}
#     for shell_cmd in voice_commands.values():
#         label = tk.Label(customize_window, text=f"Voice Command for {shell_cmd}:")
#         label.pack()
#         entry = tk.Entry(customize_window)
#         current_voice_cmd = [k for k, v in voice_commands.items() if v == shell_cmd][0]
#         entry.insert(0, current_voice_cmd)
#         entry.pack()
#         entries[shell_cmd] = entry

#     def save_voice_commands():
#         global voice_commands
#         voice_commands = {entry.get(): shell_cmd for shell_cmd, entry in entries.items()}
#         customize_window.destroy()

#     save_button = tk.Button(customize_window, text="Save", command=save_voice_commands)
#     save_button.pack()

# customize_menu.add_command(label="Edit Voice Commands", command=open_customize_window)

# # Main terminal frame
# frame = tk.Frame(root)
# frame.pack(fill="both", expand=True)

# text = tk.Text(frame, wrap="word", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
# text.pack(side="left", fill="both", expand=True)

# scrollbar = tk.Scrollbar(frame, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)

# sys.stdout = TextRedirector(text)

# # Function to insert prompt
# def insert_prompt():
#     prompt = f"{os.getcwd()} $ "
#     text.insert("end", prompt)
#     text.mark_set("input_start", "end-1c")
#     text.mark_gravity("input_start", "left")

# insert_prompt()

# # Voice input button
# def start_voice_recognition():
#     threading.Thread(target=recognize_voice, daemon=True).start()

# voice_button = tk.Button(root, text="Speak", command=start_voice_recognition)
# voice_button.pack()

# # Handle key presses for manual commands
# def on_key_press(event):
#     if event.keysym == "Return":
#         command = text.get("input_start", "end-1c").strip()
#         if command == "exit":
#             root.quit()
#         else:
#             text.insert("end", "\n")
#             execute_command(command)
#             insert_prompt()
#         return "break"
#     elif event.keysym == "Backspace":
#         if text.compare("insert", "<=", "input_start"):
#             return "break"
#     elif event.keysym == "Left":
#         if text.compare("insert-1c", "<", "input_start"):
#             return "break"
#     elif event.keysym == "Home":
#         text.mark_set("insert", "input_start")
#         return "break"
#     elif event.keysym in ("Up", "Down"):
#         return "break"

# text.bind("<Key>", on_key_press)
# text.focus_set()

# root.mainloop()




































# import os
# import sys
# import tkinter as tk
# import threading
# import speech_recognition as sr

# # Shell functions returning output instead of printing
# def removeDirectory(directories):
#     messages = []
#     for dir in directories:
#         try:
#             os.rmdir(dir)
#         except FileNotFoundError:
#             messages.append(f"Directory '{dir}' not found.")
#         except OSError:
#             messages.append(f"Cannot delete '{dir}'. Directory is not empty.")
#     return "\n".join(messages) if messages else None

# def removeFile(files):
#     messages = []
#     for file in files:
#         try:
#             os.remove(file)
#         except FileNotFoundError:
#             messages.append(f"File '{file}' not found.")
#         except PermissionError:
#             messages.append("Permission denied.")
#         except OSError:
#             messages.append(f"Cannot delete '{file}'. Directory is not empty.")
#     return "\n".join(messages) if messages else None

# def makeFile(file_name):
#     try:
#         with open(file_name, 'x') as f:
#             pass
#         return None
#     except FileExistsError:
#         return f"File '{file_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{file_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def makeDirectory(directory_name):
#     try:
#         os.mkdir(directory_name)
#         return None
#     except FileExistsError:
#         return f"Directory '{directory_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{directory_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def changeDirectory(path):
#     try:
#         os.chdir(path)
#         return None
#     except FileNotFoundError:
#         return "The system cannot find the path specified."

# def getPresentWorkingDirectory():
#     return os.getcwd()

# def list_directory():
#     return "  ".join(os.listdir(os.getcwd()))

# # Custom class to redirect stdout to the Text widget
# class TextRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert("end", string)
#         self.text_widget.see("end")

#     def flush(self):
#         pass

# # Default voice command mappings
# voice_commands = {
#     "list processes": "ls",
#     "present working directory": "pwd",
#     "change directory to": "cd",
#     "make directory": "mkdir",
#     "touch file": "touch",
#     "remove file": "rm",
#     "remove directory": "rm -r"
# }

# commands_with_args = ["cd", "mkdir", "touch", "rm", "rm -r"]

# # Special character replacements
# replacements = [
#     (" dot ", "."),
#     (" period ", "."),
#     (" underscore ", "_"),
#     (" underline ", "_"),
#     (" slash ", "/"),
#     (" backslash ", "\\"),
#     (" dash ", "-"),
#     (" hyphen ", "-"),
# ]

# def process_argument(text):
#     for spoken, char in replacements:
#         text = text.replace(spoken, char)
#     return text.strip()

# # Function to execute shell commands and insert output
# def execute_command(command):
#     if command == "pwd":
#         output = getPresentWorkingDirectory()
#         if output:
#             text.insert("end", output + "\n")
#     elif command == "ls":
#         output = list_directory()
#         if output:
#             text.insert("end", output + "\n")
#     elif command.startswith("cd "):
#         result = changeDirectory(command[3:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("mkdir "):
#         result = makeDirectory(command[6:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("touch "):
#         result = makeFile(command[6:].strip())
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("rm -r "):
#         result = removeDirectory(command.split()[2:])
#         if result:
#             text.insert("end", result + "\n")
#     elif command.startswith("rm "):
#         result = removeFile(command.split()[1:])
#         if result:
#             text.insert("end", result + "\n")

# # Function to run command and insert prompt (for voice commands)
# def run_command(cmd):
#     execute_command(cmd)
#     insert_prompt()

# # Function to recognize voice and execute command
# def recognize_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio).lower()
#             print(f"Recognized: {text}")
#             for voice_cmd, shell_cmd in voice_commands.items():
#                 if shell_cmd in commands_with_args:
#                     if text.startswith(voice_cmd):
#                         arg = text[len(voice_cmd):].strip()
#                         processed_arg = process_argument(arg)
#                         full_command = f"{shell_cmd} {processed_arg}"
#                         root.after(0, lambda cmd=full_command: run_command(cmd))
#                         break
#                 else:
#                     if voice_cmd in text:
#                         root.after(0, lambda cmd=shell_cmd: run_command(cmd))
#                         break
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

# # GUI Setup
# root = tk.Tk()
# root.title("My Shell")

# # Menu bar with Customize option
# menubar = tk.Menu(root)
# root.config(menu=menubar)

# customize_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Customize", menu=customize_menu)

# def open_customize_window():
#     customize_window = tk.Toplevel(root)
#     customize_window.title("Customize Voice Commands")

#     entries = {}
#     for shell_cmd in voice_commands.values():
#         label = tk.Label(customize_window, text=f"Voice Command for {shell_cmd}:")
#         label.pack()
#         entry = tk.Entry(customize_window)
#         current_voice_cmd = [k for k, v in voice_commands.items() if v == shell_cmd][0]
#         entry.insert(0, current_voice_cmd)
#         entry.pack()
#         entries[shell_cmd] = entry

#     def save_voice_commands():
#         global voice_commands
#         voice_commands = {entry.get(): shell_cmd for shell_cmd, entry in entries.items()}
#         customize_window.destroy()

#     save_button = tk.Button(customize_window, text="Save", command=save_voice_commands)
#     save_button.pack()

# customize_menu.add_command(label="Edit Voice Commands", command=open_customize_window)

# # Main terminal frame
# frame = tk.Frame(root)
# frame.pack(fill="both", expand=True)

# text = tk.Text(frame, wrap="word", bg="black", fg="white", insertbackground="white", font=("Courier", 10))
# text.pack(side="left", fill="both", expand=True)

# scrollbar = tk.Scrollbar(frame, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)

# sys.stdout = TextRedirector(text)

# # Function to insert prompt
# def insert_prompt():
#     prompt = f"{os.getcwd()} $ "
#     text.insert("end", prompt)
#     text.mark_set("input_start", "end-1c")
#     text.mark_gravity("input_start", "left")

# insert_prompt()

# # Voice input button
# def start_voice_recognition():
#     threading.Thread(target=recognize_voice, daemon=True).start()

# voice_button = tk.Button(root, text="Speak", command=start_voice_recognition)
# voice_button.pack()

# # Handle key presses for manual commands
# def on_key_press(event):
#     if event.keysym == "Return":
#         command = text.get("input_start", "end-1c").strip()
#         if command == "exit":
#             root.quit()
#         else:
#             text.insert("end", "\n")
#             execute_command(command)
#             insert_prompt()
#         return "break"
#     elif event.keysym == "Backspace":
#         if text.compare("insert", "<=", "input_start"):
#             return "break"
#     elif event.keysym == "Left":
#         if text.compare("insert-1c", "<", "input_start"):
#             return "break"
#     elif event.keysym == "Home":
#         text.mark_set("insert", "input_start")
#         return "break"
#     elif event.keysym in ("Up", "Down"):
#         return "break"

# text.bind("<Key>", on_key_press)
# text.focus_set()

# root.mainloop()


















# Asli maaal

# import os
# import sys
# import tkinter as tk
# import threading
# import speech_recognition as sr
# from tkinter import ttk

# COLORS = {
#     'background': '#1E1E1E',
#     'text': '#D4D4D4',
#     'accent': '#007ACC',
#     'prompt': '#00FF00',
#     'button_bg': '#2D2D2D',
#     'button_fg': '#FFFFFF',
# }

# # Shell functions with string outputs
# def removeDirectory(directories):
#     messages = []
#     for dir in directories:
#         try:
#             os.rmdir(dir)
#             messages.append(f"Directory '{dir}' removed.")
#         except FileNotFoundError:
#             messages.append(f"Directory '{dir}' not found.")
#         except OSError:
#             messages.append(f"Cannot delete '{dir}'. Directory is not empty.")
#     return "\n".join(messages) if messages else "No directories specified."

# def removeFile(files):
#     messages = []
#     for file in files:
#         try:
#             os.remove(file)
#             messages.append(f"File '{file}' removed.")
#         except FileNotFoundError:
#             messages.append(f"File '{file}' not found.")
#         except PermissionError:
#             messages.append("Permission denied.")
#         except OSError:
#             messages.append(f"Cannot delete '{file}'. Directory is not empty.")
#     return "\n".join(messages) if messages else "No files specified."

# def makeFile(file_name):
#     try:
#         with open(file_name, 'x') as f:
#             pass
#         return f"File '{file_name}' created."
#     except FileExistsError:
#         return f"File '{file_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{file_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def makeDirectory(directory_name):
#     try:
#         os.mkdir(directory_name)
#         return f"Directory '{directory_name}' created."
#     except FileExistsError:
#         return f"Directory '{directory_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{directory_name}'."
#     except Exception as e:
#         return f"An error occurred: {e}"

# def changeDirectory(path):
#     try:
#         os.chdir(path)
#         return f"Changed to {os.getcwd()}"
#     except FileNotFoundError:
#         return "The system cannot find the path specified."

# def getPresentWorkingDirectory():
#     return os.getcwd()

# def list_directory():
#     return "  ".join(os.listdir(os.getcwd()))

# class TextRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert("end", string)
#         self.text_widget.see("end")

#     def flush(self):
#         pass

# # Voice command mappings
# voice_commands = {
#     "list processes": "ls",
#     "present working directory": "pwd",
#     "change directory to": "cd",
#     "make directory": "mkdir",
#     "touch file": "touch",
#     "remove file": "rm",
#     "remove directory": "rm -r"
# }

# commands_with_args = ["cd", "mkdir", "touch", "rm", "rm -r"]

# # Special character replacements
# replacements = [
#     (" dot ", "."),
#     (" period ", "."),
#     (" underscore ", "_"),
#     (" underline ", "_"),
#     (" slash ", "/"),
#     (" backslash ", "\\"),
#     (" dash ", "-"),
#     (" hyphen ", "-"),
# ]

# def process_argument(text):
#     for spoken, char in replacements:
#         text = text.replace(spoken, char)
#     return text.strip()

# # Execute commands with block styling
# def execute_command(command):
#     text.insert("end", f"{command}\n", "command")
#     text.see("end")

#     if command == "pwd":
#         output = getPresentWorkingDirectory()
#     elif command == "ls":
#         output = list_directory()
#     elif command.startswith("cd "):
#         output = changeDirectory(command[3:].strip())
#     elif command.startswith("mkdir "):
#         output = makeDirectory(command[6:].strip())
#     elif command.startswith("touch "):
#         output = makeFile(command[6:].strip())
#     elif command.startswith("rm -r "):
#         output = removeDirectory(command.split()[2:])
#     elif command.startswith("rm "):
#         output = removeFile(command.split()[1:])
#     else:
#         output = "Unknown command"

#     text.insert("end", f"{output}\n\n", "output")

# # Run command and insert prompt
# def run_command(cmd):
#     execute_command(cmd)
#     insert_prompt()

# # Voice recognition
# def recognize_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio).lower()
#             print(f"Recognized: {text}")
#             for voice_cmd, shell_cmd in voice_commands.items():
#                 if shell_cmd in commands_with_args:
#                     if text.startswith(voice_cmd):
#                         arg = text[len(voice_cmd):].strip()
#                         processed_arg = process_argument(arg)
#                         full_command = f"{shell_cmd} {processed_arg}"
#                         root.after(0, lambda cmd=full_command: run_command(cmd))
#                         break
#                 else:
#                     if voice_cmd in text:
#                         root.after(0, lambda cmd=shell_cmd: run_command(cmd))
#                         break
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

# # GUI Setup
# root = tk.Tk()
# root.title("My Shell")
# root.configure(bg=COLORS['background'])

# # Menu bar
# menubar = tk.Menu(root)
# root.config(menu=menubar)

# customize_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Customize", menu=customize_menu)

# def open_customize_window():
#     customize_window = tk.Toplevel(root)
#     customize_window.title("Customize Voice Commands")
#     customize_window.configure(bg=COLORS['background'])
#     entries = {}
#     for shell_cmd in voice_commands.values():
#         label = tk.Label(customize_window, text=f"Voice Command for {shell_cmd}:", bg=COLORS['background'], fg=COLORS['text'])
#         label.pack()
#         entry = tk.Entry(customize_window, bg=COLORS['button_bg'], fg=COLORS['button_fg'])
#         current_voice_cmd = [k for k, v in voice_commands.items() if v == shell_cmd][0]
#         entry.insert(0, current_voice_cmd)
#         entry.pack()
#         entries[shell_cmd] = entry

#     def save_voice_commands():
#         global voice_commands
#         voice_commands = {entry.get(): shell_cmd for shell_cmd, entry in entries.items()}
#         customize_window.destroy()

#     save_button = tk.Button(customize_window, text="Save", command=save_voice_commands, bg=COLORS['button_bg'], fg=COLORS['button_fg'])
#     save_button.pack()

# customize_menu.add_command(label="Edit Voice Commands", command=open_customize_window)

# # Main terminal frame
# frame = tk.Frame(root, bg=COLORS['background'])
# frame.pack(fill="both", expand=True)

# text = tk.Text(frame, wrap="word", bg=COLORS['background'], fg=COLORS['text'],
#                insertbackground=COLORS['text'], font=("Consolas", 10), borderwidth=0)
# text.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# scrollbar = tk.Scrollbar(frame, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)

# sys.stdout = TextRedirector(text)

# # Configure tags for styling
# text.tag_configure("command", foreground=COLORS['accent'])
# text.tag_configure("output", foreground=COLORS['text'])
# text.tag_configure("prompt", foreground=COLORS['prompt'])

# # Insert prompt
# def insert_prompt():
#     prompt = f"{os.getcwd()} $ "
#     text.insert("end", prompt, "prompt")
#     text.mark_set("input_start", "end-1c")
#     text.mark_gravity("input_start", "left")

# insert_prompt()

# # Voice button
# def start_voice_recognition():
#     threading.Thread(target=recognize_voice, daemon=True).start()

# style = ttk.Style()
# style.theme_use('clam')
# style.configure('TButton', background=COLORS['button_bg'], foreground=COLORS['button_fg'], font=("Helvetica", 10))
# voice_button = ttk.Button(root, text="Speak", command=start_voice_recognition, style='TButton')
# voice_button.pack(pady=10)

# # Handle key presses
# def on_key_press(event):
#     if event.keysym == "Return":
#         command = text.get("input_start", "end-1c").strip()
#         if command == "exit":
#             root.quit()
#         else:
#             text.insert("end", "\n")
#             execute_command(command)
#             insert_prompt()
#         return "break"
#     elif event.keysym == "Backspace":
#         if text.compare("insert", "<=", "input_start"):
#             return "break"
#     elif event.keysym == "Left":
#         if text.compare("insert-1c", "<", "input_start"):
#             return "break"
#     elif event.keysym == "Home":
#         text.mark_set("insert", "input_start")
#         return "break"
#     elif event.keysym in ("Up", "Down"):
#         return "break"

# text.bind("<Key>", on_key_press)
# text.focus_set()

# root.mainloop()





















# VoiceOS.py
# import os
# import sys
# import tkinter as tk
# import threading
# import shutil
# import speech_recognition as sr
# from tkinter import ttk
# import google.generativeai as genai
# import json
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# COLORS = {
#     'background': '#002b36',
#     'text': 'cyan',
#     'accent': '#007ACC',
#     'prompt': '#2aa17f',
#     'button_bg': '#001f27',
#     'button_fg': 'cyan',
# }

# # --- Gemini AI Setup ---
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# gemini_ready = False
# gemini_model = None

# if not GEMINI_API_KEY:
#     print("Error: GEMINI_API_KEY not found in .env file. Voice AI features will be limited.")
# else:
#     try:
#         genai.configure(api_key=GEMINI_API_KEY)
#         # Use a more specific model name, 'gemini-1.0-pro' is widely available.
#         # 'gemini-1.5-flash-latest' is another good option for speed and cost.
#         gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')
#         gemini_ready = True
#         print(f"Gemini AI initialized successfully with model: {gemini_model.model_name if gemini_model else 'N/A'}.")
#     except Exception as e:
#         print(f"Error initializing Gemini AI: {e}. Voice AI features will be limited.")

# # --- Shell functions with string outputs ---
# def removeDirectory(directories): # Expects a list of directory names
#     messages = []
#     if not directories:
#         return "No directories specified for removal."
#     for dir_name in directories:
#         if not dir_name.strip():
#             messages.append("Error: Empty directory name specified.")
#             continue
#         try:
#             # To allow removing directories with content, use shutil.rmtree
#             # For now, os.rmdir only removes empty directories
#             # If you want 'rm -r' to behave like shell's, use shutil.rmtree
#             # import shutil
#             shutil.rmtree(dir_name)
#             # os.rmdir(dir_name)
#             messages.append(f"Directory '{dir_name}' removed.")
#         except FileNotFoundError:
#             messages.append(f"Directory '{dir_name}' not found.")
#         except OSError as e:
#             messages.append(f"Cannot delete '{dir_name}'. It might not be empty or permission denied: {e}")
#         except Exception as e:
#             messages.append(f"An unexpected error occurred with '{dir_name}': {e}")
#     return "\n".join(messages)

# def removeFile(files): # Expects a list of file names
#     messages = []
#     if not files:
#         return "No files specified for removal."
#     for file_name in files:
#         if not file_name.strip():
#             messages.append("Error: Empty file name specified.")
#             continue
#         try:
#             os.remove(file_name)
#             messages.append(f"File '{file_name}' removed.")
#         except FileNotFoundError:
#             messages.append(f"File '{file_name}' not found.")
#         except PermissionError:
#             messages.append(f"Permission denied for '{file_name}'.")
#         except IsADirectoryError: # Specifically catch if it's a directory
#              messages.append(f"Cannot remove '{file_name}'. It is a directory. Use 'rm -r' for directories.")
#         except OSError as e: # Broader OS error
#             messages.append(f"OS error removing '{file_name}': {e}")
#         except Exception as e:
#             messages.append(f"An unexpected error occurred with '{file_name}': {e}")
#     return "\n".join(messages)


# def makeFile(file_name):
#     if not file_name.strip():
#         return "Error: No file name specified."
#     try:
#         with open(file_name, 'a') as f:
#             pass
#         return f"File '{file_name}' ensured/created."
#     except PermissionError:
#         return f"Permission denied: Unable to create/access '{file_name}'."
#     except Exception as e:
#         return f"An error occurred creating file '{file_name}': {e}"

# def makeDirectory(directory_name):
#     if not directory_name.strip():
#         return "Error: No directory name specified."
#     try:
#         os.mkdir(directory_name)
#         return f"Directory '{directory_name}' created."
#     except FileExistsError:
#         return f"Directory '{directory_name}' already exists."
#     except PermissionError:
#         return f"Permission denied: Unable to create '{directory_name}'."
#     except FileNotFoundError: # If a parent path does not exist
#         return f"Error creating directory '{directory_name}': Path not found. Create parent directories first."
#     except Exception as e:
#         return f"An error occurred creating directory '{directory_name}': {e}"

# def changeDirectory(path):
#     if not path.strip() and path != "..":
#         if not path.strip():
#           return "Error: No directory path specified for cd."
#     try:
#         os.chdir(path)
#         return f"Changed to {os.getcwd()}"
#     except FileNotFoundError:
#         return f"The system cannot find the path specified: '{path}'"
#     except NotADirectoryError:
#         return f"Not a directory: '{path}'"
#     except PermissionError:
#         return f"Permission denied for path: '{path}'"
#     except Exception as e:
#         return f"Error changing directory to '{path}': {e}"


# def getPresentWorkingDirectory():
#     return os.getcwd()

# def list_directory():
#     try:
#         return "  ".join(os.listdir(os.getcwd()))
#     except FileNotFoundError:
#         return "Error: Current working directory not found."
#     except PermissionError:
#         return "Error: Permission denied to list current directory."
#     except Exception as e:
#         return f"Error listing directory: {e}"

# # --- Text Widget Redirection ---
# class TextRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, string):
#         self.text_widget.insert("end", string)
#         self.text_widget.see("end")

#     def flush(self):
#         pass

# # --- AI Command Interpretation ---
# def get_command_from_ai(transcribed_text):
#     if not gemini_ready or not gemini_model:
#         return {"command": "unknown", "argument": "", "error": "Gemini AI not available."}

#     response = None # Initialize response to None

#     prompt = f"""
#     You are an AI assistant for a voice-controlled shell.
#     User's speech: "{transcribed_text}"

#     Your task is to identify which of the following 7 shell commands the user intends to execute and extract any necessary arguments.
#     The supported commands are:
#     1. ls (list directory contents)
#     2. pwd (print working directory)
#     3. cd <directory_name> (change directory to <directory_name>)
#     4. mkdir <directory_name> (make directory named <directory_name>)
#     5. touch <file_name> (create/update file named <file_name>)
#     6. rm <file_name> (remove file named <file_name>)
#     7. rm -r <directory_name> (remove directory named <directory_name>, recursively)

#     Argument Processing Rules:
#     - Convert spoken numbers to digits (e.g., "one" to "1").
#     - Interpret spoken characters:
#         "dot" or "period" -> "."
#         "underscore" or "underline" -> "_"
#         "slash" -> "/"
#         "backslash" -> "\\"
#         "dash" or "hyphen" -> "-"
#     - File/directory names can contain spaces. Preserve them.

#     Respond ONLY with a JSON object in the following format:
#     {{"command": "COMMAND_NAME", "argument": "ARGUMENT_VALUE"}}

#     - If the command does not take an argument (ls, pwd), "argument" should be an empty string.
#     - For commands like cd, mkdir, touch, rm, rm -r, "argument" should be the identified file/directory name.
#       If the user intends to operate on a single entity whose name contains spaces (e.g., "my documents"),
#       the argument should be "my documents".
#     - If the user's speech is unclear, ambiguous, or does not map to any of the 7 commands, respond with:
#       {{"command": "unknown", "argument": ""}}

#     Examples:
#     User speech: "list the files" -> {{"command": "ls", "argument": ""}}
#     User speech: "where am I?" -> {{"command": "pwd", "argument": ""}}
#     User speech: "go to my project folder" -> {{"command": "cd", "argument": "my project folder"}}
#     User speech: "make a directory called test results version one" -> {{"command": "mkdir", "argument": "test results version one"}}
#     User speech: "create a file report dot txt" -> {{"command": "touch", "argument": "report.txt"}}
#     User speech: "delete the file log_backup_file.data" -> {{"command": "rm", "argument": "log_backup_file.data"}}
#     User speech: "remove the old_stuff directory" -> {{"command": "rm -r", "argument": "old_stuff"}}
#     User speech: "hey computer, can you tell me the current path?" -> {{"command": "pwd", "argument": ""}}
#     User speech: "I want to make a folder named important documents" -> {{"command": "mkdir", "argument": "important documents"}}
#     User speech: "could you please erase temp underscore folder" -> {{"command": "rm -r", "argument": "temp_folder"}}
#     User speech: "what is two plus two" -> {{"command": "unknown", "argument": ""}}

#     User speech: "{transcribed_text}"
#     JSON Response:
#     """
#     try:
#         response = gemini_model.generate_content(prompt) # Assignment happens here
        
#         if not response or not hasattr(response, 'text'):
#             error_message = "Gemini API call did not return a valid response object or text."
#             if response and hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
#                 error_message += f" (Prompt blocked: {response.prompt_feedback.block_reason})"
#             print(error_message)
#             return {"command": "unknown", "argument": "", "error": error_message}

#         cleaned_response_text = response.text.strip()
#         if cleaned_response_text.startswith("```json"):
#             cleaned_response_text = cleaned_response_text[len("```json"):]
#         elif cleaned_response_text.startswith("```"):
#             cleaned_response_text = cleaned_response_text[len("```"):]
#         if cleaned_response_text.endswith("```"):
#             cleaned_response_text = cleaned_response_text[:-len("```")]
#         cleaned_response_text = cleaned_response_text.strip()

#         ai_json = json.loads(cleaned_response_text)
        
#         if isinstance(ai_json, dict) and "command" in ai_json and "argument" in ai_json:
#             ai_json["argument"] = ai_json.get("argument") or ""
#             return ai_json
#         else:
#             print(f"Error: AI response malformed structure. Raw: {response.text}")
#             return {"command": "unknown", "argument": "", "error": "Malformed AI response structure."}

#     except json.JSONDecodeError as e:
#         raw_resp_text = "'No text in response'"
#         if response and hasattr(response, 'text'):
#             raw_resp_text = response.text
#         print(f"Error decoding JSON from AI: {e}. Raw response text: {raw_resp_text}")
#         return {"command": "unknown", "argument": "", "error": f"JSON decode error: {e}"}
#     except Exception as e:
#         error_message = f"Error calling Gemini API or processing response: {e}"
#         if response and hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
#              error_message += f" (Prompt blocked: {response.prompt_feedback.block_reason})"
#         print(error_message)
#         return {"command": "unknown", "argument": "", "error": error_message}


# # --- Command Execution ---
# def execute_command(command_str):
#     text.insert("end", f"{command_str}\n", "command")
#     text.see("end")

#     parts = command_str.split(maxsplit=2)
#     base_cmd_part1 = parts[0] if len(parts) > 0 else ""
#     base_cmd_part2 = parts[1] if len(parts) > 1 else ""
    
#     full_base_command = base_cmd_part1
#     arg_string = ""

#     if base_cmd_part1 == "rm" and base_cmd_part2 == "-r":
#         full_base_command = "rm -r"
#         arg_string = parts[2] if len(parts) > 2 else ""
#     elif base_cmd_part1 in ["cd", "mkdir", "touch", "rm"]:
#         arg_string = command_str[len(base_cmd_part1):].strip()
    
#     output = ""
#     if full_base_command == "pwd":
#         output = getPresentWorkingDirectory()
#     elif full_base_command == "ls":
#         output = list_directory()
#     elif full_base_command == "cd":
#         output = changeDirectory(arg_string)
#     elif full_base_command == "mkdir":
#         output = makeDirectory(arg_string)
#     elif full_base_command == "touch":
#         output = makeFile(arg_string)
#     elif full_base_command == "rm": 
#         if not arg_string: output = "No file specified for rm."
#         else: output = removeFile([arg_string])
#     elif full_base_command == "rm -r":
#         if not arg_string: output = "No directory specified for rm -r."
#         else: output = removeDirectory([arg_string])
#     else:
#         output = f"Unknown command: '{command_str}'"

#     text.insert("end", f"{output}\n\n", "output")

# def run_command(cmd):
#     execute_command(cmd)
#     insert_prompt()

# # --- Voice Recognition ---
# def recognize_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         gui_status_update("Listening...")
#         print("Listening...")
#         try:
#             # recognizer.adjust_for_ambient_noise(source) # Consider adding this if noisy
#             audio = recognizer.listen(source, timeout=7, phrase_time_limit=12)
#         except sr.WaitTimeoutError:
#             print("No speech detected within timeout.")
#             gui_status_update("No speech detected. Try again.")
#             # No need to call insert_prompt here, as the button re-enables.
#             return
#         except Exception as e: # Catch other microphone/listen errors
#             print(f"Error during listening: {e}")
#             gui_status_update(f"Mic error: {e}")
#             return


#     gui_status_update("Recognizing speech...")
#     print("Recognizing speech...")
#     try:
#         text_from_speech = recognizer.recognize_google(audio).lower()
#         print(f"Recognized: {text_from_speech}")
#         gui_status_update(f"Heard: {text_from_speech}. Processing with AI...")

#         if not gemini_ready:
#             message = "Gemini AI is not initialized. Cannot process voice command via AI."
#             print(message)
#             gui_status_update(message)
#             root.after(0, lambda: text.insert("end", message + "\n", "error"))
#             root.after(0, insert_prompt)
#             return

#         ai_result = get_command_from_ai(text_from_speech)
        
#         command_name = ai_result.get("command")
#         argument = ai_result.get("argument", "") 
#         error_msg = ai_result.get("error")

#         if error_msg:
#             gui_status_update(f"AI Error: {error_msg}")
#             # Also print it to the terminal GUI
#             root.after(0, lambda: text.insert("end", f"AI Error: {error_msg}\n", "error"))


#         KNOWN_COMMANDS = ["ls", "pwd", "cd", "mkdir", "touch", "rm", "rm -r"]

#         if command_name in KNOWN_COMMANDS:
#             full_command = command_name
#             if argument or command_name in ["cd", "mkdir", "touch", "rm", "rm -r"]: # Include commands that *can* take an arg even if it's empty
#                 full_command = f"{command_name} {argument}".strip()
            
#             gui_status_update(f"AI Mapped to: {full_command}")
#             root.after(0, lambda cmd=full_command: run_command(cmd))
#         else:
#             message = f"AI could not map speech to a known command. (AI result: '{command_name}')"
#             if command_name == "unknown" and not argument and not error_msg : 
#                  message = "Sorry, I didn't understand that command. Please try again."
            
#             print(message)
#             gui_status_update(message)
#             root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
#             root.after(0, insert_prompt)

#     except sr.UnknownValueError:
#         message = "Google Speech Recognition could not understand audio."
#         print(message)
#         gui_status_update(message)
#         root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
#         root.after(0, insert_prompt)
#     except sr.RequestError as e:
#         message = f"Speech recognition service error; {e}"
#         print(message)
#         gui_status_update(message)
#         root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
#         root.after(0, insert_prompt)
#     except Exception as e: 
#         message = f"An unexpected error occurred during voice processing: {e}"
#         print(message)
#         gui_status_update(message)
#         root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
#         root.after(0, insert_prompt)

# # --- GUI Setup ---
# root = tk.Tk()
# root.title("VoiceOS Shell")
# root.configure(bg=COLORS['background'])
# root.geometry("800x600")

# frame = tk.Frame(root, bg=COLORS['background'])
# frame.pack(fill="both", expand=True, padx=5, pady=(5,0))

# text = tk.Text(frame, wrap="word", bg=COLORS['background'], fg=COLORS['text'],
#                insertbackground=COLORS['text'], font=("Consolas", 11), borderwidth=0,
#                undo=True)
# text.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# scrollbar = tk.Scrollbar(frame, command=text.yview, bg=COLORS['button_bg'], troughcolor=COLORS['background'])
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)

# status_bar_text = tk.StringVar()
# status_bar = tk.Label(root, textvariable=status_bar_text, bd=1, relief=tk.SUNKEN, anchor=tk.W,
#                       bg=COLORS['button_bg'], fg=COLORS['button_fg'], font=("Consolas", 9))
# status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=(0,5))
# status_bar_text.set("Ready.")

# def gui_status_update(message):
#     status_bar_text.set(message)

# sys.stdout = TextRedirector(text)

# text.tag_configure("command", foreground=COLORS['accent'], font=("Consolas", 11, "bold"))
# text.tag_configure("output", foreground=COLORS['text'])
# text.tag_configure("prompt", foreground=COLORS['prompt'], font=("Consolas", 11, "bold"))
# text.tag_configure("error", foreground='red')

# def insert_prompt():
#     try:
#         prompt_text = f"{os.getcwd()} $ "
#     except FileNotFoundError:
#         os.chdir(os.path.expanduser("~"))
#         prompt_text = f"{os.getcwd()} $ "
#         text.insert("end", "Current directory was lost. Reverted to home.\n", "error")

#     text.insert("end", prompt_text, "prompt")
#     text.mark_set("input_start", "end-1c")
#     text.mark_gravity("input_start", "left")
#     text.see("end")

# insert_prompt()

# def start_voice_recognition_thread():
#     if not gemini_ready:
#         gui_status_update("Gemini AI not ready. Check API Key and console.")
#         text.insert("end", "Voice AI is not configured. Check console for errors (e.g. GEMINI_API_KEY).\n", "error")
#         insert_prompt()
#         return
#     voice_button.config(state=tk.DISABLED)
#     gui_status_update("Initializing mic...") # Give some feedback before listening starts
#     # Use a short delay before starting recognize_voice to allow GUI to update status
#     root.after(100, lambda: threading.Thread(target=lambda: (recognize_voice(), voice_button.config(state=tk.NORMAL)), daemon=True).start())


# style = ttk.Style()
# style.theme_use('clam')
# style.configure('TButton', 
#                 background=COLORS['button_bg'], 
#                 foreground=COLORS['button_fg'], 
#                 font=("Helvetica", 10, "bold"),
#                 bordercolor=COLORS['accent'],
#                 lightcolor=COLORS['button_bg'], 
#                 darkcolor=COLORS['button_bg'], 
#                 padding=6)
# style.map('TButton',
#           background=[('active', COLORS['accent']), ('pressed', COLORS['accent'])],
#           foreground=[('active', COLORS['button_fg']), ('pressed', COLORS['button_fg'])])

# voice_button = ttk.Button(root, text="🎤 Speak Command", command=start_voice_recognition_thread, style='TButton')
# voice_button.pack(pady=10, fill=tk.X, padx=20)

# def on_key_press(event):
#     current_cursor_pos = text.index(tk.INSERT)
#     input_start_pos = text.index("input_start")

#     if text.compare(current_cursor_pos, "<", input_start_pos):
#         if event.keysym not in ["Left", "Right", "Home", "End", "Up", "Down", "Next", "Prior", "Copy", "c", "C"]:
#             if not (event.state & 0x0004 and event.keysym.lower() == 'c'): # Allow Ctrl+C
#                 text.mark_set(tk.INSERT, input_start_pos) # Force cursor to input_start

#     if event.keysym == "Return":
#         command = text.get("input_start", "end-1c").strip()
#         if command == "exit":
#             root.quit()
#         elif command:
#             text.insert("end", "\n")
#             execute_command(command)
#             insert_prompt()
#         else:
#             text.insert("end", "\n")
#             insert_prompt()
#         return "break"
    
#     elif event.keysym == "Backspace":
#         if text.compare(tk.INSERT, "<=", "input_start"):
#             return "break"
    
#     elif event.keysym == "Left":
#         if text.compare(f"{tk.INSERT}-1c", "<", "input_start"): 
#             return "break"
    
#     elif event.keysym == "Home":
#         text.mark_set(tk.INSERT, "input_start")
#         return "break"
    
#     elif event.keysym in ("Up", "Down"):
#         # Allow if selection active and in protected area, else block
#         if not text.tag_ranges(tk.SEL):
#             return "break"


# text.bind("<Key>", on_key_press)
# text.focus_set()

# if not gemini_ready:
#     initial_msg = "Gemini AI is not configured or failed to initialize. Voice commands requiring AI will not work. Please check console output for errors (e.g., missing GEMINI_API_KEY in .env file).\n"
#     text.insert("1.0", initial_msg, "error")
#     status_bar_text.set("AI not ready. Check API key.")

# root.mainloop()


























# VoiceOS.py
import os
import sys
import tkinter as tk
import threading
import speech_recognition as sr
from tkinter import ttk
import google.generativeai as genai
import json
from dotenv import load_dotenv
import shutil

# Load environment variables from .env file
load_dotenv()

COLORS = {
    'background': '#002b36', # Solarized Dark background
    'text': '#839496',       # Solarized Dark base0
    'output_text': '#93a1a1', # Solarized Dark base1 (slightly lighter for output)
    'accent': '#268bd2',     # Solarized Dark blue (for command styling)
    'prompt': '#2aa198',     # Solarized Dark cyan (for prompt)
    'button_bg': '#073642',  # Solarized Dark base02 (darker for buttons)
    'button_fg': '#93a1a1',  # Solarized Dark base1 (for button text)
    'error_fg': '#dc322f',   # Solarized Dark red (for errors)
    'cursor_insert_bg': '#eee8d5' # Solarized Light base2 (for high visibility cursor)
}


# --- Gemini AI Setup ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_ready = False
gemini_model = None

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file. Voice AI features will be limited.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')
        gemini_ready = True
        print(f"Gemini AI initialized successfully with model: {gemini_model.model_name if gemini_model else 'N/A'}.")
    except Exception as e:
        print(f"Error initializing Gemini AI: {e}. Voice AI features will be limited.")

# --- Command History ---
command_history = []
history_index = 0

def add_to_history(cmd_to_add):
    global command_history, history_index
    if not cmd_to_add:
        return
    if not command_history or command_history[-1] != cmd_to_add:
        command_history.append(cmd_to_add)
    history_index = len(command_history)


# --- Shell functions with string outputs ---
def removeDirectory(directories):
    messages = []
    if not directories:
        return "No directories specified for removal."
    for dir_name in directories:
        if not dir_name.strip():
            messages.append("Error: Empty directory name specified.")
            continue
        try:
            shutil.rmtree(dir_name) # Use shutil.rmtree for non-empty directories
            messages.append(f"Directory '{dir_name}' and its contents removed.")
        except FileNotFoundError:
            messages.append(f"Directory '{dir_name}' not found.")
        except NotADirectoryError:
            messages.append(f"Error: '{dir_name}' is not a directory.")
        except PermissionError:
            messages.append(f"Permission denied to remove '{dir_name}'.")
        except OSError as e:
            messages.append(f"OS error removing '{dir_name}': {e}")
        except Exception as e:
            messages.append(f"An unexpected error occurred with '{dir_name}': {e}")
    return "\n".join(messages)

def removeFile(files):
    messages = []
    if not files:
        return "No files specified for removal."
    for file_name in files:
        if not file_name.strip():
            messages.append("Error: Empty file name specified.")
            continue
        try:
            os.remove(file_name)
            messages.append(f"File '{file_name}' removed.")
        except FileNotFoundError:
            messages.append(f"File '{file_name}' not found.")
        except PermissionError:
            messages.append(f"Permission denied for '{file_name}'.")
        except IsADirectoryError:
             messages.append(f"Cannot remove '{file_name}'. It is a directory. Use 'rm -r' for directories.")
        except OSError as e:
            messages.append(f"OS error removing '{file_name}': {e}")
        except Exception as e:
            messages.append(f"An unexpected error occurred with '{file_name}': {e}")
    return "\n".join(messages)


def makeFile(file_name):
    if not file_name.strip():
        return "Error: No file name specified."
    try:
        with open(file_name, 'a') as f:
            pass
        return f"File '{file_name}' ensured/created."
    except PermissionError:
        return f"Permission denied: Unable to create/access '{file_name}'."
    except Exception as e:
        return f"An error occurred creating file '{file_name}': {e}"

def makeDirectory(directory_name):
    if not directory_name.strip():
        return "Error: No directory name specified."
    try:
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created."
    except FileExistsError:
        return f"Directory '{directory_name}' already exists."
    except PermissionError:
        return f"Permission denied: Unable to create '{directory_name}'."
    except FileNotFoundError:
        return f"Error creating directory '{directory_name}': Path not found. Create parent directories first."
    except Exception as e:
        return f"An error occurred creating directory '{directory_name}': {e}"

def changeDirectory(path):
    if not path.strip() and path != "..":
        if not path.strip():
          return "Error: No directory path specified for cd."
    try:
        os.chdir(path)
        return f"Changed to {os.getcwd()}"
    except FileNotFoundError:
        return f"The system cannot find the path specified: '{path}'"
    except NotADirectoryError:
        return f"Not a directory: '{path}'"
    except PermissionError:
        return f"Permission denied for path: '{path}'"
    except Exception as e:
        return f"Error changing directory to '{path}': {e}"


def getPresentWorkingDirectory():
    return os.getcwd()

def list_directory():
    try:
        return "  ".join(os.listdir(os.getcwd()))
    except FileNotFoundError:
        return "Error: Current working directory not found."
    except PermissionError:
        return "Error: Permission denied to list current directory."
    except Exception as e:
        return f"Error listing directory: {e}"

def clear_terminal_screen():
    text.delete('1.0', tk.END)
    return "" # No output string, new prompt will be added

# --- Text Widget Redirection ---
class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert("end", string)
        self.text_widget.see("end")

    def flush(self):
        pass

# --- AI Command Interpretation ---
def get_command_from_ai(transcribed_text):
    if not gemini_ready or not gemini_model:
        return {"command": "unknown", "argument": "", "error": "Gemini AI not available."}

    response = None

    prompt = f"""
    You are an AI assistant for a voice-controlled shell.
    User's speech: "{transcribed_text}"

    Your task is to identify which of the following 8 shell commands the user intends to execute and extract any necessary arguments.
    The supported commands are:
    1. ls (list directory contents)
    2. pwd (print working directory)
    3. cd <directory_name> (change directory to <directory_name>)
    4. mkdir <directory_name> (make directory named <directory_name>)
    5. touch <file_name> (create/update file named <file_name>)
    6. rm <file_name> (remove file named <file_name>)
    7. rm -r <directory_name> (remove directory named <directory_name>, recursively)
    8. clear (clear the terminal screen)

    Argument Processing Rules:
    - Convert spoken numbers to digits (e.g., "one" to "1").
    - Interpret spoken characters: "dot" or "period" -> ".", "underscore" or "underline" -> "_", "slash" -> "/", "backslash" -> "\\", "dash" or "hyphen" -> "-"
    - File/directory names can contain spaces. Preserve them.

    Respond ONLY with a JSON object in the following format:
    {{"command": "COMMAND_NAME", "argument": "ARGUMENT_VALUE"}}

    - If the command does not take an argument (ls, pwd, clear), "argument" should be an empty string.
    - For commands like cd, mkdir, touch, rm, rm -r, "argument" should be the identified file/directory name.
    - If the user's speech is unclear, ambiguous, or does not map to any of the supported commands, respond with:
      {{"command": "unknown", "argument": ""}}

    Examples:
    User speech: "list the files" -> {{"command": "ls", "argument": ""}}
    User speech: "where am I?" -> {{"command": "pwd", "argument": ""}}
    User speech: "go to my project folder" -> {{"command": "cd", "argument": "my project folder"}}
    User speech: "make a directory called test results version one" -> {{"command": "mkdir", "argument": "test results version one"}}
    User speech: "create a file report dot txt" -> {{"command": "touch", "argument": "report.txt"}}
    User speech: "delete the file log_backup_file.data" -> {{"command": "rm", "argument": "log_backup_file.data"}}
    User speech: "remove the old_stuff directory" -> {{"command": "rm -r", "argument": "old_stuff"}}
    User speech: "clear the screen" -> {{"command": "clear", "argument": ""}}
    User speech: "what is two plus two" -> {{"command": "unknown", "argument": ""}}

    User speech: "{transcribed_text}"
    JSON Response:
    """
    try:
        response = gemini_model.generate_content(prompt)
        
        if not response or not hasattr(response, 'text'):
            error_message = "Gemini API call did not return a valid response object or text."
            if response and hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                error_message += f" (Prompt blocked: {response.prompt_feedback.block_reason})"
            print(error_message)
            return {"command": "unknown", "argument": "", "error": error_message}

        cleaned_response_text = response.text.strip()
        if cleaned_response_text.startswith("```json"):
            cleaned_response_text = cleaned_response_text[len("```json"):]
        elif cleaned_response_text.startswith("```"):
            cleaned_response_text = cleaned_response_text[len("```"):]
        if cleaned_response_text.endswith("```"):
            cleaned_response_text = cleaned_response_text[:-len("```")]
        cleaned_response_text = cleaned_response_text.strip()

        ai_json = json.loads(cleaned_response_text)
        
        if isinstance(ai_json, dict) and "command" in ai_json and "argument" in ai_json:
            ai_json["argument"] = ai_json.get("argument") or ""
            return ai_json
        else:
            print(f"Error: AI response malformed structure. Raw: {response.text}")
            return {"command": "unknown", "argument": "", "error": "Malformed AI response structure."}

    except json.JSONDecodeError as e:
        raw_resp_text = "'No text in response'"
        if response and hasattr(response, 'text'):
            raw_resp_text = response.text
        print(f"Error decoding JSON from AI: {e}. Raw response text: {raw_resp_text}")
        return {"command": "unknown", "argument": "", "error": f"JSON decode error: {e}"}
    except Exception as e:
        error_message = f"Error calling Gemini API or processing response: {e}"
        if response and hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
             error_message += f" (Prompt blocked: {response.prompt_feedback.block_reason})"
        print(error_message)
        return {"command": "unknown", "argument": "", "error": error_message}


# --- Command Execution ---
def execute_command(command_str_input):
    # Add command to history if it's not empty and not "clear"
    # "clear" is not typically part of bash history either that repopulates the command line
    if command_str_input and command_str_input.strip().lower() != "clear":
        add_to_history(command_str_input.strip())

    command_str = command_str_input.strip() # Use stripped version for processing

    if command_str: # Only insert non-empty command to text widget
        text.insert("end", f"{command_str}\n", "command")
        text.see("end")

    parts = command_str.split(maxsplit=2)
    base_cmd_part1 = parts[0] if len(parts) > 0 else ""
    base_cmd_part2 = parts[1] if len(parts) > 1 else ""
    
    full_base_command = base_cmd_part1.lower() # Match commands case-insensitively
    arg_string = ""

    if full_base_command == "rm" and base_cmd_part2.lower() == "-r":
        full_base_command = "rm -r"
        arg_string = parts[2] if len(parts) > 2 else ""
    elif full_base_command in ["cd", "mkdir", "touch", "rm"]:
        arg_string = command_str[len(base_cmd_part1):].strip()
    
    output = ""
    if full_base_command == "pwd":
        output = getPresentWorkingDirectory()
    elif full_base_command == "ls":
        output = list_directory()
    elif full_base_command == "cd":
        output = changeDirectory(arg_string)
    elif full_base_command == "mkdir":
        output = makeDirectory(arg_string)
    elif full_base_command == "touch":
        output = makeFile(arg_string)
    elif full_base_command == "rm": 
        if not arg_string: output = "No file specified for rm."
        else: output = removeFile([arg_string])
    elif full_base_command == "rm -r":
        if not arg_string: output = "No directory specified for rm -r."
        else: output = removeDirectory([arg_string])
    elif full_base_command == "clear":
        output = clear_terminal_screen() # Clears screen, then prompt will be added
    elif not full_base_command : # Handles empty input after stripping
        pass # Just go to new prompt
    else:
        output = f"Unknown command: '{command_str}'"

    if output: # Only print output if there is some
        text.insert("end", f"{output}\n\n", "output")
    elif full_base_command == "clear": # Special case for clear
        pass # Output already handled by clearing, just need prompt
    elif command_str : # If it was a known command with no output or an unknown command
        text.insert("end", "\n", "output") # Ensure a newline if command was processed


def run_command(cmd):
    execute_command(cmd)
    insert_prompt() # Prompt is inserted after command execution, including after clear

# --- Voice Recognition ---
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        gui_status_update("Listening...")
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=12)
        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            gui_status_update("No speech detected. Try again.")
            return
        except Exception as e:
            print(f"Error during listening: {e}")
            gui_status_update(f"Mic error: {e}")
            return

    gui_status_update("Recognizing speech...")
    print("Recognizing speech...")
    try:
        text_from_speech = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {text_from_speech}")
        gui_status_update(f"Heard: {text_from_speech}. Processing with AI...")

        if not gemini_ready:
            message = "Gemini AI is not initialized."
            print(message)
            gui_status_update(message)
            root.after(0, lambda: text.insert("end", message + "\n", "error"))
            root.after(0, insert_prompt)
            return

        ai_result = get_command_from_ai(text_from_speech)
        
        command_name = ai_result.get("command")
        argument = ai_result.get("argument", "") 
        error_msg = ai_result.get("error")

        if error_msg:
            gui_status_update(f"AI Error: {error_msg}")
            if not command_name or command_name == "unknown":
                 root.after(0, lambda: text.insert("end", f"AI Error: {error_msg}\n", "error"))
                 root.after(0, insert_prompt)
                 return

        KNOWN_COMMANDS = ["ls", "pwd", "cd", "mkdir", "touch", "rm", "rm -r", "clear"] # Added clear

        if command_name in KNOWN_COMMANDS:
            full_command = command_name
            if argument or command_name in ["cd", "mkdir", "touch", "rm", "rm -r"]:
                full_command = f"{command_name} {argument}".strip()
            
            # add_to_history(full_command) # Handled by execute_command now
            gui_status_update(f"AI Mapped to: {full_command}")
            root.after(0, lambda cmd=full_command: run_command(cmd))
        else:
            message = f"AI could not map speech to a known command. (AI result: '{command_name}')"
            if command_name == "unknown" and not argument and not error_msg: 
                 message = "Sorry, I didn't understand that command."
            
            print(message)
            gui_status_update(message)
            root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
            root.after(0, insert_prompt)

    except sr.UnknownValueError:
        message = "Google Speech Recognition could not understand audio."
        print(message)
        gui_status_update(message)
        root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
        root.after(0, insert_prompt)
    except sr.RequestError as e:
        message = f"Speech recognition service error; {e}"
        print(message)
        gui_status_update(message)
        root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
        root.after(0, insert_prompt)
    except Exception as e: 
        message = f"An unexpected error in voice processing: {e}"
        print(message)
        gui_status_update(message)
        root.after(0, lambda m=message: text.insert("end", m + "\n", "error"))
        root.after(0, insert_prompt)

# --- GUI Setup ---
root = tk.Tk()
root.title("VoiceOS Shell")
root.configure(bg=COLORS['background'])
root.geometry("800x600")

frame = tk.Frame(root, bg=COLORS['background'])
frame.pack(fill="both", expand=True, padx=5, pady=(5,0))

text = tk.Text(frame, wrap="word", bg=COLORS['background'], fg=COLORS['text'],
               insertbackground=COLORS['cursor_insert_bg'], font=("Consolas", 11), borderwidth=0,
               undo=True)
text.pack(side="left", fill="both", expand=True, padx=5, pady=5)

scrollbar = tk.Scrollbar(frame, command=text.yview, bg=COLORS['button_bg'], troughcolor=COLORS['background'],
                         activebackground=COLORS['accent']) # Added activebackground
scrollbar.pack(side="right", fill="y")
text.config(yscrollcommand=scrollbar.set)

status_bar_text = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_bar_text, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                      bg=COLORS['button_bg'], fg=COLORS['button_fg'], font=("Consolas", 9))
status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=(0,5))
status_bar_text.set("Ready.")

def gui_status_update(message):
    status_bar_text.set(message)

sys.stdout = TextRedirector(text) # Redirects print statements to the Text widget

text.tag_configure("command", foreground=COLORS['accent'], font=("Consolas", 11, "bold"))
text.tag_configure("output", foreground=COLORS['output_text']) # Using dedicated output color
text.tag_configure("prompt", foreground=COLORS['prompt'], font=("Consolas", 11, "bold"))
text.tag_configure("error", foreground=COLORS['error_fg'])

def insert_prompt():
    # Ensure the insert mark is at the end before inserting prompt, especially after clear
    text.mark_set(tk.INSERT, tk.END)
    text.see(tk.END)
    try:
        prompt_text = f"{os.getcwd()} $ "
    except FileNotFoundError:
        os.chdir(os.path.expanduser("~"))
        prompt_text = f"{os.getcwd()} $ "
        text.insert(tk.END, "Current directory was lost. Reverted to home.\n", "error")

    text.insert(tk.END, prompt_text, "prompt")
    text.mark_set("input_start", f"{tk.END}-1c") # Point right before the last char of prompt
    text.mark_gravity("input_start", "left")
    text.see(tk.END) # Scroll to prompt

insert_prompt()

def start_voice_recognition_thread():
    if not gemini_ready:
        gui_status_update("Gemini AI not ready. Check API Key and console.")
        text.insert("end", "Voice AI is not configured. Check console (GEMINI_API_KEY).\n", "error")
        insert_prompt()
        return
    voice_button.config(state=tk.DISABLED)
    gui_status_update("Initializing mic...")
    root.after(100, lambda: threading.Thread(target=lambda: (recognize_voice(), voice_button.config(state=tk.NORMAL)), daemon=True).start())


style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', 
                background=COLORS['button_bg'], 
                foreground=COLORS['button_fg'], 
                font=("Helvetica", 10, "bold"),
                bordercolor=COLORS['accent'],
                lightcolor=COLORS['button_bg'], 
                darkcolor=COLORS['button_bg'], 
                padding=6)
style.map('TButton',
          background=[('active', COLORS['accent']), ('pressed', '#005f99')], # Darker accent on press
          foreground=[('active', '#FFFFFF'), ('pressed', '#FFFFFF')])

voice_button = ttk.Button(root, text="🎤 Speak Command", command=start_voice_recognition_thread, style='TButton')
voice_button.pack(pady=10, fill=tk.X, padx=20)

def on_key_press(event):
    global history_index
    current_cursor_pos = text.index(tk.INSERT)
    input_start_pos = text.index("input_start")

    # Basic protection against editing output (simplified)
    if text.compare(current_cursor_pos, "<", input_start_pos):
        # Allow navigation keys, copy, select all
        if event.keysym not in ["Left", "Right", "Home", "End", "Up", "Down", "Next", "Prior", "Copy", "c", "C"] \
           and not ( (event.state & 0x0004 and event.keysym.lower() == 'c') or \
                     (event.state & 0x0004 and event.keysym.lower() == 'a') ): # Ctrl+C, Ctrl+A
            text.mark_set(tk.INSERT, input_start_pos)

    if event.keysym == "Return":
        command_line_content = text.get("input_start", f"{tk.END}-1c") # Get text from prompt start to current end
        if command_line_content.strip() == "exit": # Handle exit command
            root.quit()
        elif command_line_content.strip(): # If there is a command
            text.insert(tk.END, "\n") # Move to next line for output
            run_command(command_line_content.strip()) # Execute it
        else: # Empty command, just show new prompt
            text.insert(tk.END, "\n")
            insert_prompt()
        return "break" 
    
    elif event.keysym == "Up":
        if command_history:
            if history_index > 0:
                history_index -= 1
            current_input_end = f"{tk.END}-1c"
            if text.compare("input_start", "<", current_input_end): # if there is text after prompt
                 text.delete("input_start", current_input_end)
            elif text.index("input_start") == text.index(current_input_end): # if prompt is end-1c, meaning input start IS the end.
                 pass # Nothing to delete if input area is empty

            text.insert("input_start", command_history[history_index])
            text.mark_set(tk.INSERT, tk.END) # Move cursor to very end
        return "break"

    elif event.keysym == "Down":
        if command_history:
            current_input_end = f"{tk.END}-1c"
            if history_index < len(command_history) -1 :
                history_index += 1
                if text.compare("input_start", "<", current_input_end):
                     text.delete("input_start", current_input_end)
                elif text.index("input_start") == text.index(current_input_end):
                     pass
                text.insert("input_start", command_history[history_index])
            elif history_index == len(command_history) - 1: # At last item, next is blank
                history_index +=1
                if text.compare("input_start", "<", current_input_end):
                     text.delete("input_start", current_input_end)
                elif text.index("input_start") == text.index(current_input_end):
                     pass
            text.mark_set(tk.INSERT, tk.END)
        return "break"

    elif event.keysym == "Backspace":
        # Prevent deleting the prompt itself
        if text.compare(tk.INSERT, "<=", "input_start"):
            return "break"
    
    elif event.keysym == "Left":
        # Prevent moving cursor to the left of input_start mark
        if text.compare(f"{tk.INSERT}-1c", "<", "input_start"):
            return "break"
    
    elif event.keysym == "Home":
        # Move cursor to beginning of current input line
        text.mark_set(tk.INSERT, "input_start")
        return "break"

text.bind("<Key>", on_key_press)
text.focus_set()

if not gemini_ready:
    initial_msg = "Gemini AI not configured. Check console (GEMINI_API_KEY).\n"
    text.insert("1.0", initial_msg, "error")
    status_bar_text.set("AI not ready. Check API key.")

root.mainloop()