from appUsers import User

def test_user():
    aindi = User('Aindi', 'Tsarni', '123456789', 'at@gmail.com')
    assert aindi.description() == "User is Aindi Tsarni\n Phone Number: 123456789\n email: at@gmail.com"
