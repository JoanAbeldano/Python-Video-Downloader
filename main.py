from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os
import winsound
import threading

def download(link):
    def download_video():
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        yd.download(path_to_download_folder)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        button.config(state=tk.NORMAL)

    button.config(state=tk.DISABLED)
    threading.Thread(target=download_video).start()

window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("500x300")

label1 = ttk.Label(window, text="Video Link")
label1.pack()
entry1 = ttk.Entry(window)
entry1.pack()
button = ttk.Button(window, text="Download", command=lambda:[download(entry1.get())])
button.pack()

window.mainloop()
