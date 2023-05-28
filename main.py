import csv

from Email import Email
from Professor import Professor

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

    #schools = ['University of Bridgeport', email.send_emailTLS()]
    for professor in professors:
        email = Email(professor)
        #maybe email = Email(professor), the rest of the inputs will be specific to the class
        if professor.school == 'University of Bridgeport':
            email.send_email('TLS','smtp.gmail.com',587,'CV/CV.pdf',
                             'templates/alabamastate/alabamastate.txt')

        elif professor.school == 'testing':
            email.send_email('SSL', 'smtp.gmail.com', 465, 'CV/CV.pdf',
            'templates/alabamastate/alabamastate.txt')