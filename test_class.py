from datetime import datetime


class Contact:
    def __init__(self, name, last_name, number, email, born_date):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.born_date = datetime.strptime(born_date, "%d/%m/%Y")

    def get_full_name(self):
        return self.name + " " + self.last_name

    def get_age(self):
        today = datetime.today()
        return today.year - self.born_date.year - \
               ((today.month, today.day) < (self.born_date.month, self.born_date.day))


contact = Contact(name="Nate", last_name="Gentile", number="5514781044", email="nate@nate.com", born_date="27/07/1990")

print(contact.name)
print(contact.number)
print(contact.get_full_name())
print(contact.get_age())