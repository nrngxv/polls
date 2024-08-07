# A very simple polls program
The aim of this program was to learn about how django works and understand how designing a frontend of a application works

## How it works
--- THIS PROGRAM RUNS COMPLETELY LOCALLY ---

First check if you are on the latest version of python or not. Run this in your terminal
```
python --version
```
It should say Python 3.11.4

Next, Clone this GitHub respository:
```
git clone https://github.com/nrngxv/polls.git
```

Next, cd into the directory where the git is cloned, and run this command
```
python manage.py runserver
```
This will start the server.

Next, go to this web address ```http://127.0.0.1:8000/``` and you will see the home page for the application

## Explaning the interface

**The home page**
The home page consist of a navigation bar. With links to the home page and a create page. 
The rest of the page, displays a list of already made polls, and each list of poll has two button with it.
- One is to vote on the Poll
- One is to view the result
- Questions displyed on each poll view

![polls home page gif](https://github.com/user-attachments/assets/22fd1ded-0ca6-4b9a-8ce0-c32aebd3fd1e)


**Create page**
This page give you access to creating a custom poll. 
- Enter a poll question
- Enter the different options to the poll
- The new poll gets updated on the home page.

![polls create](https://github.com/user-attachments/assets/e1fcfa95-53e7-4b80-8481-8acf97ff8a03)
