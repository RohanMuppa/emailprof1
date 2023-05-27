import smtplib


class Email:
    def __init__(self, sender_email, sender_password, recipient_email, subject, body):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body
        self.email = None

    #def create_email(self):

    def send_email(self):
        message = f"Subject: {self.subject}\n\n{self.body}"
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.recipient_email, message)
