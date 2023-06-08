import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class Email:
    def __init__(self, professor):
        self.sender_email = os.environ['email']
        self.sender_password = os.environ['password']
        self.professor = professor

    def send_email(self, secType, smtp_server, smtp_port, file_path, pdf_file_path=None):
        with open(file_path, 'r') as file:
            html_content = file.read()

        # Modify the HTML content as needed
        html_content = html_content.replace('[lastName]', self.professor.lastName)
        html_content = html_content.replace('[area]', self.professor.area)
        html_content = html_content.replace("[department]", self.professor.department)
        html_content = html_content.replace('[school]', self.professor.school)

        # Add experience if not blank, otherwise use regular template
        if self.professor.get_interests() != '':
            html_content = html_content.replace('[experience]', self.professor.interests)
        else:
            html_content = html_content.replace('[experience]', "in this field is immense and would be invaluable to the project.")

        # Create a multipart message
        message = MIMEMultipart("alternative")

        # Create HTML part of the message
        html_part = MIMEText(html_content, "html")

        # Attach the HTML part to the message
        message.attach(html_part)

        # Set the sender, recipient, and subject
        message["From"] = self.sender_email
        message["To"] = self.professor.eaddress
        message["Subject"] = "High School Research Opportunity Inquiry"

        # Attach the PDF file
        if pdf_file_path != None:
            with open(pdf_file_path, "rb") as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), "pdf")
            pdf_attachment.add_header("Content-Disposition", "attachment", filename="attachment.pdf")
            message.attach(pdf_attachment)

        if secType == 'SSL':
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
        elif secType == 'TLS':
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)

    def set_subject(self, message):
        self.subject = message
    #def check_email_sent(self, professor, imap_server, sender_email):
        # Create an instance of the IMAP4_SSL class
        #mail = imaplib.IMAP4_SSL(imap_server)

        # Login to the email account
        #mail.login(sender_email, os.environ['password'])

        # Search for sent emails to the professor's email address
        #mailbox_name = "Sent"
        #search_criteria = f'(TO "{professor.eaddress}")'
        #result = mail.select(mailbox_name)
        #if result[0] == 'OK':
            #result = mail.search(None, search_criteria)
            #if result[0]:
                #print(f"Email already sent to {professor.eaddress}")
                #return True

        # Logout from the email account
        #mail.logout()

        #return False