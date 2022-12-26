# [**Moody Box Manual Testing**](https://hdyd.herokuapp.com/)

[Back to README](https://github.com/CrankyCat-Loves-Coding/how-do-you-do#3-testing-and-launch)

## **Overview**

This README file is for Moody Box Manual Testing.

## **Table of Contents**

- [**Moody Box**](#overview)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)
    - [**1. User Story**](#1-user-story)
    - [**2. Manual Testing**](#2-manual-testing)
    - [**3. Validation**](#3-validation)
    - [**4. Error and Solution**](#4-error-and-solution)

## **1. User Story**

- ***Part 1 – An unauthenticated User***

  - As an Unauthenticated User, I can use this website sensibly, so that I feel comfortable using it.

  - As an Unauthenticated User, I can find a guideline to understand how to use this website, so that I don’t get confused.

  - As an Unauthenticated User, I can sign up to use the website, so that I can keep my data privately.

  - As an Unauthenticated User, I can login to my own page, so I can keep track of my history.

- ***Part 2 - An authenticated User***

  - As an Authenticated User, I want my records to be private, so that I feel safe about what I have recorded.

  - As an Authenticated User, I can record anything I want, so that I can use it as my diary.

  - As an Authenticated User, I can view all records I have, so that I can go back and review when I want.

  - As an Authenticated User, I can edit any records I have., so I organized it.

  - As an Authenticated User, I can delete any records I like, so that I can control what I like to keep.

  - ***[Link to Github issue](https://github.com/CrankyCat-Loves-Coding/how-do-you-do/issues?q=is%3Aissue+is%3Aclosed)***

[Back to the top](#overview)

## **2. Manual Testing**

- ### ***Home page***

  - **Navbar**

    - **Moody Box(Website name)**:

      - click the Moody Box logo and redirect the user back to the home page as expected.

    - **Home**:

      - click Home redirect user back to home page as expected.

    - **Register**:

      - click Register redirect user to sign-up page as expected.

    - **Sign-in within sign-up page**:

      - click Sign-in redirect user to sign-in page as expected.

    - **Login**:

      - click Login redirect user to sign-in page as expected.

    - **Sign-up within login page**:

      - click Sign-up redirect user to sign-up page as expected.

    - **User Icon**:

      - click the User Icon and redirect an unauthenticated user to the sign-in page as expected.

    - **Youtube Icon**:

      - click Youtube Icon and open Youtube.com in a new tab as expected.

    - **Facebook Icon**:

      - click Facebook Icon and open Facebook.com in a new tab as expected.

    - **Twitter Icon**:

      - click Twitter Icon and open Twitter.com in a new tab as expected.

    - **Github Icon**:

      - click Github Icon and open the Moody Box Github page in a new tab as expected.

  - **Body**

    - **How it work**:

      - click How it works within the middle of the notification box and redirect users to the How-it-work page as expected.
  
  - **Footer**

    - **Source Code**:
      - click Source Code and open the Moody Box Github page in a new tab as expected.

  - **Allauth**

    - Users are able to sign up via the register page.

    - Message and notification displayed correctly after the user registered.

    - User is able to close the notification.

    ![Successful Sign up](https://res.cloudinary.com/dimaeig1n/image/upload/v1671926351/successful-signup-message.gif)

  - **Login**

    - User is able to login via the login page.

    - Messages pop up to notify users that they have been successfully signed in.

    - User is able to close the notification.

    - RecordEmo and EmoBox displayed at the navbar and within the middle box for an authenticated User.

    ![Successful Logged in](https://res.cloudinary.com/dimaeig1n/image/upload/v1671927840/successful-login.jpg)

  - **Responsiveness**

    - **Home/Register/Login/How it Works Page**:

      - All pages responsively displayed from large screen to mobile screen. Responsiveness was tested using Dev Tools to emulate the  device of Iphone SE(375*667). Details can be seen as below image

    - **Home Page**

    ![Home page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671922727/home-page.gif)

    - **Register Page**

    ![Register page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671924234/sign-up-page.gif)

    ![Register page with message](https://res.cloudinary.com/dimaeig1n/image/upload/v1671927345/successful-registered-message-responsive.gif)

    - **Login Page**

    ![Login page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671924624/login-page.gif)

    - **How it works Page**

    ![How it works page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671925005/how-it-work-page.gif)

- **Summary**

  - Manual testing for User Story [ Part 1 - An unauthenticated User ] is completed. Internal links are redirected correctly and External links are opened in new tabs. Mobile and window views display respectively. Registration process can be completed correctly and smoothly. Overall, the home page view and function is finished as expected.
  
  - Users are now able to navigate through the entire website and there is a page to explain how to use it. Users can register to start adding an emo or login as an authenticated user to review and organize their records.

[Back to the top](#overview)

- ### ***Profile page***

  - Click the user icon within the navbar and redirect users to the profile page.

  - Profile page renders user's display name if there is any, otherwise display None as default.

  - Click the edit button and redirect the user to the edit profile page, at the same time display a message with blue banner reminding the user that they are editing their display name.

  - Once the user clicked update, a message with green banner "Display name has changed to {profile.name} successfully" displayed and display name changed as expected.

  - Details can be found here ![change display name](https://res.cloudinary.com/dimaeig1n/image/upload/v1671931445/change-displayname.gif)

  [Back to the top](#overview)

- ### ***RecordEmo page***

  - RecordEmo within the navbar redirected to RecordEmo page correctly.

  - RecordEmo within the home page notification box redirected to RecordEmo page correctly.

  - RecordEmo within the how-it-works page redirected to RecordEmo page correctly.

  - RecordEmo within the EmoBox page redirected to RecordEmo page correctly.

  - An authenticated user is able to select a date to add an emo

  - An authenticated user is able to select Feeling types: happy, excited, calm, disappointed, anxious and angry

  - An authenticated user is able to enter details of their emo. The textfield is implemented via Summernote, it allows users to style texts and add image and much more.

  - Once Stuffing is clicked, a message with green banner "Emo added successfully! " display.

  - Then click the EmoBox redirected the user to the EmoBox page.

  - Details can be found here ![Add emo page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671933437/add-emo.gif)

  [Back to the top](#overview)

- ### ***Emobox page***

  - EmoBox within the navbar redirected to EmoBox page correctly.

  - EmoBox within the home page notification box redirected to EmoBox page correctly.

  - EmoBox within the how-it-works page redirected to EmoBox page correctly.

  - EmoBox within the RecordEmo page redirected to EmoBox page correctly.

  - An authenticated user click details redirected to show-emo page, this page listed all records related to requested user.

  - Details can be found here ![Emobox Page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671935381/emobox.gif)

  [Back to the top](#overview)

- ### ***Update Emo page***

  - Click update within emo detail page redirected user to edit emo page.

  - Within the edit emo page , a message with blue banner "You are editing an emo " displayed accordingly

  - A message with green banner "Emo updated successfully " displayed after click save(update).

  - Details can be found here ![Update Emo Page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671937007/update-emo.gif)

  [Back to the top](#overview)

- ### ***Delete Emo page***

  - A delete confirmation pop up after user clicked delete emo.

  - Click 'cancel' discharge pop up

  - Click 'yes. delete it' delete specify emo

  - A message with green banner "Emo deleted successfully " displayed after click 'yes. delete it' .

  - Details can be found here ![Delete Emo Page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671937835/delete-emo.gif)

  [Back to the top](#overview)

  - **Responsiveness**

    - **Profile/RecordEmo Page**:
      - All pages responsively displayed from large screen to mobile screen. Responsiveness was tested using Dev Tools to emulate the device of Iphone SE(375*667). Details can be seen as below image

    - **Profile page**

    ![Profile page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671932814/profile-Responsiveness.gif)

    - **RecordEmo page**

    ![RecordEmo page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671934686/add-emo-responsiveness.gif)

    - **Emobox page**

    ![Emobox page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671935687/emo-responsiveness.gif)

    - **Update Emobox page**

    ![Update page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671937235/update-emo-responsiveness.gif)

    - **Delete Emobox page**

    ![Delete page](https://res.cloudinary.com/dimaeig1n/image/upload/v1671937728/delete-emo-responsiveness.gif)

- **Summary**

  - Manual testing for User Story [ Part 2 - An unauthenticated User ] is completed. Data rendered correctly, update and delete function worked as expected. Message and pop up display as designed.

  - Users are now able to login to their personal account, modify or delete any records as well as add an emo after logging in.

[Back to the top](#overview)

## **3. Validation**

- [W3C HTML Validator](https://validator.w3.org/#validate_by_uri)

  - Document checking completed. No errors or warnings to show.

    - Details can be found here ![W3C HTML Validator result](https://res.cloudinary.com/dimaeig1n/image/upload/v1672008514/W3C_HTML_Validator.jpg)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_uri)

  - Document checking completed. No errors or warnings to show.
  
    - Details can be found here ![W3C CSS Validator result](https://res.cloudinary.com/dimaeig1n/image/upload/c_scale,w_800/v1672012260/W3C_CSS_Validator.jpg)

- [JSHint](https://beautifytools.com/javascript-validator.php)

  - No issue found.

- [CI Python Linter](https://pep8ci.herokuapp.com/)

  - No issue found.

- [Lighthouse](https://github.com/GoogleChrome/lighthouse/blob/HEAD/docs/user-flows.md)

  - Device: Desktop

    - ![Lighthouse desktop](https://res.cloudinary.com/dimaeig1n/image/upload/v1672014761/lighthouse-desktop.jpg)
  
  - Device: Mobile

    - ![Lighthouse Mobile](https://res.cloudinary.com/dimaeig1n/image/upload/v1672014761/lighthouse-mobile.jpg)

[Back to the top](#overview)

## **4. Error and Solution**

- ***Error 1***

  - ***Error message***:
  
    ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects

  - ***Solution***:

    - ```Heroku login -i``` (login to Heroku)

    - ```heroku stack:set heroku-20 -a <app name>```

    - runtime.txt (root directory, with the content of: python-3.8.14)

    - save, commit, push, deploy to heroku

    - [Article](https://devcenter.heroku.com/articles/heroku-20-stack)

- ***Error 2***

  - ***Error message***:

    TypeError: expected str, bytes or os.PathLike object, not tuple

  - ***Solution***:

    ```MEDIA_ROOT = os.path.join(BASE_DIR, 'media')```, media_root was incorrectly set

- ***Error 3***

  - ***Error message***:

    Class Product has no objects member

  - ***Solution***:

    - Fixed by adding ```objects = models.Manager()``` to Product.

    - That's not an error, it's just a warning from VSC. Django adds that property dynamically to all model classes (it uses a lot of magic under the hood), so the IDE doesn't know about it by looking at the class declaration, so it warns you about a possible error (it's not). objects is in fact a Manager instance that helps with querying the DB. If you really want to get rid of that warning you could go to all your models and add objects = models.Manager() Now, VSC will see the objects declared and will not complain about it again.

    - [Article](https://stackoverflow.com/questions/45135263/class-has-no-objects-member )

- ***Error 4***

  - ***Error message***: django.db.migrations.exceptions.NodeNotFoundError: Migration checkout.0005_order_coupon dependencies reference nonexistent parent node ('coupons', '0003_alter_coupon_coupon_code_alter_coupon_discount_price')

  - ***Solution***:

    - basicly to solved this error is to completely remove your Django migrations and reset your database.

    - before doing that it is better to save database by using ```python3 manage.py dumpdata products.product > products_dump.json```,```python3 manage.py dumpdata products.category > categories_dump.json```. this can be skip if fixture is in place. This is how we got them.products is the app name, product is the model, products_dump.json is the name of the file we put the data in

    - Remove the all migrations files within your project. Go through each of your project apps' migration folders and remove everything inside, except the init.py file.

    - Drop the database. If you're using Heroku Postgres, the command for this is: ```heroku pg:reset DATABASE_URL```, need to login to Heroku ```Heroku login -i``` before doing that

    - Run the commands ```python3 manage.py makemigrations``` and ```python3 manage.py migrate``` to remake migrations and setup the new database

    - ```python3 manage.py loaddata categories```, ```python3 manage.py loaddata products``` to load data back
  
  [Back to the top](#overview)
