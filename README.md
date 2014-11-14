SFUCN
=====



This website is split into 4 pages

MAINPAGE
========
First page the website detects on whether the user has a logged in token,
if not the user is redirected to the login page.
If the user is logged in then an overview of the site is given.
User is able to see all the courses they are tracking and the current status of those courses.

LOGINPAGE
========
Simple form requesting the users Username/Email and the password that corresponds to it.
Signup button is located on the same page for if the user does not have an account

SIGNUPPAGE
========
Simple page with a form in the middle where the user inserts the following information in order to create an account:
- Email (Along with email validation checks)
- Username (longer than 6 characters, no special characters)
- Password (longer than 6 characters)
This will store the account information within our backend

ABOUTPAGE
========
Description of the project and who wrote the project and the purpose of the project

COURSESPAGE
========
List of all available courses is brought up, on course select the user is prompted for the course number and the section they want to watch.

Accounts
========
String Email
String Username
String Password
Course[] coursesWatching
