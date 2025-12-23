from tkinter import *
import qrcode   # ✅ correction ici

root = Tk()
root.title("QR Code Generator")
root.geometry("1000x550")
root.configure(background="#AE2321")
root.resizable(False, False)

#icon image
img_icon = PhotoImage(file="icon.png")
root.iconphoto(False, img_icon)

def generer():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("QRCODE/" + str(name) + ".png")

    global Image
    Image = PhotoImage(file="QRCODE/" + str(name) + ".png")
    Image_view.config(image=Image)

Image_view = Label(root, bg = "#AE2321")
Image_view.pack(padx=50, pady=10, side = RIGHT)


Label(root, text="Title", fg="white", bg="#AE2321", font=20).place(x=50, y=170)
title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generer", width=20, height=2, bg="black", fg="white", command=generer).place(x=50, y=300)

root.mainloop()
