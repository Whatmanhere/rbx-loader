import tkinter as tk
from tkinter import ttk
import time
import os
import subprocess

class RobloxLoader:
    def __init__(self, master):
        self.master = master
        self.master.title("Roblox Loader")
        self.master.geometry("400x200")
        self.master.configure(bg="black")

        # Set window icon
        icon = tk.PhotoImage(file="fly.png")
        master.iconphoto(False, icon)

        # Loading bar
        self.progressbar = ttk.Progressbar(master, length=300, mode="determinate", style="custom.Horizontal.TProgressbar")
        self.progressbar.place(relx=0.5, rely=0.3, anchor="center")

        # Set background and progress color
        style = ttk.Style()
        style.theme_use('clam')  # Choose your preferred theme
        style.configure("custom.Horizontal.TProgressbar", background="black", troughcolor="white", foreground="white")

        # Modern cancel button
        self.cancel_button = ttk.Button(master, text="Cancel", command=self.close_loader)
        self.cancel_button.place(relx=0.5, rely=0.5, anchor="center")

        # Start loading
        self.load_roblox(25)

    def load_roblox(self, target_value):
        current_value = self.progressbar['value']
        while current_value < target_value:
            current_value += 1
            self.progressbar['value'] = current_value
            self.master.update_idletasks()
            time.sleep(0.02)  # Simulate loading time

        # Teleport every 25%
        if target_value < 100:
            self.master.after(2000, self.load_roblox, target_value + 25)
        else:
            # Open Roblox after loading
            self.open_roblox()

    def open_roblox(self):
        try:
            # Path to Roblox Player executable
            roblox_exe_path = os.path.join(os.environ["LOCALAPPDATA"], "Bloxstrap", "Versions", "version-bca459bcd1854ce4", "RobloxPlayerBeta.exe")
            
            # Launch Roblox Player
            subprocess.Popen([roblox_exe_path])
        except FileNotFoundError:
            print("RobloxPlayerBeta.exe not found.")

    def close_loader(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()

    loader = RobloxLoader(root)
    root.mainloop()
