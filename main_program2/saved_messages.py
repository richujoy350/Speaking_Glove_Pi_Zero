import tkinter as tk
import subprocess

class SavedMessagesPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Saved Messages")
        self.root.attributes("-fullscreen", True)

        self.label_title = tk.Label(self.root, text="Saved Messages", font=("Helvetica", 20))
        self.label_title.pack()

        self.button_audio = tk.Button(self.root, text="Audio", font=("Helvetica", 12), command=self.show_audio_files)
        self.button_audio.pack()

        self.button_text = tk.Button(self.root, text="Text", font=("Helvetica", 12), command=self.show_text_files)
        self.button_text.pack()

        self.root.focus_force()
        self.root.bind('1', self.open_text_files)
        self.root.bind('2', self.open_audio_files)
        self.root.bind('<Control_R>', self.go_back)
        self.root.mainloop()

    def show_audio_files(self):
        file_list = self.get_files_from_directory("audio", ".wav")
        self.show_files_dialog("Audio Files", file_list)

    def show_text_files(self):
        file_list = self.get_files_from_directory("text", ".txt")
        self.show_files_dialog("Text Files", file_list)

    def get_files_from_directory(self, directory, extension):
        files = []
        path = os.path.join(os.getcwd(), directory)
        for file in os.listdir(path):
            if file.endswith(extension):
                files.append(file)
        return files

    def show_files_dialog(self, title, file_list):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        for i, file in enumerate(file_list):
            label = tk.Label(dialog, text=file)
            label.pack()

    def quit_application(self, event=None):
        self.root.destroy()

    def open_text_files(self,event=None):
        self.root.destroy()
        subprocess.Popen(["python", "text_files_viewer.py"])

    def open_audio_files(self,event=None):
        self.root.destroy()
        subprocess.Popen(["python", "audio_files_viewer.py"])

    def go_back(self, event=None):
        self.root.destroy()
        subprocess.Popen(["python", "main.py"])

if __name__ == "__main__":
    root = tk.Tk()
    saved_messages_page = SavedMessagesPage(root)
