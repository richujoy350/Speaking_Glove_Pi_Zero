import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import os
import subprocess

categories = ['General', 'Emergency', 'Food', 'Travel']
current_category = None
speech_engine = pyttsx3.init()

def speak_text(text, repeat=3):
    for _ in range(repeat):
        speech_engine.say(text)
    speech_engine.runAndWait()

def handle_key(event):
    global current_category

    if event.char.isdigit():
        key_number = int(event.char)
        if 1 <= key_number <= len(categories):
            current_category = categories[key_number - 1]
            speak_text(current_category, repeat=3)
            # Load the next page or perform the desired action for the category

def go_back(event=None):
    root.destroy()
    subprocess.Popen(["python", "main.py"])

def main():
    global root
    root = tk.Tk()
    root.title("Image to Speech")
    root.attributes("-fullscreen", True)

    # Load and display the category images
    image_folder = '/home/richard/Speaking_Glove/code_bases/main_program2/images/'
    category_images = []
    for i, category in enumerate(categories):
        image_path = os.path.join(image_folder, f"{category.lower()}.jpg")
        image = Image.open(image_path)
        image = image.resize((500, 500))  # Adjust the image size as needed
        category_images.append(ImageTk.PhotoImage(image))

    # Create labels for the category images
    image_labels = []
    for i, image in enumerate(category_images):
        label = tk.Label(root, image=image)
        label.pack(side=tk.LEFT, padx=20)
        image_labels.append(label)

    # Bind the keyboard event to handle category selection
    root.bind('<Key>', handle_key)
    root.bind('<Control_R>', go_back)

    root.mainloop()

if __name__ == '__main__':
    main()
