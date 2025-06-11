class User:
    def __init__(self, fName, lName, phoneNum, email):
        self.first_name = fName
        self.last_name = lName
        self.phone = phoneNum
        self.email = email

    def description(self):
        return f"User is {self.first_name} {self.last_name}\n Phone Number: {self.phone}\n email: {self.email}"

aindi = User('Aindi', 'Tsarni', '123456789', 'at@gmail.com')

print(aindi.description())