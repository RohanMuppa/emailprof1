import csv
import smtplib

from Email import Email
from Professor import Professor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def csv_parser(path):
    professors = []
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
            professors.append(professor)

    return professors

if __name__ == '__main__':
    path = 'example.csv'
    professors = csv_parser(path)
    email = Email()  # Assuming the Email class doesn't require a professor argument

    # Call the functions beforehand and store the results in the dictionary
    # this may take longer to iterate through every school and process the function beforehand, but code looks much simpler and the time is not that much greater
    school_emails = {
        'University of Bridgeport': email.send_email('TLS', 'smtp.gmail.com', 587, 'CV/CV.pdf',
                                                     'templates/alabamastate/alabamastate.txt'),
        'testing': email.send_email('TLS', 'smtp.gmail.com', 587, 'CV/CV.pdf',
                                    'templates/alabamastate/alabamastate.txt')
    }
    for professor in professors:
        email = Email(professor)

        if professor.school in school_emails:
            school_emails[professor.school]