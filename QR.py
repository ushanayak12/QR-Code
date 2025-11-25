import qrcode
from tkinter import *
from tkinter import messagebox

def generate_qr(data, filename = "UshaQR.png"):
    img= qrcode.make(data)
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

if __name__ == "__main__":
    data_input = input("enter text or URL for QR code:")
    generate_qr(data_input)

data = input("Enter text/URL: hello usha")
filename = input("Enter the file name: Hello_usha_qr.png ")

QR = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)
QR.add_data(data)
QR.make(fit=True)
img = QR.make_image(fill_color = "black", back_color = "white")
img.save(filename)

print("QR Code Created Sucessfully !")


def generate():
    data = entry.get()
    if not data.strip():
        messagebox.showerror("error", "enter the data first")
        return
    img = qrcode.make(data)
    img.save("qr_gui.png")
    messagebox.showinfo("sucess", "QR saved as qr_gui.png")

root = Tk()
root.title("QR Code Generator")

Label(root, text = "Enter text or URL:").pack()
entry = Entry(root, width = 10)
entry.pack(pady = 10)

Button(root, text = "Generate QR", command=generate).pack(pady=5)
root.mainloop()