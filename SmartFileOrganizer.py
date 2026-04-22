import tkinter as tk
import os
import shutil
from datetime import datetime

#  path 
source = "C:/Users/YourName/Downloads"

# ---------------- ORGANIZE FUNCTION ----------------
def organize_files():
    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            # 📅 Date (Year-Month)
            modified_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(modified_time).strftime("%Y-%m")

            # 📂 File type category
            if ext in [".jpg", ".jpeg", ".png", ".gif"]:
                category = "Images"
            elif ext in [".mp4", ".mkv", ".avi"]:
                category = "Videos"
            elif ext in [".pdf", ".docx", ".txt"]:
                category = "Documents"
            elif ext in [".mp3", ".wav"]:
                category = "Music"
            else:
                category = "Others"

            # 📁 Final path (Type + Date)
            final_path = os.path.join(source, category, date_folder)

            if not os.path.exists(final_path):
                os.makedirs(final_path)

            shutil.move(file_path, os.path.join(final_path, file))

    status_label.config(text="✅ Files Organized by Type & Date!")

# ---------------- UNORGANIZE FUNCTION ----------------
def unorganize_files():
    for root_dir, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root_dir, file)

            if root_dir != source:
                try:
                    shutil.move(file_path, os.path.join(source, file))
                except:
                    pass

    status_label.config(text="🔁 Files Restored to Downloads!")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("400x350")

title = tk.Label(root, text="Smart File Organizer", font=("Arial", 16, "bold"))
title.pack(pady=20)

organize_btn = tk.Button(root, text="📂 Organize Files", bg="yellow", command=organize_files)
organize_btn.pack(pady=10)

unorganize_btn = tk.Button(root, text="🔁 Unorganize Files", bg="lightblue", command=unorganize_files)
unorganize_btn.pack(pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=20)

root.mainloop()
