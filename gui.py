# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from customtkinter import *


class FishingApp:
    def __init__(self, main_agent):
        self.app = CTk(fg_color="#202020")
        self.app.title("WoW Multi-Tool")
        self.app.geometry("600x400")
        self.main_agent = main_agent
        set_appearance_mode("dark")

        # Create navigation menu
        self.create_navigation_menu()

        # Create frames for each section
        self.main_menu_frame = self.create_main_menu_frame()
        self.fishing_frame = self.create_fishing_frame()
        self.grinding_frame = self.create_grinding_frame()
        self.healing_frame = self.create_healing_frame()
        self.tracking_frame = self.create_tracking_frame()
        self.settings_frame = self.create_settings_frame()
        self.about_frame = self.create_about_frame()

        # Initially show the main menu frame
        self.show_frame(self.main_menu_frame)

        self.update_zone_display()

        self.app.mainloop()

    def create_navigation_menu(self):
        # Frame for navigation buttons
        nav_frame = CTkFrame(self.app, width=100, fg_color="#202020")
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_menu_label = CTkLabel(nav_frame, text="WoW Multi-Tool", font=("Arial", 16))
        self.main_menu_label.pack(pady=5, padx=5, fill=tk.X)

        self.main_menu_button = self.create_button(
            nav_frame, "Main Menu", lambda: self.show_frame(self.main_menu_frame)
        )
        self.main_menu_button.pack(pady=5, padx=15, fill=tk.X)

        self.fishing_button = self.create_button(
            nav_frame, "Fishing Bot", lambda: self.show_frame(self.fishing_frame)
        )
        self.fishing_button.pack(pady=5, padx=15, fill=tk.X)

        self.grinding_button = self.create_button(
            nav_frame, "Grinding Bot", lambda: self.show_frame(self.grinding_frame)
        )
        self.grinding_button.pack(pady=5, padx=15, fill=tk.X)

        self.healing_button = self.create_button(
            nav_frame, "Healing Bot", lambda: self.show_frame(self.healing_frame)
        )
        self.healing_button.pack(pady=5, padx=15, fill=tk.X)

        self.tracking_button = self.create_button(
            nav_frame, "Tracking Bot", lambda: self.show_frame(self.tracking_frame)
        )
        self.tracking_button.pack(pady=5, padx=15, fill=tk.X)

        self.settings_button = self.create_button(
            nav_frame, "Settings", lambda: self.show_frame(self.settings_frame)
        )
        self.settings_button.pack(pady=5, padx=15, fill=tk.X)

        self.about_button = self.create_button(
            nav_frame, "About", lambda: self.show_frame(self.about_frame)
        )
        self.about_button.pack(pady=5, padx=15, fill=tk.X)

        self.quit_button = self.create_button(
            nav_frame, "Quit", command=self.app.destroy
        )
        self.quit_button.pack(pady=5, padx=15, fill=tk.X)

        self.version_label = CTkLabel(nav_frame, text="Version: 1.0.0", font=("Arial", 12))
        self.version_label.pack(side=tk.BOTTOM, padx=5, anchor=tk.W)

        self.fps_label = CTkLabel(nav_frame, text="FPS:", font=("Arial", 12))
        self.fps_label.pack(side=tk.BOTTOM, padx=5, anchor=tk.W)

    def create_main_menu_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="Main Menu", font=("Arial", 16))
        label.pack(pady=20)
        return frame

    def create_fishing_frame(self):
        frame = CTkFrame(self.app)

        self.fishing_label = CTkLabel(frame, text="Fishing Bot", font=("Arial", 16))
        self.fishing_label.pack(pady=20)

        self.start_fishing_button = self.create_button(
            frame, "Start Fishing", self.start_fishing
        )
        self.start_fishing_button.pack(pady=5, padx=10)

        self.stop_fishing_button = self.create_button(
            frame, text="Stop Fishing", command=self.stop_fishing
        )
        self.stop_fishing_button.pack(pady=5, padx=10)

        self.running_label = CTkLabel(frame, text="Running", text_color="green")
        self.stopped_label = CTkLabel(frame, text="Stopped", text_color="red")
        self.stopped_label.pack(pady=5, fill=tk.X, padx=10)

        # Frame for zone and time display
        self.info_frame = CTkFrame(frame, fg_color="#202020")
        self.info_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        # Zone and time display labels
        self.zone_display_label = CTkLabel(self.info_frame, text="Current Zone: Unknown", font=("Arial", 12))
        self.zone_display_label.pack(side=tk.LEFT, padx=15, pady=0, fill=tk.X)

        self.time_display_label = CTkLabel(self.info_frame, text="Current Time: Unknown", font=("Arial", 12))
        self.time_display_label.pack(side=tk.RIGHT, padx=15, pady=0, fill=tk.X)

        return frame

    def create_grinding_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="Grinding Bot", font=("Arial", 16))
        label.pack(pady=20)
        # Add grinding-related widgets here
        return frame

    def create_healing_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="Healing Bot", font=("Arial", 16))
        label.pack(pady=20)
        # Add grinding-related widgets here
        return frame

    def create_tracking_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="Tracking Bot", font=("Arial", 16))
        label.pack(pady=20)
        # Add grinding-related widgets here
        return frame

    def create_settings_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="Settings", font=("Arial", 16))
        label.pack(pady=20)
        # Add grinding-related widgets here
        return frame

    def create_about_frame(self):
        frame = CTkFrame(self.app)
        label = CTkLabel(frame, text="About", font=("Arial", 16))
        label.pack(pady=20)
        # Add grinding-related widgets here
        return frame


    def create_button(self, parent, text, command):
        return CTkButton(
            parent, text=text,
            corner_radius=32,
            hover_color="#202020",
            command=command
        )

    def show_frame(self, frame):
        # Hide all frames
        self.main_menu_frame.pack_forget()
        self.fishing_frame.pack_forget()
        self.grinding_frame.pack_forget()
        self.healing_frame.pack_forget()
        self.tracking_frame.pack_forget()
        self.settings_frame.pack_forget()
        self.about_frame.pack_forget()

        # Show the selected frame
        frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


    def start_fishing(self):
        if self.main_agent.cur_img is None:
            messagebox.showerror("Error", "Screen capture not running!")
            return
        self.main_agent.start_fishing()
        self.update_status_labels(True)

    def stop_fishing(self):
        print("Stopping fishing")
        self.main_agent.stop_fishing()
        self.update_status_labels(False)

    def update_status_labels(self, is_running):
        # Hide both labels first
        self.running_label.pack_forget()
        self.stopped_label.pack_forget()

        # Show the appropriate label
        if is_running:
            self.running_label.pack(pady=5, fill=tk.X, padx=10)
        else:
            self.stopped_label.pack(pady=5, fill=tk.X, padx=10)

    def update_zone_display(self):
        # Update the label with the current zone
        if self.main_agent.zone:
            self.zone_display_label.configure(text=f"Current Zone: {self.main_agent.zone}")
        else:
            self.zone_display_label.configure(text="Current Zone: Unknown")

        if self.main_agent.cur_time:
            self.time_display_label.configure(text=f"Current Time: {self.main_agent.cur_time}")
        else:
            self.time_display_label.configure(text="Current Time: Unknown")

        if self.main_agent.fps:
            self.fps_label.configure(text=f"FPS: {self.main_agent.fps}")
        else:
            self.fps_label.configure(text="FPS:")

        # Schedule the next update
        self.app.after(1000, self.update_zone_display)  # Update every 1 second