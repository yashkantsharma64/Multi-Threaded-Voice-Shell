# 🗣️🎙️ VoiceOS Shell: Your Voice, Your Command  Terminal Terminal 💻✨

**(Powered by Python, Tkinter, SpeechRecognition, and Google Gemini AI)**

![VoiceOS Shell Demo GIF](https://i.imgur.com/YOUR_DEMO_GIF_HERE.gif) 
*(Recommendation: Create a short GIF showcasing the voice commands and GUI, then replace the placeholder link above. Tools like Giphy Capture, ScreenToGif, or Kap are great for this.)*

---

## 🚀 Overview

Tired of typing? Step into the future with **VoiceOS Shell**, a Python-based, voice-activated terminal that brings the power of your voice directly to your command line. Simply speak your commands, and watch them execute! Leveraging the intelligence of **Google's Gemini AI**, VoiceOS Shell understands your intent even with slight variations in speech, making for a fluid and intuitive user experience.

Beyond voice, it functions as a traditional terminal, allowing typed commands and offering a familiar interface with a customizable, sleek theme.

---

## ✨ Features

*   **🎤 Voice-Activated Commands**: Control your shell with natural language.
    *   Say "list files" or "show me everything" and `ls` runs.
    *   "Make a folder named new project" executes `mkdir new project`.
*   **🧠 AI-Powered Understanding**: Utilizes Google Gemini AI for:
    *   Flexible command recognition – no need for exact phrasing!
    *   Smart argument parsing (e.g., "create report dot txt" becomes `touch report.txt`).
*   **⌨️ Traditional Typing**: Fall back to keyboard input whenever you prefer.
*   **📜 Command History**: Navigate through your previously entered commands using **Up/Down arrow keys**.
*   **🎨 Customizable Theming**: Comes with a cool "Solarized Dark" inspired theme. (Colors are easily adjustable in the code!)
*   **🛠️ Core Shell Functionality**:
    *   `ls`: List directory contents.
    *   `pwd`: Print working directory.
    *   `cd <directory>`: Change directory.
    *   `mkdir <directory>`: Create a new directory.
    *   `touch <file>`: Create a new empty file or update timestamp.
    *   `rm <file>`: Remove a file.
    *   `rm -r <directory>`: Remove a directory and its contents (recursively).
    *   `clear`: Clear the terminal screen.
*   **💻 Cross-Platform GUI**: Built with Tkinter for a native look and feel.
*   **📢 Real-time Feedback**: Status bar updates for listening, recognizing, and AI processing states.

---

## 🔧 Getting Started

### Prerequisites

*   Python 3.7+
*   A microphone connected to your system.
*   A Google Gemini API Key.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/VoiceOS-Shell.git
    cd VoiceOS-Shell
    ```

2.  **Set up Google Gemini API Key:**
    *   Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create an API key.
    *   Create a file named `.env` in the project's root directory (`VoiceOS-Shell/`).
    *   Add your API key to the `.env` file like this:
        ```env
        GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
        ```
        **Important:** Make sure this `.env` file is in your `.gitignore` if you plan to push your project to a public repository to avoid exposing your API key!

3.  **Install Dependencies:**
    It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    Then install the required packages:
    ```bash
    pip install -r requirements.txt 
    ```
    *(If a `requirements.txt` is not provided, install manually):*
    ```bash
    pip install SpeechRecognition PyAudio google-generativeai python-dotenv Pillow
    ```
    *   **PyAudio Notes**: Installation can sometimes be tricky.
        *   On **Linux**: You might need `sudo apt-get install python3-pyaudio portaudio19-dev`
        *   On **macOS**: `brew install portaudio` then `pip install pyaudio`
        *   On **Windows**: `pip install pipwin` then `pipwin install pyaudio` might work, or download a precompiled wheel.
    *   **Pillow** (`pip install Pillow`): Included if you add image support (like the demo GIF in the Tkinter window later, not currently in the script but good for advanced READMEs).

4.  **Run the Application:**
    ```bash
    python VoiceOS.py
    ```

---

## 🗣️ How to Use

1.  **Speak Command Button**: Click the "🎤 Speak Command" button.
2.  **Speak**: The status bar will indicate "Listening...". Clearly speak one of the supported commands (e.g., "list files", "make a directory called photos", "go to documents").
3.  **Execution**:
    *   The shell will show what it recognized.
    *   The AI will interpret it and map to a command.
    *   The command will be executed, and output will be displayed.
4.  **Type Commands**: You can also type commands directly into the terminal prompt and press `Enter`.
5.  **Command History**:
    *   Press the **Up Arrow** key to cycle through previous commands.
    *   Press the **Down Arrow** key to cycle forward if you've gone back.
6.  **Clear Screen**: Type `clear` or say "clear screen" to clear the terminal display.
7.  **Exit**: Type `exit` and press `Enter` to close the shell.

---

## 🎨 Customization

The visual theme (colors for background, text, prompt, etc.) is defined in the `COLORS` dictionary at the beginning of `VoiceOS.py`. Feel free to experiment and create your own look!

```python
COLORS = {
    'background': '#002b36',
    'text': '#839496',
    # ... and so on
}