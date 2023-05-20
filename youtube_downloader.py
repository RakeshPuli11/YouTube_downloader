import tkinter
from tkinter import messagebox
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("550x200")
root.title("Youtube downloader")


def startdownload():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        high_resolution_vedio = yt_object.streams.get_highest_resolution()
        high_resolution_vedio.download()
        messagebox.showinfo("Task update", "Downloaded successfully")

    except:
        messagebox.showinfo("Task Error", "invalid you tube link")


title_label = customtkinter.CTkLabel(root, text="insert a youtube link")
title_label.pack(padx=10, pady=10)


# link input
url_var = tkinter.StringVar()


link = customtkinter.CTkEntry(
    root, width=450, height=30, placeholder_text="link plz...", textvariable=url_var)
link.pack()

# download

download = customtkinter.CTkButton(
    root, text="Download", command=startdownload)
download.pack(padx=10, pady=(30,10))
root.mainloop()
