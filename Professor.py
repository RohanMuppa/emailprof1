class Professor:
    def __init__(self, email, area, interests, school, department):
        self.email = email
        self.area = area
        self.interests = interests
        self.school = school
        self.department = department
        self.lastName = self.get_last_name()

    def get_last_name(self):
        return self.email.split('@')[0]

    def get_email(self):
        return self.email

    def get_area(self):
        return self.area

    def get_interests(self):
        return self.interests

    def get_school(self):
        return self.school

    def get_department(self):
        return self.department
