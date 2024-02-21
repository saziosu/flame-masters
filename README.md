# Flame Masters

![amiresponsive](readme-images/amiresponsive.png)

Link for the finished deployed site: https://flame-masters-f04a2ade371e.herokuapp.com/

# Table of Contents

- [Flame Masters](#flamemasters)
- [Table of Contents](#table-of-contents)
- [Site Goals](#site-goals)
- [Agile Methodology](#agile-methodology)
  - [Labels](#labels)
  - [Epics](#epics)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Features](#features)
  - [Current Features](#current-features)
  - [Future Features](#future-features)
  - [Accessibility](#accessibility)
- [Technology Used](#technology-used)
  - [Languages](#languages)
  - [Frameworks, Libraries \& Programs](#frameworks-libraries--programs)
- [Deployment \& Development](#deployment--development)
  - [Forking the Repository](#forking-the-repository)
  - [Deploy to Heroku](#deploy-to-heroku)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Content](#content)
- [Acknowledgements](#acknowledgements)


# Site Goals
The goals of the site are to provide users with an attractive site providing a range of Hot Sauces and Spicy Snacks with varying levels of heat.
The user can decide how hot they want to go and view all products within that range.
If the user has a favourite brand, they can also view all products from that range.


# Agile Methodology
This project was developed using agile methodologies by utilising Epics and User stories.
User storied were assigned to Epics. 
The Epics & User Stories were prioritised by labels. `must have`, `should have`, `could have`.
A kanban board in GitHub was used to track these, with a `not started`, `in progress`, `done`, `NINTH(not important, nice to have)` and `bug` sections.
When a user story is completed, it gets moved to the done section.
The full kanban board can be viewed here: LINK

## Labels
The labels are priorised as follows:

|             |                                                                                      |
|-------------|--------------------------------------------------------------------------------------|
| must have   | This feature/issue is required for the project to function                           |
| should have | Important to implement but will not crash the project without but still key features |
| could have  | would like to have, but not essential to the project                                 |
| bug         | Something isn't working                                                              |

These result in the following stats:

![User story stats](readme-images/story-stats.png)

## Epics
There are six Epics within this project:

**EPIC: Design & Experience**
This epic focuses on the overall styling of the website

**EPIC: User Interactivity & Feedback**
This epic focuses on the communications between the website and the user

**EPIC: Product Admin**
This epic focuses on the product management on the front end for the admin user

**EPIC: User Accounts**
This epic focuses on the user's ability to register for an account

**EPIC: Product Viewing**
This epic focuses on the features of viewing products on the front end for the shopping user

**EPIC: Cart & Payments**
This epic focuses on the shopping cart and payments


## User Stories
Majority of User stories are linked to Epics. Labels are applied for prioritisation, such as `must have`, `should have` and `could have`.

**Epic**|**User story**|**Label**
:-----:|:-----:|:-----:
-|As a Developer, I can deploy the website early so that I can avoid any technical issues or stress later in the project|Must have
 Design & Experience|As a User, I can view a clean and attractive website so that I can have a positive experience|could have
 Design & Experience|As a User, I can receive feedback messages so that I can gain feedback from the actions I have completed|could have
User Interactivity & Feedback|As a User, I can receive confirmation emails so that I can track my order|should have
User Interactivity & Feedback|As a User, I can contact the website admins so that I can resolve any issues with my order|could have
User Interactivity & Feedback|As a user, I can leave reviews on a product so that I can give my opinion on the product|could have
User Interactivity & Feedback|As a user, I can sign up for a newsletter so that I can keep up to date on news from my favourite store|could have
User Interactivity & Feedback|As a user, I can edit my product reviews so that I can update my feedback|should have
User Interactivity & Feedback|As a User, I can delete my reviews so that I can change my feedback|could have
Product Admin|Allow Admin users to create products|must have
Product Admin|As an Admin, I can update products on the front end so that I can update details on the products|must have
Product Admin|As an Admin, I can delete products on the front end so that I can manage my store|must have
User Accounts|As a user, I can register for an account so that I can manage my details|should have
User Accounts|As a user, I can view my order history on my profile so that I can track my purchasing|could have
User Accounts|As a user, I can update my personal details so that I can have them saved for my next purchase|should have
Product Viewing|As a user, I can view all available products so that I can compare and decide which I want to purchase|must have
Product Viewing|As a user I can view the detailed descriptions of a product so that I can decide if it is suitable for my taste|must have
Product Viewing|As a user I can see the price of the product so that I can know if its in my price range|must have
Product Viewing|As a user I can choose different categories from the front end so that I can find the products that I want to purchase|should have
Product Viewing|As a user, I can search for products so that I can find the product I am looking for|should have
Cart & Payments|As a user I can add products to my cart so that I can purchase them|must have
Cart & Payments|As a user I can remove items from my cart so that I can purchase something else|must have
Cart & Payments|As a user I can update the number of items in my cart so that I can easily purchase the correct number of items|must have
Cart & Payments|As a user I can see how much total order will cost so that I can know if I can afford my purchase|must have
Cart & Payments|As a user I can make payments so that I can receive my products|must have

## Wireframes

The following wireframes were used to plan the look of the site:

Home Page:
![homepage wireframe](readme-images/homepage-wireframe.png)

Products Page:
![products wireframe](readme-images/products-wireframe.png)

Cart Page:
![cart wireframe](readme-images/cart-wireframe.png)

# Design

## Color Scheme

The main color scheme is white, grey and black.
This overall gives a pleasant, clean look to the website

## Typography

Fonts were chosen from GoogleFonts

* [Syne](https://fonts.google.com/specimen/Syne) was used for header fonts
* [Inter](https://fonts.google.com/specimen/Inter) was used for all other fonts
* San-serif was used as the fallback font

## Imagery

Images were sourced from several places to get suitable images of a wide range of products.
The full details of sources are in the media credits section of this README

# Features 

## Current Features

### Navigation
![navigation](readme-images/navigation.png)
The navbar is based on the Boutique Ado walkthrough. It is responsive via the bootstrap classes and features options like filtering products, contacting the website admins, viewing the shopping cart and signing up/logging in.

### Authentication
![register](readme-images/register.png)
The authentication is located in the top header navbar section.
This allows users to register for an account, login and sign out.
This allows users to see different content based on their account role like user, or admin/superuser

### Products
![products](readme-images/all-products.png)
The products page is based on the Boutique Ado walkthrough.
It is also responsive via the bootstrap classes and features counts of the products features.
It also allows sorting by brand name, heat level, price, etc.

#### Product Detail
![product detail](readme-images/product-detail.png)
The product detail allows the user to view the full details of the product.
The user can add the product to the cart from this page.
It also includes the average rating and ingredients.
If the website owner marks the product as a staff favourite it also notes this for the user on this page.

### Product Reviews
![product reviews](readme-images/product-review.png)
The product reviews can be found at the bottom of the product detail page.
This allows users to add review if they have ordered a product.
They can also only leave one review for a product, this helps prevent the data on the rating from getting skewed by multiple reviews from one person.
The user that made the review is allowed to edit or delete their review, allowing them to change their feedback.

### Cart & Checkout
![cart](readme-images/cart.png)
The shopping cart uses bootstrap to remain responsive.
It also allows the user to increase or decrease the number of items in the cart via the buttons on the right.

![checkout](readme-images/checkout.png)
The checkout also uses bootstrap to remain responsive.
It provides on order summary and allows the user to save the details added to the checkout to their profile if they are logged in.

### User Profile
![profile](readme-images/profile.png)
The user profile allows the user to update their information that will be loaded into the checkout.
The user can also view their previous orders via the profile page.

### Contact
![contact](readme-images/contact.png)
The contact page allows users to get into contact with the website owners. They can submit general queries, complaints and returns on this page.
This page also allows the user to sign up for the MailChimp newletter to keep up to date with the latest news.

### Contact Submissons
![contact submissions](readme-images/contact-submissions.png)
Superusers can view the contact submissions page, which shows the details of the contact form submissions.
This allows the superusers to view the contacts from their users and provides them with their email address so they can liase with them further.

### User permissions
![user permissions](readme-images/user-perms.png)
The website allows front end CRUD operations for the superuser.
They can add, edit and delete products.
A user that leaves a review is also allowed to add, edit and delete product reviews for products they have purchased.
The restrictions added via the code ensures that there is a secure check placed on each crud operation to ensure only the correct user is allowed to complete these actions.


## Future Features

* Wishlist: It would be nice to have a wishlist to allow users to have more interations with the site. The wishlist is also great for the owners of the site as it allows them to show which products their users love and can then use that information to gear their marketing towards that further.
* Multiple payment options: This site currently uses stripe payments, it would be nice in future to add options to include applepay and google pay to allow for swifter checkouts.
* Live Chat Support: As the website grows, it would be great to include a live chat support for users to speak directly with a member of staff for any questions or concerns they may have.

## Accessibility

ACCESSIBILITY CONSIDERATIONS

# Technology Used

## Languages

* HTML
* CSS
* Python
* JavaScript

## Frameworks, Libraries & Programs 

* BootStrap
* Django
* AutoSlug
* [ElephantSQL](https://www.elephantsql.com/) + PostgreSQL
* AWS S3
* CrispyForms
* django-allauth
* django-phonenumber-field & phonenumbers
* gunicorn
* psycopg2
* requests-oauthlib
* sqlparse
* urllib3

# Deployment & Development

## Forking the Repository

1. Log in or Sign up to [GitHub](https://github.com/)
2. Navigate to https://github.com/saziosu/book-swap.
3. Click the 'fork' button in the top right corner.
4. Feel free to customize your repo name, this is not required.
5. Click the Create Fork button.

## Deploy to Heroku
Heroku was used to deploy this site:

1. Run pip3 freeze > requirements.txt in the console to set up the requirements.txt file. This command will create the file if it does not already exist.
2. Commit any changes and push to GitHub.
3. Navigate to Heroku's website and log in to the dashboard.
4. Click on "Create new app" in the top right.
5. Enter the "App name" and select your region, then click "Create App". 
6. Head to the Settings tab in the new app.
7. Go to "Config Vars" under the Settings tab.
8. Click on "Reveals Config Vars".
9. Add the "ARN", "DATABASE_URL", and "SECRET_KEY" values generated for the project
10. Add "PORT" key and "8000" value to the config vars.
11. Move to the "deploy" tab on the app, and scroll down to the deployment method section.
12. Select "GitHub" and connect to GitHub.
13. Search for the appropriate GitHub repo and Connect.
14. Select "Automatic deploys" or "Manual deploys" to deploy the application.


# Testing

[TESTING.md](TESTING.md)

# Credits

## Code

* CODE
* CREDITS
* HERE


## Media

* MEDIA
* CREDITS
* HERE


## Content

* CONTENT
* CREDITS

# Acknowledgements

* Thanks y'all

[Top](#flamemasters)