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

        if professor.school == 'MIT':
            email.send_email('SSL', 'outgoing.mit.edu', 465,
                             'templates/generalEmail')

        elif professor.school == 'University of Bridgeport':
            email.send_email('TLS','smtp.gmail.com',587,
                             'templates/ubridgeport/bridgeportTemplate')

        elif professor.school == 'University of Minnesota':
            #if professor.lastName == 'Milewski':
                #email.set_subject("High School Hydrological Remote Sensing Research Inquiry")
            email.send_email('TLS', 'smtp.gmail.com', 587,
                             'templates/generalEmail')

        elif professor.school == 'Georgia Tech':
            email.send_email('TLS', 'smtp.office365.com', 587,
                            'templates/generalEmail')

        elif professor.school == 'University of Alaska':
            email.send_email('TLS', 'smtp.gmail.com', 587, 'templates/universityofalaska/ualaska')

        elif professor.school == 'Lund University':
            email.send_email('SSL', 'smtp.gmail.com', 465,
                             'templates/lunduni')

        else:
            email.send_email('SSL', 'smtp.gmail.com', 465,
                             'templates/generalEmail')

        #if professor.school == "Startup":

        if professor.school == 'testing':
            email.send_email('SSL', 'smtp.gmail.com', 465,
            'templates/generalEmail')