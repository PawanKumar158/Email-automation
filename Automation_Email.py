import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
EMAIL_ADDRESS = "p1kuma******@gmail.com" # Send_email address 
EMAIL_PASSWORD = "#t#q s##c o##g in#u"  # Use app-specific password if using Gmail with 2FA
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Recipient email
RECIPIENT_EMAIL = "kumar332*****@gmail.com" # Receiver EMAIL_ADDRESS 

def send_email():
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Daily Report" # Subject of email 

        # Email body
        body = "This is your daily report. Hello how are you?"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
        server.quit()

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Execute the email sending function
send_email()
