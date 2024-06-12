import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

# Function to handle the video download
def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    # Display progress and status labels
    progress_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))
    status_label.pack(pady=(10, 5))

    try:
        # Create a YouTube object with a progress callback
        you_t = YouTube(url, on_progress_callback=on_progress)

        # Get the video stream with the desired resolution
        stream = you_t.streams.filter(res=resolution).first()

        # Download the video into a specific directory
        os.path.join("downloads", f"{you_t.title}.mp4") 
        stream.download(output_path="downloads")

        # Update status label on successful download
        status_label.configure(text="Downloaded", text_color="white", fg_color="green")

    except Exception as e:
        # Update status label on error
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")

# Callback function to update the progress bar
def on_progress(stream, chunk, bytes_remaining):
    tot_size = stream.filesize
    bytes_downloaded = tot_size - bytes_remaining
    percentage_completed = bytes_downloaded / tot_size * 100
    
    # Update progress label and progress bar
    progress_label.configure(text= str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))

# create a root window/the main application window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Title of the window and size
root.title("YouTube Load!")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1000, 720)

# Create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Create & place URL entry components
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

# Create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))

# Create and place resolution selection components
resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(pady=(10, 5))
resolution_combobox.set("720p")

# Create and place progress and status labels
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0 )

status_label = ctk.CTkLabel(content_frame, text="")

# Start the application
root.mainloop()