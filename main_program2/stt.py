import tkinter as tk
import speech_recognition as sr
import subprocess

def stt_page(root):
    root.title("STT-Glove")
    root.geometry("800x600")
    root.attributes("-fullscreen", True)

    text = tk.Text(root, font=("Sitka Small", 40), bd=2, relief=tk.GROOVE, wrap=tk.WORD, undo=True)
    text.pack(fill=tk.BOTH, expand=True)

    def go_back(event=None):
        root.destroy()
        subprocess.Popen(["python", "main.py"])

    def set_text(text_value):
        text.delete("1.0", tk.END)
        text.insert(tk.END, text_value)

    def start_capture(event):
        set_text("Please talk")
        root.after(100, capture)

    def capture():
        try:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()

            with microphone as source:
                audio_data = recognizer.record(source, duration=5)

            set_text("Recognizing...")

            text_value = recognizer.recognize_google(audio_data)

            set_text(text_value)

        except sr.UnknownValueError:
            set_text("Unable to recognize speech")

        except sr.RequestError as e:
            set_text(f"Error occurred: {str(e)}")

    home_button = tk.Button(root, text="Home", command=go_back, font=("Arial", 16), bg="blue", fg="white", padx=10, pady=5)
    home_button.pack(side=tk.BOTTOM, pady=10)

    root.bind("<Return>", start_capture)
    root.bind("<Control_R>", go_back)  # Bind right control key to go back to home
    root.focus_force()

if __name__ == "__main__":
    root = tk.Tk()
    stt_page(root)
    root.mainloop()
