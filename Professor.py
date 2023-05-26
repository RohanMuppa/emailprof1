from Email import Email


class Professor:
    def __init__(self, lastName, address, area, interests, school, department):
        self.eaddress = address
        self.area = area
        self.interests = interests
        self.school = school
        self.department = department
        self.lastName = lastName

    def set_email(self, sender, recipient, password, subject, body):
        # Replace the placeholders with your own email and password
        self.email = Email(sender, password, recipient, subject, body)

    def get_email(self):
        return self.email

    def get_eaddress(self):
        return self.eaddress

    def get_area(self):
        return self.area

    def get_interests(self):
        return self.interests

    def get_school(self):
        return self.school

    def get_department(self):
        return self.department
