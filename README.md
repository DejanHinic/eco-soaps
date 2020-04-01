[![Build Status](https://travis-ci.com/DejanHinic/eco-soaps.svg?branch=master)](https://travis-ci.com/DejanHinic/eco-soaps)
# EcOs - Organic soaps webshop

Stream Three Project: Data Centric Development - Milestone Project

<!-- ![EcOs Organic Soaps](https://github.com/DejanHinic/cook_book/blob/master/static/images/screencapture-noom-noom-cookbook-herokuapp-com-1583152419684.png?raw=true) -->


This project is part of the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course.

Project consists of the following sections:

1. Homepage - Containing 'Log in', 'Register', 'Cart' and 'All Products' button when user is not authenticated and 'Profile', 'Checkout' button when user is logged into his / her account.

2. Login form - Page containing the form that enables user to log into their account to use the app.

3. Register form - Page containing the form that enables user to sign up for the EcOs app.
 
4. All Products - Page displaying list of products with option of 'detail view'.

5. Detail view - Page containing more details about the product. 

6. Search - Page containing search.

7. Profile - Page containing user information, such as email.

## Table of Contents

- [Demo](#demo)
- [UX](#ux)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

<a name="demo"/>

## Demo

Website demo is available [here](https://eco-soaps.herokuapp.com/).

<a name="ux"/>

## UX

### UX Design

In this project I was aiming to achieve a simple and user friendly user design, while providing all required information. All sections are arranged in a logical order to provide intuitive user experience.

To create clean and bright design I used the following colors in my project: lightblue (`#add8e6`), ligtseagreen (`#17a2b8`), white (`#ffff`), black (`#373737`, `#292826`), slategrey (`#607981`).

### Target Audience

This application aims to attract people who care about their health and enviroment. Eco products are probably the future of washing, cleaning and many more use that we can think of. It is not enough to have just

a product, now it should have benefit to people and enviroment.

### User Stories

The following user stories were used to design this project:

**User Story 1:** As a user I would like to create an account to purchase products available in the app.

**User Story 3:** As a user I would like to have an option to login and logout of my account so nobody else can access it.

**User Story 4:** As a user I would like to see more details about products.

**User Story 5:** As a user I would like to be preview the products without creating an account to be sure that I want that products and then commit to registraton.

**User Story 6:** As a user I would like to be able to go back to cart and edit it.

**User Story 7:** As a user I would like to be able to complete my purchase at checkout.

**User Story 8:** As a user I would like to search any word referring product.

**User Story 9:** As a user I would like to see all collection of reviews in an organised, easy to navigate way.

### Mockups & Wireframes

The following [wireframe](https://github.com/DejanHinic/eco-soaps/tree/master/wireframe-mockups) sketches were created to design the project layout options for large, medium and mobile displays.

<a name="features"/>

## Features

### Existing Features

The project consists of various features presented below.

#### Page loading

- **Spinner** - jQuery method `show()` and `hide()` was used to create spinner showing while page is loading;

- **Overlay** - overlay that fades out the background while page is loading;

#### Buttons

- **Amend / button** - buttons that enable editing and deleting numbers of products;

- **Product detail /  button** - button that is linked to the view specific product;

- **Checkout button** - button that leads user to final stage of purchasing;

- **Add to cart button** - button that adds product to cart;

#### Forms

- **Register form** - register form that enables user to use the app. User input includes username, email address, and password (that has to be repeated);

- **Log in form** - login form that enables user to sign into the user account;

- **Checkout form** - form that asks user to enter the crucial information to be able to purchase the product;

- **Update comment form** - form that enables user to edit and resubmit the comment;

- **Reset password form** - form that allow user to reset the password and to recieve confirmation by email;

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices. 

- **Footer** - contains GitHub link to my profile on GitHub;

#### Alerts

- **Forms** - all forms have pop message that says that User can not leave empty space on placeholders if there is need to make some input and not leave it blank;

#### Other

- **Carusel** - Bootstrap carusel with image and text;

- **Search bar** - search bar that enables users to search any letter that product may contain;

### Features left to implement

List of features to be implemented in the future:

- add and edit username details;

- delete account; 

- pagination on product page;

- reviews app;

- rating system to products;

<a name="technologies-used"/>

## Techonologies & Languages Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)

* [Boostrap](https://getbootstrap.com/) was used mainly to make the website responsive on multiple devices using bootstrap grid.   

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) Stripe JavaScript was used to render the payment processing.

* [Gitpod](https://www.gitpod.io/) Gitpod was the IDE used to code the whole project with.

* [jQuery](https://jquery.com/) The project uses JQuery to simplify DOM manipulation.

* [Github](https://github.com/) Github was used to document the project progress.

* [HTML Validator](https://validator.w3.org/) This was used to validate the HTML code.

* [HTML Formatter](https://htmlformatter.com/) This was used for formatting the HTMl code.

* [Stripe](https://stripe.com/) Stripe is used for to make payments securely on any products on the page.

* [Postgres](https://www.postgresql.org/)/ [Sqlite3](https://www.sqlite.org/index.html) These were used for storing Databases.

* [Heroku](www.heroku.com) Heroku was used for hosting the web page.

* [Django](https://www.djangoproject.com/) Django frameworks were used for this project.

* [Python3](https://www.python.org/) Python3 was the main language used for this project.

* [Font Awesome](https://fontawesome.com/) Font Awesome was used to style the fonts/icons of the page.

* [Chrome Devtools](https://developers.google.com/web/tools/chrome-devtools) Google Chrome Devtools was used for inspecting webpage for any errors and used for designing the page in a faster way.

* [AWS](aws.amazon.com/) Amazon Web Services was used to host the media and static files for the project.

* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) Creation, configuration and management of AWS S3 Bucket.
‎
* [Gunicorn](https://pypi.org/project/gunicorn/) Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX to assist the deployment of Django projects to Heroku.

* [Pip](https://pip.pypa.io/en/stable/installing/) Used to install tools for the project.

* [Pillow](https://pillow.readthedocs.io/en/stable/) Python image library to help process images files to store in databases.

* django-forms-bootstrap This was used for styling Django Forms.

* [psycopg2](https://pypi.org/project/psycopg2/) Psycopg the most popular PostgreSQL database adapter was used for Python.

* [Adobe XD](https://www.adobe.com/products/xd.html) -  tool that was used to create mockups;


<a name="testing"/>

## Testing

### Code validation

#### CSS

CSS code was validated using the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/).

- all CSS code was passing.

#### HTML

HTML code was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

- All HTML templates were good. Only warning it shows for curly brackets from Ginger block codes.

#### JavaScript

JavaScript code was validated using [JSHint](https://jshint.com/).

#### Python

Python code was tested using medels test ([test.py](https://github.com/DejanHinic/eco-soaps/blob/master/products/tests.py) file).

All remaining features were tested manually. 

#### Travis 

* Travis was used to scan packages and libraries for bugs and anything that might damage travis or the server, to ensure that that server is safe and free of code that might be dangerous. All tests were passed, see the green build passing button in top of the README file and see pictures below

### Features testing

All the features were tested manually throughout the application development process. Table below outlines all features and tests performed on them, as well as all resolved and remaining bugs associated with tested features.

| Feature type                         | Feature                                  | Tests                                                                                                                                                                                                                                                                                                                                                                                                                       | Bugs                                                  |
| ------------------------------------ | :--------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------:|
| Buttons (including anchor links)     | Reset password                           | - test if clicking on button sent the message to mail;<br> - test all possibilities are correctly returned;                                                                                                                                                                                                                                                                                                                 | Message setnt confirmed but never recieve it on real mail.  |
|                                      | GitHub link                              | - test if clicking the link redirects user to my repository;<br> - test if GitHub page opens in a new tab;                                                                                                                                                                                                                                                                                                                  | No bugs.                                                |
|                                      | Detail view                              | - test if clicking the link redirect to detail page;<br> ;                                                                                                                                                                                                                                                                                                                                                                  | No bugs.                                                |
| Forms                                | Sign up form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;<br> - test if password hashing works i.e. password saved to database is hashed;                                                                                                                                   | No bugs.                                                  |
|                                      | Sign in form                             | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test is user can log in using incorrect password;                                                                                                                                                                                                                                | No bugs.                                                   |
|                                      | Checkout                                 | - test if input validation works correctly for each field;<br> - test if there is any field left empty the form cannot be submitted;<br> - test if submitted form saves data correctly into the database;                                                                                                                                                                                                                   | No bugs.                                                  |
| Structure                            | Navbar                                   | - test if all navbar menu items redirect user to the appropriate page;<br> - test if item that is currently active is highlighted;<br> - test if navbar collapses on smaller devices;                                                                                                                                                                                                                                       | No bugs.                                                 |
|                                      | Footer                                   | - test if GitHub link works correctly;<br> - test if footer stays at the bottom of the page;                                                                                                                                                                                                                                                                                                                                | No bugs.                                                 |
| Alerts                               | Toast messages                           | - test if all flash messages are styled with toastr;<br> - test if no text is cut off;<br> - test if delete button and progress displays correctly;<br> - test if different colors applied to different categories of toast messages;                                                                                                                                                                                       | No unresolved bugs left.                                 |
|                                      | Delete confirmation messages             | - test if confirmation message pops up when trying to delete a review or account;<br> - test if clicking 'delete' button on the message performs deleting;<br> - test if clicking 'cancel' cancels the action;                                                                                                                                                                                                              | No unresolved bugs left.                                 |
| Other                                | Search bar                               | - test various search bar inputs (ones that exist in the database and ones that do not);<br> - test search bar with no input provided;<br> - test if inputs are submitted on 'enter';<br> - check if search bar in not collapsing along with other menu items on smaller devices;                                                                                                                                           | No bugs.                                                 |


### Responsiveness testing

This site was tested across multiple browsers (Google Chrome, Mozilla Firefox) and on multiple mobile devices (iPad Mini, iPad, Huawei P20) to ensure compatibility and responsiveness.

Chrome developer tools were used to additionally inspect responsiveness for the following devices:

- iPad Pro / iPad / iPad Mini (portrait & landscape);

- iPhone 5/SE (portrait & landscape);

- iPhone 6/7/8 (portrait & landscape);

- iPhone 6/7/8 Plus (portrait & landscape);

- iPhone X (portrait & landscape);

- Android (Pixel 2) (portrait & landscape).

The website is fully responsive and working well on mobile devices.

#### Bugs:

- Email bug : Still having a problem with reset password email. Everything looks good and seems to be correct but when I allow 'risky apps' on google acccount to get the mail I never recieve it.

- requirements.txt file bug : I created a requirements.txt so I dont have to install all modules every time, but despite of that, every time when I exit Gitpod I have to Install all the modules which I need to work on project. 

<a name="deployment"/>

## Deployment

### GitHub

The site was developed using Gitpod. To keep records of different versions of all project files git version control system was used. 

To initialize the local repository I used Code Institute full template.

In order to track the changes in the local repository the following steps were taken:

- command `$ git add 'filename'` - to update what will be committed;

- command `$ git commit` - to commit the changes.

Using `$ git push` command all changes from the local repository were pushed to the remote one on GitHub.


### Django

To work on my new apps in Django I followed this steps:

    - pip3 install Django(==version you want to work in)

    - django-admin startproject NAME OF PROJECT .   

    - python3 manage.py runserver (or just run because we have all aliases specified in full template)

    - django-admin startapp NAME OF APP

    - in views.py create a view

    - urls.py connect the view to urls

    - python3 manage.py createsuperuser  making admin

    - python3 manage.py makemigrations  after making the models in models.py we allways need to make migrations

    - python3 manage.py migrate  after makingmigrations we allways need to migrate as well

    - in settings.py we need add our new applications and set ALLOWED HOST

    - at the end of project turned Deboug to False
    


   

### Heroku

This project is hosted using Heroku, deployed directly from the `master` branch. 

To deploy my project I followed these steps:

    - In order to run the app Heroku needs to install the required dependencies so make sure that 'requirements.txt' file was created and committed;

    - I used option to directly connect to github and to let Heroku to automaticly update my commits from GitHub;

    - all the KEYS and PASSWORDS, postgres data,  what we stored in env.py >> gitignore  we need to enter in Heroku Configurations

    - In order to create 'requirements.txt' file run `$ sudo pip3 freeze --local > requirements.txt` command in the terminal;

    - Procfile is a Heroku specific type of file that tells Heroku how to run our project;

    - For the 'Procfile' run `$ echo web: python > Procfile` command in the terminal;



### Stripe 

    - created STRIPE watching the tutorial from content of this course. 

    - Use the 4242 4242 4242 4242 card number and 123 cvv to test it 


### AWS Bucket 

 - created AWS bucked watching the tutorial from content of this course. 

           
<a name="credits"/>

## Credits

### Content & Media

All content I got from Google (texts and images)

### Media



### Acknowledgements

For this project I didnt use any help for mentors or tutors. ( I know I should, but everytime was too long to wait, and after I put more effort in solving the problem I always find a way) I was using the help of Slack community and contents on Google and Youtube.
