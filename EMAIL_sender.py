import smtplib
from tkinter import *


def send_message(addres=None, email_body=None, address_entry=None):
    address_info = addres.get()
    email_body_info = email_body.get()
    print(address_info, email_body_info)
    sender_email = "Enter your email"
    sender_password = "Enter you password"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Login successful")
    server.sendmail(sender_email, address_info, email_body_info)
    print("Message sent")
    address_entry.delete(0, END)
    email_body.delete(0, END)

    app = Tk()
    app.geometry("800x800")
    app.title("Python Mail Send App")
    heading = Label(text="Python Email Sending App", bg="yellow", fg="black", font="arial", width="500", height="3")

    heading.pack()
    address_field = Label(text="Recipient Address: ")
    email_body_field = Label(text="Message : ")
    address_field.place(x=15, y=70)
    email_body_field.place(x=15, y=140)
    address = StringVar()
    email_body_field = StringVar()
    address_entry = Entry(textvariable=address, width=30)
    email_body_enrty = Entry(textvariable=email_body, width=30)
    address_entry.place(x=15, y=100)
    email_body_enrty.place(x=15, y=180)
    button = Button(app, text="Send Message", command=send_message, width=30, height=2, bg="grey")
    button.place(x=15, y=220)

    app.mainloop()
