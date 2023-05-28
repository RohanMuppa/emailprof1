import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Credentials
sender = os.environ['email']
password = os.environ['password']

class Email:
    def __init__(self, professor):
        self.recipient_email = professor.eaddress
        self.sender = os.environ['email']
        self.password = os.environ['password']
        self.professor = professor
    #def create_email(self):

    def send_email(self, secType, smtp_server, smtp_port, CV_file_path, file_path):
        with open(file_path, 'r') as file:
            html_content = file.read()

        # Modify the HTML content as needed
        html_content = html_content.replace('[lastName]', self.professor.lastName)
        html_content = html_content.replace('[area]', self.professor.area)
        html_content = html_content.replace("[department]", self.professor.department)
        html_content = html_content.replace('[school]', self.professor.school)

        # Add experience if not blank, otherwise use regular template
        if self.professor.get_interests() == '':
            html_content = html_content.replace('[experience]', self.professor.interests)
        else:
            html_content = html_content.replace('[experience]', "this field is immense and invaluable")

        # Create a multipart message
        message = MIMEMultipart("alternative")

        # Create HTML part of the message
        html_part = MIMEText(html_content, "html")

        # Attach the HTML part to the message
        message.attach(html_part)

        # Attach the PDF file
        with open(CV_file_path, "rb") as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), "pdf")
        pdf_attachment.add_header("Content-Disposition", "attachment", filename="attachment.pdf")
        message.attach(pdf_attachment)

        # Set the sender, recipient, and subject
        message["From"] = sender
        message["To"] = self.professor.eaddress
        message["Subject"] = "Research Opportunity Inquiry"

        if secType == 'SSL':
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipient_email, message.as_string())

        elif secType ==  'TLS':
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(message)