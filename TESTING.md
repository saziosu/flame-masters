# Flame Masters | Testing

Link for the finished deployed site: [FlameMasters](https://flame-masters-f04a2ade371e.herokuapp.com/)

![Amiresponsive image](readme-images/amiresponsive.png)

# Table of Contents

- [Flame Masters | Testing](#flamemasters--testing)
- [Table of Contents](#table-of-contents)
- [Testing Tools](#testing-tools)
  - [W3C Validator](#w3c-validator)
  - [CSS Validator](#css-validator)
    - [JavaScript Validator](#javascript-validator)
    - [Python Validator](#python-validator)
    - [Lighthouse Report](#lighthouse-report)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Fixed bugs](#fixed-bugs)

# Testing Tools

## W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML code across all pages of the website.
Due to the django templating, pasting directly from the code was not possible.
Instead the source code via the browser was used to test these and directly input into the validator.
Several changes were made to resolve any errors found


## CSS Validator

[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code across all possible pages of the website.

| Page     | Pass/Fail |
| -------- | --------- |
| Homepage | Pass      |
| Products | Pass      |
| Contact  | Pass      |
| Login    | Pass      |
| Cart     | Pass      |

All other pages required login which was not handled by the validator via the url
Most of the pages are utilising Bootstrap for styling, however the custom css from style.css was input manually and passed with no errors:

**base.css**
![base css](readme-images/base-css.png)

**checkout.css**
![checkout css](readme-images/checkout-css.png)

**profile.css**
![profile css](readme-images/profile-css.png)

### JavaScript Validator

[JShint](https://jshint.com/) was used to validate the JavaScript on the site.

Javascript from the following templates/files were tested:
* cart.html
* stripe_elements.js
* products.html
* quantity_input_script.html
* countryfield.js

All passed through the validators.
Most showed errors for undefined variables or unused variables, but these are coming from the HTML that is not seen by the validator

### Python Validator

The [Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code written on the project
Several edits were made to resolve any errors, which were mainly lines too long and a missing new line at the end of the file.
One file needed the `# noqa` applied as the long line could not be resolved.
Whenever this was updated, to resolve style issues it lead to python syntax errors and it was decided to leave this as is for the moment.
Some files, such as migration files and manage.py were showing lines too long but these were not updated as they are native django files

| File                            | Pass/Fail |
| ------------------------------- | --------- |
| cart/templatetags/cart_tools.py | Pass      |
| cart/apps.py                    | Pass      |
| cart/contexts.py                | Pass      |
| cart/urls.py                    | Pass      |
| cart/views.py                   | Pass      |
| checkout/admin.py               | Pass      |
| checkout/apps.py                | Pass      |
| checkout/forms.py               | Pass      |
| checkout/models.py              | Pass      |
| checkout/signals.py             | Pass      |
| checkout/urls.py                | Pass      |
| contact/admin.py                | Pass      |
| contact/forms.py                | Pass      |
| contact/models.py               | Pass      |
| contact/urls.py                 | Pass      |
| contact/views.py                | Pass      |
| flame_masters/urls.py           | Pass      |
| flame_masters/settings.py       | Pass      |
| flame_masters/views.py          | Pass      |
| home/apps.py                    | Pass      |
| home/urls.py                    | Pass      |
| home/views.py                   | Pass      |
| products/admin.py               | Pass      |
| products/apps.py                | Pass      |
| products/forms.py               | Pass      |
| products/models.py              | Pass      |
| products/urls.py                | Pass      |
| products/views.py               | Pass      |
| profiles/apps.py                | Pass      |
| profiles/forms.py               | Pass      |
| profiles/models.py              | Pass      |
| profiles/urls.py                | Pass      |
| profiles/views.py               | Pass      |

### Lighthouse Report

DETAILS ON LIGHTHOUSE TESTING

TABLE ON TESTING

# Manual Testing

A range of devices were used to test the site.

* OnePlus 7T Pro (Firefox, chrome, opera)
* MAC: MacBook Pro 14-inch 2021 (Mac OS Ventura 13.6.2) (Chrome, Safari, Firefox)
* LENOVO Tab P11 11.5" Tablet (Chrome, Firefox)

[Browserstack](https://www.browserstack.com/) was also used to test on the following devices:

* iPhone 15 (Chrome, Safari)
* iPhone 12 mini (Chrome, Safari)
* Samsung s23 (Chrome, Firefox)
* iPad 10th (Chrome, Safari)


TABLE OF TESTED FEATURES

# Bugs

## Known Bugs

To my knowledge there are no further bugs on this project

## Fixed bugs

All resolved bugs are listed on the [kanban board for the project](https://github.com/users/saziosu/projects/5)