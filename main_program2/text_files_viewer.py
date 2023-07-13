import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess

text_files = []
current_file_path = None  # Introduce a global variable to store the current file path

def load_text_files(folder_path):
    global text_files
    text_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    return text_files

def show_initial_gui():
    file_buttons_frame.pack()
    text_area.pack_forget()
    back_button.pack_forget()
    edit_button.pack_forget()
    save_button.pack_forget()
    clear_text_area()

def show_text(file_path):
    global current_file_path  # Set the value of current_file_path when showing a text file
    current_file_path = file_path
    file_buttons_frame.pack_forget()
    text_area.pack()
    back_button.pack()
    edit_button.pack()
    text_area.config(state=tk.NORMAL)  # Enable the text area
    text_area.delete(1.0, tk.END)
    with open(file_path, 'r') as file:
        content = file.read()
        text_area.insert(tk.INSERT, content)
    text_area.config(state=tk.DISABLED)  # Disable text area initially
    save_button.pack_forget()

def edit_text():
    text_area.config(state=tk.NORMAL)
    text_area.focus_set()

def save_text():
    global current_file_path  # Access the current_file_path variable
    if current_file_path:
        content = text_area.get(1.0, tk.END)
        with open(current_file_path, 'w') as file:
            file.write(content)
        text_area.config(state=tk.DISABLED)
        text_area.focus_set()  # Move focus away from the text area to hide the cursor
        edit_button.pack()
        save_button.pack_forget()

def clear_text_area():
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.config(state=tk.DISABLED)

def load_and_show_text_files(folder_path):
    text_files = load_text_files(folder_path)
    if text_files:
        for index, file in enumerate(text_files, start=1):
            if index > 5:
                break
            file_path = os.path.join(folder_path, file)
            file_button = tk.Button(file_buttons_frame, text=f"{index}. {file}", command=lambda path=file_path: show_text(path))
            file_button.pack(side=tk.TOP)

def handle_keyboard_event(event):
    if event.char.isdigit():
        key_number = int(event.char)
        if 1 <= key_number <= len(text_files):
            file_path = os.path.join(folder_path, text_files[key_number - 1])
            show_text(file_path)
    elif event.keysym.lower() == "tab":
        show_initial_gui()
    elif event.keysym.lower() == "shift_l":
        edit_text()
    elif event.keysym.lower() == "shift_r":
        save_text()
    elif event.keysym.lower() == "control_r":
        go_back()

def go_back():
    root.destroy()
    subprocess.Popen(["python", "saved_messages.py"])

# Specify the folder path
folder_path = "/home/richard/Speaking_Glove/code_bases/main_program2/text"

# Load text files
text_files = load_text_files(folder_path)

# Create the main window
root = tk.Tk()
root.title("Text Files Viewer")
root.attributes("-fullscreen", True)

# Create a frame for file buttons
file_buttons_frame = tk.Frame(root)

# Create a text area to display the content
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)

# Button to go back to initial GUI
back_button = tk.Button(root, text="Back", command=show_initial_gui)

# Button to edit the text
edit_button = tk.Button(root, text="Edit", command=edit_text)

# Button to save changes
save_button = tk.Button(root, text="Save Changes", command=save_text)
save_button.pack_forget()  # Hide save button initially

# Bind keyboard event handler
root.bind("<Key>", handle_keyboard_event)

# Load and show initial text files GUI
load_and_show_text_files(folder_path)

# Create a home button to return to the main.py interface
home_button = tk.Button(root, text="Home", command=go_back)
home_button.pack(side=tk.TOP)

# Show initial GUI
show_initial_gui()

# Run the GUI main loop
root.mainloop()
