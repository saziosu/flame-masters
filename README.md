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
There are three Epics within this project:

**EPIC: ONEt**
Details on epic one

**EPIC: TWO**
Details on Epic two


## User Stories
Majority of User stories are linked to Epics. Labels are applied for prioritisation, such as `must have`, `should have` and `could have`.

**Epic**|**User Story**|**Label**
TABLE OF USER STORIES

## Wireframes

The following wireframes were used to plan the look of the site:
IMAGE

# Design

## Color Scheme

COLOR SCHEME DETAILS

## Typography

Fonts were chosen from GoogleFonts

* [Syne](https://fonts.google.com/specimen/Syne) was used for header fonts
* [Inter](https://fonts.google.com/specimen/Inter) was used for all other fonts
* San-serif was used as the fallback font

## Imagery

**All images were chosen to match the theme of the site**
IMAGE DETAILS

# Features 

## Current Features

### Feature One
details and image

### FEATURE TWO
details and image


## Future Features

* Details
* On
* Future
* Features

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