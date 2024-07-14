import tkinter as tk
from tkinter import filedialog

class CreatEmailWindow:
    def __init__(self, master, filename):
        self.master = master
        master.title("Create Email")
        
        self.filename = filename

        self.label = tk.Label(master, text="Create Email")
        self.label.pack()

        self.sender_label = tk.Label(master, text="Sender Email:")
        self.sender_label.pack()
        self.sender_entry = tk.Entry(master)
        self.sender_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.receiver_label = tk.Label(master, text="Receiver Email:")
        self.receiver_label.pack()
        self.receiver_entry = tk.Entry(master)
        self.receiver_entry.pack()

        self.subject_label = tk.Label(master, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(master)
        self.subject_entry.pack()

        self.body_label = tk.Label(master, text="Body:")
        self.body_label.pack()
        self.body_text = tk.Text(master, height=10)
        self.body_text.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_email)
        self.send_button.pack()

    def send_email(self):
        sender_email = self.sender_entry.get()
        sender_password = self.password_entry.get()
        receiver_email = self.receiver_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END)
        send_email(sender_email, sender_password, receiver_email, subject, body, self.filename)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CreatEmailWindow(root)
    root.mainloop()
