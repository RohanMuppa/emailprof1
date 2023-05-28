import csv

from Email import Email
from Professor import Professor

def csv_parser(path):
    professors = []
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row

        for row in csv_reader:
            professor = Professor(row[0], row[1], row[2], row[3], row[4], row[5])
            professors.append(professor)

    return professors


if __name__ == '__main__':
    path = 'CSV/emailprof.csv'
    professors = csv_parser(path)

    #schools = ['University of Bridgeport', email.send_emailTLS()]
    for professor in professors:
        email = Email(professor)
        #maybe email = Email(professor), the rest of the inputs will be specific to the class
        #if professor.isPhd == 1:

        if professor.school == 'University of Bridgeport':
            email.send_email('TLS','smtp.gmail.com',587,
                             'templates/ubridgeport/bridgeportTemplate')

        elif professor.school == 'Alabama State University':
            email.send_email('SSL', 'smtp.gmail.com', 465,
                             'templates/generalEmail')

        #if professor.school == "Startup":

        elif professor.school == 'testing':
            email.send_email('SSL', 'smtp.gmail.com', 465,
            'templates/generalEmail')