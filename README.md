# Contact-App-Project

For my third milestone project, I have decided to create a contact app for users so that they get to keep their information 
about his or her contact. The application is created to ensure that users are able to create, edit, update and delete their 
contacts. This is to address the information Architecture for processing, storing, retrieving and updating data.
 
# UX

## UX Design
The main color scheme for the project was mainly green and white background. It also consists of
black text so that the users can easily see their contacts. Also the navigation is placed orderly
to provide user experience better.

## User Stories

### Users
- As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
- As a first time user, I want to navigate easily in order to find the content and be able to see my contacts.
- As a user, i want to add my contact.
- As a user, i want to edit or delete my contact.

### Owner
- As a owner, I want my users to be able to have access to their contacts
- As a owner, I would like my users to navigate easily.
- As a owner, I would like to ensure users that they are able to keep their contacts.

## Target Audience


## Wireframe
I used Balsamiq to create the Wireframe for the project. This Wireframe contains
the schematics for the ideal project:

[Link to the Final Version of the Wireframe]()

## Data schema


[Database Schema](/workspace/contact-app-project/database-designs/database-model-design.png)


# Features

## Existing Features

### Structure


### Forms
- Register form: This provides interface to new users for sign up.

- Log In form: form that enable users to sign into already created account.



### Home


### Profile
- The Profile section features exclusively for a user session. 
  All collections per user are stored in their respective profile Page and secure to only be available to the owner.

### Add New Contact
- This section will have the form where the user will put theur contacts full name, telephone and email.

### Security
- To make the user authentication more secure, the Log In form integrates werkzeug security features namely:
"generate_password_hash" and "check_password_hash". it is difficult to crack the passwords.

## Features Left to Implement


# Technologies Used

## Languages
- [HTML](https://html.com/)
- [CSS](https://www.w3schools.com/css/)
- [Javascript](https://www.w3schools.com/js/DEFAULT.asp)
- [Python](https://www.python.org/)
- [django]

## Tools and Libraries
- [Materialize](https://materializecss.com/)
    - It was used to create grid layout and styling various features such as navbar accordion, cards, buttons and
    form to render responsive website.
- [PEP8 Python Validator](http://pep8online.com/)
    - To validate the python code
- [JQuery](https://jquery.com)
    - It was used to simplify JavaScript.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - This is a web application framework used to create functions with Python that are injected into html templates.
- [Git](https://git-scm.com/)
    - It was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Jshint](https://jshint.com/)
    - To validate my JavaScript code.
- [HTML Validator](https://validator.w3.org/)
    - To validate my HTML code.
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
    - To validate my CSS code.
- [drawio](https://app.diagrams.net/)
    - Used to create the database schema and data manipulation operations diagrams.
- [dbdiagramio](https://dbdiagram.io/home)
    - Used to create the database schema diagram online.
- [font awesome](https://fontawesome.com/)
    - It  was used to create grid layout and styling various features such as navbar accordion, 
      cards, buttons, forms, and footer to render responsive website.

# External Hosting
- [Heroku](http://heroku.com/)
    - It was used to deploy, manage, and scale the app.
- [GitHub](https://github.com/)
    - The project used the GitHub hosting service to save the project in a repository.

# Testing

I used Chrome DevTools lighthouse to test the app to see how is it functioning well.

[Screenshot of lighthous testing](/workspace/contact-app-project/images/ligthouse-devtools-screenshot.png)

# Testing User Stories from User Experience (UX) Section

### Users:
1. As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
  - The user will see the Register form for first time user to sign up.
  - Also the user will be able to log in at the Log in form if their account is already created.
  - The user can log out at the Log Out form if they want to leave their account.
  - For security measures, the form will have the werkzeug security features such as 
    "generate_password_hash" and "check_password_hash". These hashing passwords will be good to keep their 
    information secured.

2. As a first time user, I want to navigate easily in order to find the content and be able to see my contacts.
    - At the top of each page there is a clean navigation bar, each link describes at what section 
    they will end up at clearly.
    - The user will be able to see their contacts with the collaspible. It behaves as expected and each
    collaspible-header has the name and the details of the contact including which user created by.

3. As a user, i want to add my contact.
    - The users can make use of the Add Contact form by clicking Add Contact tab in the navbar menu.

4. As a user, i want to edit or delete my contact.
    - Each relevant section provides Edit/Delete buttons which allow users to revise or delete contacts that they added.

### Owner:
1. As a owner, I want my users to be accessible to their contacts
    - The composition of the app is clear and simple. Already at the home page, the users will be able
    to see their contacts easily including the information that they created

2. As a owner, I would like to ensure users that they are able to keep their contacts.
    - There is enough security for the users to keep their contacts safe. In the future, i hope
    to make more tough security on the contacts where the collaspible is accessed to each user.

## Bugs

### Fixed
- I have fixed the link between the contact.py and the base.html with '{{ url_for(edit_contacts)}}'
- I have fixed the contacts.html because i was having trouble with the wrapping of the contacts.

### Unfixed
- The validation for the forms because i failed to have the validation function when the user clicks 
if the form is not complete or incorrect.

### Further Testing
- All the links were tested. They are all work perfectly.
- I have tested my app with Google Chrome, Microsoft Edge and Safari.
- All Codes passed through their respective Validators to erase syntax error.
- The button links works as expected.
- To prevent arbitrary code from running and security flaw, after the development stage, 
  I specify the debug=False before submission.
- I have tested my with my IPhone and IPad.

# Deployment

## Github
The app was developed on GitPod, using git and GitHub to host the repository 
as it cannot host a Python project on GitHub Page which only allows for static websites. 
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

Note: It's important to contain our environment variables within a hidden env.py file 
which should never be pushed to GitHub by ensuring .gitignore has it secured.

# Heroku
Here are the following steps to take when to deploy using Heroku:

1. Create Heroku App
- Go to Heroku website
- Go to sign up and create your own account.
- Select Python as your primary language.
- Fill in your unique name and select your corresponding region.
- Click Create App.

2. Add requirements.txt file

- Type "pip3 freeze --local > requirements.txt"
- After that, I type "git add -A"
- Then type git commit -m "Add requirements.txt file" 
- Finally, type git push.

3. Add Procfile
- Type echo web: python contact.py > Procfile
- Then type git add -A
- Then type git commit -m "Add Procfile"
- Finally git push

4. Creating default environment variables
- Click Settings on Heroku dashboard
- Click on Reveal Config Vars.
- Add the key of "IP" and the value of "0.0.0.0", and click on Add.
- Add the key of "PORT" and the value of "5000", then click Add.
- Add the key of "SECRET_KEY" and the value of "your secret key string here", then click Add.
- Add the key of "MONGO_URI" and the value of "mongo URI string here"
- Finally, add the key of "MONGO_DBNAME" and the value of "the name of your database here".

5. Setting-up Automatic Deployment from GitHub
- Click Deploy on the dashboard.
- Click Connect to GitHub.
- Ensure that my GitHub profile is displayed, then add my repository name (same as my Heroku App), 
  and then click search.
- Click connect once it finds the repository.
- Then safely click Enable Automatic Deployment.
- Select Branch and then click Deploy Branch.
- The message will say "Your App was successfully deployed"
- Click View to launch app.

## Credits

### Code 
- The code came from the Code Institute mini project which inspired me to do something
different. I made some modifications to definitely fit my needs.

### Acknowledgements

- I would like to thank Aaron for helping and supporting me with this project.
- I would like to thank the Tutor Support for their maximum effort to assist me.