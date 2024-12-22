import tkinter as tk
from tkinter import messagebox
import pyqrcode
from PIL import Image, ImageTk
import io

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data for the QR code!")
        return
    
    # Generate the QR code using pyqrcode
    qr = pyqrcode.create(data)
    
    # Create an image from the QR code
    buffer = io.BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)
    
    # Open the image from the buffer and convert it to a format compatible with Tkinter
    img = Image.open(buffer)
    img_tk = ImageTk.PhotoImage(img)
    
    # Update the label with the new QR code image
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep a reference to prevent garbage collection

root = tk.Tk()
root.title("QR Code Generator")
root.geometry('400x400')

# Label for input text
entry_label = tk.Label(root, text="Enter text or URL for QR Code:")
entry_label.pack(pady=10)

# Entry widget for text input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
