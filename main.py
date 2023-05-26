import csv
from Email import Email
from Professor import Professor

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
    path = 'prof.csv'
    professors = csv_parser(path)

    sender = 'rishimaraseta@gmail.com'
    password = 'nejnvpujmuezqbmo'

    for professor in professors.values():
        recipient = professor.get_eaddress()
        subject = 'Research Opportunity Inquiry'
        body = """
        Dear Professor [Last Name],

        I hope this email finds you well. My name is [Your Name], and I am currently a [year/level] student majoring in [your major] at [your university]. I am reaching out to you because of my keen interest in conducting research in the field of [specific research area or topic].

        After reviewing your impressive research profile and publications, I am particularly intrigued by your work in [mention specific projects or areas of research]. The innovative approaches and insights you have contributed to the field have inspired me to explore further and actively participate in research endeavors.

        I have gained substantial knowledge and skills through my coursework in [relevant courses], as well as my involvement in [mention any relevant extracurricular activities or research projects]. These experiences have equipped me with a solid foundation in [specific research techniques or methodologies] and have fostered my passion for contributing to scientific advancements.

        I am particularly interested in exploring research opportunities within your research group or lab. Your expertise aligns closely with my research interests, which primarily revolve around [describe your specific research interests or questions]. I believe that working under your guidance would provide invaluable insights and opportunities for growth in my academic and professional journey.

        I would greatly appreciate the opportunity to discuss potential research projects or any available positions in your lab. I am open to assisting with ongoing projects, conducting independent research, or collaborating on new initiatives within the realm of [specific research area]. I am also open to any suggestions or guidance you may have regarding potential research avenues.

        Please find attached my resume and a brief overview of my research experience for your reference. I would be more than happy to provide any additional information or documents upon your request.

        Thank you for considering my inquiry. I am genuinely enthusiastic about the possibility of joining your research team and contributing to the advancement of knowledge in [research area]. I look forward to the possibility of discussing this further at your convenience.

        Best regards,

        [Your Name]"""

        professor.set_email(sender, recipient, password, subject, body)
        professor.email.send_email()
