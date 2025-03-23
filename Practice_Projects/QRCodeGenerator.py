import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    source_code = text_input.get("1.0", tk.END).strip()

    if not source_code:
        messagebox.showwarning("Input Error", "Please enter some text to generate the QR code!")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(source_code)
        qr.make(fit=True)

        if qr.version > 40:
            messagebox.showwarning("Input Too Large", "The input data is too large to fit into a single QR code. Please reduce the size.")
            return

        global qr_image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image = qr_image.resize((300, 300), Image.Resampling.LANCZOS)
        qr_image_tk = ImageTk.PhotoImage(qr_image)

        qr_label.config(image=qr_image_tk)
        qr_label.image = qr_image_tk

        save_button.config(state=tk.NORMAL)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr():
    if qr_image:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            try:
                qr_image.save(file_path)
                messagebox.showinfo("Success", f"QR code saved successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {e}")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("600x600")

style = ttk.Style()
style.theme_use("clam")

input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X)

input_label = ttk.Label(input_frame, text="Enter Source Code:", font=("Helvetica", 12))
input_label.pack(anchor=tk.W)

text_input = tk.Text(input_frame, height=10, font=("Helvetica", 10))
text_input.pack(fill=tk.X, pady=5)

button_frame = ttk.Frame(input_frame)
button_frame.pack(fill=tk.X, pady=10)

generate_button = ttk.Button(button_frame, text="Generate QR Code", command=generate_qr)
generate_button.pack(side=tk.LEFT, padx=5)

save_button = ttk.Button(button_frame, text="Save QR Code", command=save_qr, state=tk.DISABLED)
save_button.pack(side=tk.LEFT, padx=5)

qr_frame = ttk.Frame(root)
qr_frame.pack(fill=tk.BOTH, expand=True)

qr_label = ttk.Label(qr_frame)
qr_label.pack(pady=20)

root.mainloop()