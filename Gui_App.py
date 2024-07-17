import tkinter as tk
from tkinter import filedialog

def create_email_ui():
    window = tk.Tk()
    window.title('Email Automation')

    def send_email_action():
        to_address = to_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END)
        attachment_path = filedialog.askopenfilename()
        send_email(to_address, subject, body, attachment_path)

    def view_emails_action():
        emails = read_emails()
        email_listbox.delete(0, tk.END)
        for email in emails:
            email_listbox.insert(tk.END, f"From: {email['from']}, Subject: {email['subject']}")

    tk.Label(window, text='To:').grid(row=0)
    to_entry = tk.Entry(window)
    to_entry.grid(row=0, column=1)

    tk.Label(window, text='Subject:').grid(row=1)
    subject_entry = tk.Entry(window)
    subject_entry.grid(row=1, column=1)

    tk.Label(window, text='Body:').grid(row=2)
    body_text = tk.Text(window, height=10, width=30)
    body_text.grid(row=2, column=1)

    tk.Button(window, text='Send Email', command=send_email_action).grid(row=3, column=1)

    tk.Button(window, text='View Emails', command=view_emails_action).grid(row=4, column=0)
    email_listbox = tk.Listbox(window, height=10, width=50)
    email_listbox.grid(row=5, column=0, columnspan=2)

    window.mainloop()

# Run the UI
create_email_ui()
