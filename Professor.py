class Professor:
    def __init__(self, eaddress, lastName, area, interests, school, department):
        self.eaddress = eaddress
        self.area = area
        self.interests = interests
        self.school = school
        self.department = department
        self.lastName = lastName
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
