from datetime import date, datetime

class Human:

    def __init__(self, first_name, last_name, date_of_birth = None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        born_date = datetime.strptime(self.date_of_birth, "%d/%M/%Y")
        return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))

