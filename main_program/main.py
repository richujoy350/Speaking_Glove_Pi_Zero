import tkinter as tk
import subprocess

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Speaking Glove")
        self.root.geometry("400x300")

        self.label_title = tk.Label(self.root, text="Speaking Glove", font=("Helvetica", 20))
        self.label_title.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.button_tts = tk.Button(self.root, text="TTS", font=("Helvetica", 12), command=self.open_tts_functionality)
        self.button_tts.place(relx=0.9, rely=0.5, anchor=tk.E)

        self.button_stt = tk.Button(self.root, text="STT", font=("Helvetica", 12), command=self.open_stt_functionality)
        self.button_stt.place(relx=0.9, rely=0.6, anchor=tk.E)

        self.button_images_to_speech = tk.Button(self.root, text="Images to Speech", font=("Helvetica", 12), command=self.open_images_to_speech_functionality)
        self.button_images_to_speech.place(relx=0.9, rely=0.7, anchor=tk.E)

        self.button_save_messages = tk.Button(self.root, text="Save Messages", font=("Helvetica", 12), command=self.open_save_messages_functionality)
        self.button_save_messages.place(relx=0.9, rely=0.8, anchor=tk.E)

        # Automatically focus the window
        self.root.focus_force()
        # Bind key '1' to the TTS functionality
        self.root.bind('1', self.open_tts_functionality)
        # Bind key '2' to the TTS functionality
        self.root.bind('2', self.open_stt_functionality)
        # Bind key '4' to the TTS functionality
        self.root.bind('4', self.open_saved_messages_functionality)

        self.root.mainloop()

    def open_tts_functionality(self, event=None):
        self.root.destroy()
        subprocess.Popen(["python", "tts.py"])

    def open_stt_functionality(self, event=None):
        self.root.destroy()
        subprocess.Popen(["python", "stt.py"])

    def open_images_to_speech_functionality(self):
        # Logic to open Images to Speech functionality
        pass

    def open_saved_messages_functionality(self, event=None):
        root.destroy()
        subprocess.Popen(["python", "saved_messages.py"])

if __name__ == '__main__':
    root = tk.Tk()
    home_page = HomePage(root)
