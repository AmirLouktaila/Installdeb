import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import sys
import os

def get_terminal_command():
    desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
    
    if "gnome" in desktop_env:
        return "gnome-terminal"
    elif "kde" in desktop_env:
        return "konsole"
    elif "xfce" in desktop_env:
        return "xfce4-terminal"
    elif "lxde" in desktop_env or "lxqt" in desktop_env:
        return "lxterminal"
    elif "mate" in desktop_env:
        return "mate-terminal"
    elif "deepin" in desktop_env:
        return "deepin-terminal"
    elif "enlightenment" in desktop_env:
        return "terminology"
    else:
        raise Exception("Unsupported desktop environment")

def install_deb_file(file_path):
    root = tk.Tk()
    root.withdraw()  

    result = messagebox.askokcancel("Install deb file", f"Do you want to install the file: {file_path}?")

    if result:
        try:
            terminal_cmd = get_terminal_command()
            terminal_cmd += f" -- /bin/bash -c '"
            terminal_cmd += f"echo Input Password; "
            terminal_cmd += f"sudo bash -c \"echo Wait...; dpkg -i {file_path} > /dev/null 2>&1; echo Installation complete :{file_path}\"; "
            terminal_cmd += f"read -p \"Press Enter to close terminal\"'"

            subprocess.Popen(terminal_cmd, shell=True)


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    else:
        print("Cancel clicked")

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        deb_file = sys.argv[1]
        install_deb_file(deb_file)
    else:
        print("Please pass the path of the deb file as an argument.")
