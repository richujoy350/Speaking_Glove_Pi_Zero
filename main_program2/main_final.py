import tkinter as tk
import pyttsx3

import subprocess
import threading


class Application:
    def __init__(self, root):
        self.root = root
        self.root.focus_force()
        # Load and display the image
        self.image_path = "images/glovemain.png"
        self.photo = tk.PhotoImage(file=self.image_path)
        self.label = tk.Label(root, image=self.photo)
        self.label.pack(fill=tk.BOTH, expand=tk.YES)

        self.default_binding()
        # Create a flag to check if a process is running
        self.process_running = False

        # Start the Tkinter main loop
        root.mainloop()

    def play_audio(self, text):
        # engine = pyttsx3.init()
        # threading.Thread(target=engine.say(text))
        # engine.runAndWait()
        subprocess.call(["espeak", "-v", "ml+m3", "-s", "120", "-k", "0.8", text])

    def display_image(self, image_path):
        photo = tk.PhotoImage(file=image_path)
        self.label.configure(image=photo)
        self.label.image = photo

    def open_tts_functionality(self, event=None):
        # Hide the image label temporarily
        self.label.pack_forget()

        # Create a text box
        self.text_box = tk.Text(self.root, height=10, width=50)
        self.text_box.pack(pady=10)
        self.text_box.focus_set()  # Set focus on the text box

        # Create a "Speak" button
        self.speak_button = tk.Button(self.root, text="Speak", command=self.speak_text)
        self.text_box.bind("<Return>", self.speak_text)

        # Set the focus to the text box
        self.root.bind("<Escape>", lambda event: self.default_binding())
        # Bind Ctrl+q to quit application
        self.root.bind("<Control-q>", self.quit_application)
        self.root.unbind("1")
        self.root.unbind("2")
        self.root.unbind("3")
        self.root.unbind("4")
        self.root.unbind("5")
        self.root.unbind("6")
        self.speak_button.pack()

    def open_stt_functionality(self, event=None):
        self.its_default_binding()

    def open_saved_functionality(self, event=None):
        self.its_default_binding()

    def open_its_functionality(self, event=None):
        self.its_default_binding()
        self.image = "images/its_main.png"
        self.display_image(self.image)

    def open_general_functionality(self, event=None):
        if not self.process_running:
            self.process_running = True
            threading.Thread(
                target=self.display_icon_and_speak,
                args=("images/general-icon.png", "general", "images/general.png"),
            ).start()
            # Rebind keys '1', '2', '3', and '4' to speak specific texts
            self.root.bind(
                "1",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/toilet-icon.png", "toilet", "images/general.png"),
                ).start(),
            )
            self.root.bind(
                "2",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/hungry-icon.png", "Hungry", "images/general.png"),
                ).start(),
            )
            self.root.bind(
                "3",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/sleepy-icon.png", "Sleepy", "images/general.png"),
                ).start(),
            )
            self.root.bind(
                "4",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/pain-icon.png", "Pain", "images/general.png"),
                ).start(),
            )
            self.root.bind(
                "<Escape>",
                self.open_its_functionality,
            )

    def open_emergency_functionality(self, event=None):
        if not self.process_running:
            self.process_running = True
            threading.Thread(
                target=self.display_icon_and_speak,
                args=("images/emergency-icon.png", "emergency", "images/emergency.png"),
            ).start()
            self.root.bind(
                "1",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=(
                        "images/policestation-icon.png",
                        "Police",
                        "images/emergency.png",
                    ),
                ).start(),
            )
            self.root.bind(
                "2",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=(
                        "images/hospital-icon.png",
                        "hospital",
                        "images/emergency.png",
                    ),
                ).start(),
            )
            self.root.bind(
                "3",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=(
                        "images/ambulance-icon.png",
                        "Ambulance",
                        "images/emergency.png",
                    ),
                ).start(),
            )
            self.root.bind(
                "4",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=(
                        "images/firedept-icon.png",
                        "Fire Force",
                        "images/emergency.png",
                    ),
                ).start(),
            )

    def open_food_functionality(self, event=None):
        if not self.process_running:
            self.process_running = True
            threading.Thread(
                target=self.display_icon_and_speak,
                args=("images/food-icon.png", "food", "images/food.png"),
            ).start()
            self.root.bind(
                "1",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/water-icon.png", "water", "images/food.png"),
                ).start(),
            )
            self.root.bind(
                "2",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/tea-icon.png", "tea", "images/food.png"),
                ).start(),
            )
            self.root.bind(
                "3",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/juice-icon.png", "juice", "images/food.png"),
                ).start(),
            )
            self.root.bind(
                "4",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/breakfast-icon.png", "breakfast", "images/food.png"),
                ).start(),
            )
            self.root.bind(
                "5",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/lunch-icon.png", "lunch", "images/food.png"),
                ).start(),
            )
            self.root.bind(
                "6",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/dinner-icon.png", "dinner", "images/food.png"),
                ).start(),
            )

    def open_travel_functionality(self, event=None):
        if not self.process_running:
            self.process_running = True
            threading.Thread(
                target=self.display_icon_and_speak,
                args=("images/travel-icon.png", "travel", "images/travel.png"),
            ).start()
            self.root.bind(
                "1",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/busstop-icon.png", "Bus Stop", "images/travel.png"),
                ).start(),
            )
            self.root.bind(
                "2",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/auto-icon.png", "Auto Rickshaw", "images/travel.png"),
                ).start(),
            )
            self.root.bind(
                "3",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=("images/taxi-icon.png", "Taxi", "images/travel.png"),
                ).start(),
            )
            self.root.bind(
                "4",
                lambda event: threading.Thread(
                    target=self.display_icon_and_speak,
                    args=(
                        "images/trainstation-icon.png",
                        "Railway Station",
                        "images/travel.png",
                    ),
                ).start(),
            )

    def default_binding(self, event=None):
        # Reset the default bindings
        # Bind key '1' to the TTS functionality
        self.root.bind("1", self.open_tts_functionality)
        # Bind key '2' to the TTS functionality
        self.root.bind("2", self.open_stt_functionality)
        # Bind key '4' to the TTS functionality
        self.root.bind("3", self.open_its_functionality)
        # Bind key '3' to the TTS functionality
        self.root.bind("4", self.open_saved_functionality)
        # Bind Escape key to go back to default binding
        self.root.bind("<Escape>", self.default_binding)
        # Bind Ctrl+q to quit application
        self.root.bind("<Control-q>", self.quit_application)

        self.root.unbind("5")
        self.root.unbind("6")
        self.display_image(self.image_path)
        self.process_running = False

    def its_default_binding(self, event=None):
        # Reset the default bindings
        # Bind key '1' to the TTS functionality
        self.root.bind("1", self.open_general_functionality)
        # Bind key '2' to the TTS functionality
        self.root.bind("2", self.open_emergency_functionality)
        # Bind key '4' to the TTS functionality
        self.root.bind("3", self.open_food_functionality)
        # Bind key '3' to the TTS functionality
        self.root.bind("4", self.open_travel_functionality)
        # Bind Escape key to go back to default binding
        self.root.bind("<Escape>", self.default_binding)
        # Bind Ctrl+q to quit application
        self.root.bind("<Control-q>", self.quit_application)

        self.root.unbind("5")
        self.root.unbind("6")

        self.process_running = False

    def quit_application(self, event=None):
        self.root.destroy()

    def display_icon_and_speak(self, icon, text_to_speak, image_after):
        threading.Thread(target=self.display_image(icon))
        threading.Thread(target=self.play_audio(text_to_speak))
        self.root.after(500, lambda: self.display_image(image_after))

        # self.play_audio(text_to_speak)
        self.process_running = False

    def speak_text(self, event=None):
        text_to_speak = self.text_box.get("1.0", tk.END).strip()
        if text_to_speak:
            threading.Thread(target=self.play_audio, args=(text_to_speak,)).start()


# Create the Tkinter window
root = tk.Tk()
root.geometry("480x320")  # Set the window size to 480x320
root.attributes("-fullscreen", True)  # Set the window to full screen


# Create an instance of the Application class
app = Application(root)
