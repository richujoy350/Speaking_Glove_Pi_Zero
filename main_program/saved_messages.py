import tkinter as tk
import os

class SavedMessagesPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Saved Messages")
        self.root.geometry("400x300")

        self.label_title = tk.Label(self.root, text="Saved Messages", font=("Helvetica", 20))
        self.label_title.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.button_audio = tk.Button(self.root, text="Audio", font=("Helvetica", 12), command=self.show_audio_files)
        self.button_audio.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.button_text = tk.Button(self.root, text="Text", font=("Helvetica", 12), command=self.show_text_files)
        self.button_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

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

if __name__ == "__main__":
    root = tk.Tk()
    saved_messages_page = SavedMessagesPage(root)