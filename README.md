# Flash E-Commerce

Flash is an ecommerce website that allows customers to buy the best quality of cameras that they can get. It is an
upcoming business that will benefit customers to buy the camera they need in their everydat lives.
 
# UX

## UX Design
The main color scheme for the project was mainly white and a nice background. It also consists of
black text so that the users can easily see their contacts. Also the navigation is placed orderly
to provide user experience better.

## User Stories

### Users
- As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
- As a first time user, I want to navigate easily in order to find the content and be able to see my contacts.
- As a user, i want to buy my product.
- As a user, i want to edit or delete my product.

### Owner
- As a owner, I want my users to be able to have access to their contacts
- As a owner, I would like my users to navigate easily.
- As a owner, I would like to ensure users that they are able to keep their contacts.

## Target Audience


## Wireframe
I used Balsamiq to create the Wireframe for the project. This Wireframe contains
the schematics for the ideal project:

[Final Version of the Wireframe](/workspace/flash-ecommerce/wireframe/wireframe.pdf)

## Data schema


[Database Schema](/workspace/flash-ecommerce/image/data_schema.png)

# Features

## Existing Features

### Structure

### Forms
- Register form: This provides interface to new users for sign up.

- Log In form: form that enable users to sign into already created account.

# Home Page
- The home page offers five nav bars to take users to relevant sections. It contains full-width appealing Hero Image Heading Caption with a call-to-action button which take users straight to product listing.

# User Account
- This provides interface for new users to register and sign into already created account. 
- The creation of the account requires a valid email and a password. Account owners can access the following features:
    - Update profile information
    - View order history
    - Review purchased product

# Shopping Bag
- The shopping bag populates all purchased product details, subtotal for items purchased and a grand total.
- Users can remove items from the shopping bag and update quantities before checkout.
- Thereafter users have the option to continue shopping or proceed to payment.

# Search bar
- The Search functionality is present on all pages to enable users narrow down their search.
# Product Listing
- The product listing is structured to offer users multiple search criteria and quicker access to specific products.
- Product listing can be sorted by Category, Name, Price, and Rating.
- This can be done either in ascending or descending order.

# Product View
- The product view populates the product details such as:
- Product name
- Category
- Image
- Price
- Rating
- Size adjustment
- Quantity increment/decrement functionality
- Add to bag and Keep Shopping buttons

# Checkout
- Checkout allow users to enter their delivery and payment details initially.
- The checkout details and delivery information are pre-filled with the information provided in the user's profile which can also be edited.
- A summary of the order is populated on the checkout page
- Users also have the option to adjust their bag before completion of order
- Payment is made by card using Stripe

# Administrator features
- The administrator has the sole right to product management section
- An administrator can edit or delete a product to get users updated and engaged.

# Features Left to implement
- Add s3 to django.
- Add AWS to django.
- More media
- Add another custom model


# Technologies Used

## Languages
- [HTML](https://html.com/)
- [CSS](https://www.w3schools.com/css/)
- [Javascript](https://www.w3schools.com/js/DEFAULT.asp)
- [Python](https://www.python.org/)
- [django](https://www.djangoproject.com/)

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

[Screenshot of lighthous testing]()

# Testing User Stories from User Experience (UX) Section

### Users:
1. As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
  - The user will see the Register form for first time user to sign up.
  - Also the user will be able to log in at the Log in form if their account is already created.
  - The user can log out at the Log Out form if they want to leave their account.

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

- I would like to thank Aaron for helping and supporting me with this final project.
- I would like to thank the Tutor Support for their maximum effort to assist me.