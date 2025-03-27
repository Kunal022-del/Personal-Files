import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pyautogui
import os
# hello world

class BirthdayCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Card")
        self.root.geometry("850x900")
        self.root.configure(bg="#f8f9fa")  # Light background color

        # Header frame
        header_frame = tk.Frame(self.root, bg="chocolate", pady=10)
        header_frame.pack(fill=tk.X)

        # Back button with icon on the left side
        self.back_icon = tk.Button(
            header_frame,
            text="⬅️",
            bg="chocolate",
            fg="white",
            font=("Arial", 16),
            command=self.root.destroy,
        )
        self.back_icon.pack(side=tk.LEFT, padx=10, pady=6)  # Back button on the left

        # Title label
        title_label = tk.Label(
            header_frame,
            text="Happy Birthday!",
            bg="chocolate",
            fg="white",
            font=("Arial", 19, "bold"),
        )
        title_label.pack(side=tk.LEFT, expand=True)  # Title label after the back button

        # Content frame for the rest of the interface (adjusting size)
        content_frame = tk.Frame(
            self.root, bg="black", padx=20, pady=10
        )  # Reduced pady
        content_frame.pack(
            expand=False, fill=tk.BOTH
        )  # Use `expand=False` to make it smaller

        # Image frame
        self.image_frame = tk.Frame(self.root, bg="#ffffff", relief=tk.RIDGE, bd=5)
        self.image_frame.pack(pady=10)

        # Image paths
        self.images = []
        self.image_paths = [
            r"C:\Users\Gateway\Desktop\Kunal\A72_photos\20210626_153211.jpg",
            r"C:\Users\Gateway\Desktop\Kunal\A72_photos\20211126_212518.jpg",
            r"C:\Users\Gateway\Desktop\Kunal\A72_photos\20211126_213057.jpg",
            r"C:\Users\Gateway\Desktop\Kunal\A72_photos\20220611_222431.jpg",
        ]
        self.load_images()

        # Text frame
        self.text_frame = tk.Frame(self.root, bg="#FFFFFF", relief=tk.RIDGE, bd=5)
        self.text_frame.pack(pady=20)

        # Text box for the birthday message
        self.text_box = tk.Text(
            self.text_frame,
            wrap=tk.WORD,
            font=("Times New Roman", 14),
            height=4,
            width=60,
            fg="white",
            bg="black",
            padx=10,
            pady=10,
            bd=0,
        )
        self.text_box.grid(row=0, column=0)
        self.scrollbar = tk.Scrollbar(
            self.text_frame, orient=tk.VERTICAL, command=self.text_box.yview
        )
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_box.config(yscrollcommand=self.scrollbar.set)
        self.text_box.insert(
            tk.END,
            "Dear Papa,\n\n"
            "You are my guiding light and my biggest inspiration. "
            "Your love, wisdom, and kindness have shaped my world.\n"
            "Wishing you a day filled with joy and a year ahead full of happiness. "
            "Love you endlessly!\n"
            "I also remember those two days where I had taken money unknowingly so that I could feed my friends during exams, "
            "and the day when I used foul words on a social media app just for fun. I never intended to make you unhappy. "
            "Sorry Papa !.\n\n"
            "With love, always.",
        )
        self.text_box.config(state=tk.DISABLED)

        # Save button to capture a screenshot
        self.save_button = tk.Button(
            self.root,
            text="Save!",
            command=self.save_screenshot,
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#d9534f",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=10,
        )
        self.save_button.pack(pady=20)

    def load_images(self):
        try:
            for iteration, img_path in enumerate(self.image_paths):
                if os.path.exists(img_path):  # Ensure the image file exists
                    img = Image.open(img_path)
                    img = img.resize((340, 230))
                    photo = ImageTk.PhotoImage(img)
                    self.images.append(photo)
                    label = tk.Label(self.image_frame, image=photo, bg="#ffffff")
                    label.grid(
                        row=iteration // 2, column=iteration % 2, padx=10, pady=10
                    )
                else:
                    messagebox.showerror("Error", f"Image file not found: {img_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load images: {e}")

    def save_screenshot(self):
        try:
            timestamp = random.randint(1, 100)
            screenshot_path = os.path.join(os.getcwd(), f"screenshot_{timestamp}.jpg")
            screenshot = pyautogui.screenshot()  # Take a screenshot
            screenshot.save(screenshot_path)
            messagebox.showinfo("Success", f"Screenshot saved as {screenshot_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to take screenshot: {e}")


if __name__ == "main":
    root = tk.Tk()
    BirthdayCardApp(root)
    root.mainloop()
