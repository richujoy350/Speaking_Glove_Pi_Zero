import tkinter as tk
import subprocess

#def text_to_speech(text):
#    subprocess.call(["espeak", "-v", "ml+m3", "-s", "120", text])

def text_to_speech(text):
    subprocess.call(["espeak", "-v", "ml+m3", "-s", "120", "-k", "0.8", text])

def speak_button_callback(event=None):
    text = input_text.get("1.0", tk.END).strip()
    text_to_speech(text)

def go_back(event=None):
    root.destroy()
    subprocess.Popen(["python", "main.py"])

def main():
    global input_text, root

    root = tk.Tk()
    root.title("Text-to-Speech")

    input_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
    input_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    input_text.focus_set()  # Set focus to the input_text widget

    speak_button = tk.Button(root, text="Speak", command=speak_button_callback)
    speak_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    home_button = tk.Button(root, text="Home", command=go_back)
    home_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    # Bind Enter key to speak functionality
    root.bind('<Return>', speak_button_callback)
    # Bind right control key to go back to home
    root.bind('<Control_R>', go_back)

    # Automatically focus the window
    root.focus_force()

    root.mainloop()

if __name__ == '__main__':
    main()
