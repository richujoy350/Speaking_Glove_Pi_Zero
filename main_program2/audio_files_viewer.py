import os
import tkinter as tk
from pygame import mixer
import sounddevice as sd
import soundfile as sf
import subprocess

mode = None
recording = None
record = None# Global variable to store the recording data

def play_audio(event):
    key = event.char.lower()
    if key in number_keys:
        index = number_keys.index(key)
        file_path = audio_file_paths[index]
        mixer.music.load(file_path)
        mixer.music.play()
        window.after(100, check_music_status)

def record_audio(event):
    global recording
    stop_button.pack()
    print("Recording audio")
    key = event.char.lower()
    stop_button.config(state=tk.NORMAL)
    global record
    record = number_keys.index(key)
    #file_path = audio_file_paths[index]
    print("recording begins")
    recording = sd.rec(int(10 * samplerate), samplerate=samplerate, channels=channels)
    print('before')
    #sd.wait()
    #sf.write(file_path, recording, samplerate)
    #print('after')
   # show_initial_gui()

def stop_audio():
    global recording
    print("stop")
    sd.stop()
    #key = event.char.lower()
    #index = number_keys.index(key)
    file_path = audio_file_paths[record]
    sf.write(file_path, recording, samplerate)
    recording = None
    stop_button.config(state=tk.DISABLED)
    stop_button.pack_forget()# Disable the stop button
    show_initial_gui()
    return

def check_music_status():
    if mixer.music.get_busy():
        window.after(100, check_music_status)
    else:
        show_initial_gui()

def show_initial_gui():
    page_name.config(text="Audio Messages")
    frame.pack()
    record_button.pack_forget()
    play_button.pack_forget()

def show_audio_files(event):
    key = event.char.lower() if event else None
    print("Audio files listed")
    if key == 'r':
        page_name.config(text="Audio Recorder")
        record_button.configure(command=record_audio)  # Update the command to record_audio
        record_button.pack_forget()
        play_button.pack_forget()
  # Show the stop button
    if key == 'p':
        page_name.config(text="Audio Player")
        play_button.configure(command=play_audio)
        play_button.pack_forget()
        record_button.pack_forget()
        stop_button.pack_forget()  # Hide the stop button
    frame.pack(pady=20)

def play_audio_by_index(index):
    file_path = audio_file_paths[index]
    event = tk.Event()  # Create a new event object
    event.char = number_keys[index]  # Set the char attribute to the corresponding key
    play_audio(event)

def handle_key(event):
    key = event.char.lower()
    global mode
    if key == 'r':
        mode = 'r'
        show_audio_files(event)
        return
    elif key == 'p':
        mode = 'p'
        show_audio_files(event)
        return
    elif key == 's' :
        stop_audio()
        return
    elif key == "x" :
        mixer.music.stop()

    if key in number_keys:
        if mode == 'r':
            index = number_keys.index(key)
            record_audio(event)
        if mode == 'p':
            index = number_keys.index(key)
            play_audio_by_index(index)
    elif event.keysym.lower() == "control_r":
        go_back()

def go_back():
    window.destroy()
    subprocess.Popen(["python", "saved_messages.py"])

folder_path = "/home/richard/Speaking_Glove/code_bases/main_program2/audio"  # Specify the folder path here

audio_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
audio_files.sort()

number_keys = ['1', '2', '3', '4', '5']

audio_file_paths = [os.path.join(folder_path, file) for file in audio_files]

window = tk.Tk()
window.title("Audio Player")
window.attributes("-fullscreen", True)

page_name_frame = tk.Frame(window)
page_name_frame.pack(side=tk.TOP, pady=10)
page_name = tk.Label(page_name_frame, text="Audio Messages", font=("Helvetica", 16))
page_name.pack()


# Create the buttons for record, play, and stop
back_button = tk.Button(window, text="Back",font=('Arial', 12), command=show_initial_gui)
record_button = tk.Button(window, text="Record", font=('Arial', 12), command=show_audio_files)
play_button = tk.Button(window, text="Play", font=('Arial', 12), command=show_audio_files)
stop_button = tk.Button(window, text="Stop", font=('Arial', 12), command=stop_audio, state=tk.DISABLED)  # Initially disabled

# Create a frame for the audio files
frame = tk.Frame(window)

# Create buttons for each audio file
for i, audio_file in enumerate(audio_files):
    button = tk.Button(frame, text=audio_file, font=('Arial', 12), command=lambda index=i: play_audio_by_index(index))
    button.pack()

# Bind the keyboard event to the window
window.bind('<Key>', handle_key)

# Initialize the mixer
mixer.init()

# Set the recording parameters
samplerate = 44100  # Sample rate
channels = 2  # Number of channels (stereo)

# Show the initial GUI with record, play, and stop buttons
show_initial_gui()

# Run the main event loop
window.mainloop()

# Cleanup and quit the mixer
mixer.quit()