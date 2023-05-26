import csv

from Email import Email
from Professor import Professor


def __init__(self, email, area, interests, school, department):
    self.email = email
    self.area = area
    self.interests = interests
    self.school = school
    self.department = department

def csv_parser(path):
    professors = {}
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row

        for row in csv_reader:
            email = row[0]
            lastName = row[1]
            area = row[2]
            interests = row[3]
            school = row[4]
            department = row[5]

            professor = Professor(email, area, interests, school, department)
            professors[lastName] = professor

    return professors

if __name__ == '__main__':
    path = 'example.csv'
    professors = csv_parser(path)

    for lastName, professor in professors.items():
        print("Last Name:", lastName)
        print("Email:", professor.email)
        print("Area:", professor.area)
        print("Interests:", professor.interests)
        print("School:", professor.school)
        print("Department:", professor.department)
        print()

    sender = 'rishimaraseta@gmail.com'
    recipient = 'asd2as23c2@gmail.com'
    password = 'nejnvpujmuezqbmo'
    subject = 'Hello'
    body = 'This is a test email!'

    # Replace the placeholders with your own email and password
    email = Email(sender, password, recipient, subject, body)
    email.send_email()



