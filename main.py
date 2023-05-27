import csv
import smtplib

from Email import Email
from Professor import Professor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def csv_parser(path):
    professors = {}
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row

        for row in csv_reader:
            eaddress = row[0]
            lastName = row[1]
            area = row[2]
            interests = row[3]
            school = row[4]
            department = row[5]

            professor = Professor(lastName, eaddress, area, interests, school, department)
            professors[lastName] = professor

    return professors

if __name__ == '__main__':
    path = 'example.csv'
    professors = csv_parser(path)

    # Credentials
    sender = os.environ['email']
    password = os.environ['password']

    for professor in professors.values():
        if professor.school == 'Alabama State University':
            # Open and edit the file
            file_path = 'templates/alabamastate/alabamastate.txt'  # Replace with the actual file path
            with open(file_path, 'r') as file:
                html_content = file.read()

            # Modify the HTML content as needed
            html_content = html_content.replace('[lastName]', professor.lastName)
            html_content = html_content.replace('[area]', professor.area)
            html_content = html_content.replace('[department]', professor.department)
            html_content = html_content.replace('[school]', professor.school)

            # Add experience if not blank, otherwise use regular template
            if professor.interests:
                html_content = html_content.replace('[experience]', professor.interests)
            else:
                html_content = html_content.replace('[experience]', '<regular experience template>')

            # Create a multipart message
            message = MIMEMultipart("alternative")

            # Create HTML part of the message
            html_part = MIMEText(html_content, "html")

            # Attach the HTML part to the message
            message.attach(html_part)

            # Set the sender, recipient, and subject
            message["From"] = sender
            message["To"] = professor.eaddress
            message["Subject"] = "Research Opportunity Inquiry"

            # Send the email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, professor.eaddress, message.as_string())