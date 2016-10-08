# User_Login_System
A simple user login and registration system in Python.

## Screenshots
#### Register
![Alt text](screenshots/register.png?raw=true "Register")
#### Login
![Alt text](screenshots/login.png?raw=true "Login")
#### Login Success
![Alt text](screenshots/login_success.png?raw=true "Login Success")

### Registration
* Check if the user already exists by checking for the user entry (username) in the DB.
* If user already exists show error message.
* Else create a new User entry in the DB with username, encrypted password and email.

### Login
* Check if the user exists.
* If user exists then validate the username and password with the entry in DB.
* Add user to the *session* and redirect to index page.
* If user doesn't exist of password is incorrect show error message.

### Logout
* Pop user key from the *session*.

### Index Page
* If user is logged in (ie., if user key is in session) then show Index page.
* Else redirect to login page.

### Encryption
* sha256 algorithm (from python hashlib library) is used for encrypting passwords.

### Backend
* Web framework: flask
* Database: MySql
