import threading
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x500")
file = 'newfile.gif'
info = Image.open(file)
frames = info.n_frames

# Use ImageTk.PhotoImage instead of tk.PhotoImage to avoid color inversion
im = []
for i in range(frames):
    img = Image.open(file)
    img.seek(i)
    img_rgba = img.convert("RGBA")
    photo = ImageTk.PhotoImage(img_rgba)
    im.append(photo)

# Create a label with the first frame
gif_label = tk.Label(root, image=im[0])
gif_label.pack()

def animation(count):
    if count == frames:
        count = 0
    # Update the label with the next frame
    gif_label.configure(image=im[count])
    count += 1
    # Decrease the delay to increase the speed by 2%
    root.after(int(50*0.98), lambda: animation(count))

# Start the animation
animation(0)

root.mainloop()
