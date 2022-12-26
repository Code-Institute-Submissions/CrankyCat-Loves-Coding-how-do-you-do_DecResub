# [**How Do You Do**](https://hdyd.herokuapp.com/)

![Portfolio image](media/home-page.jpg)

## **Overview**

I always wonder how many days I feel happy and how many days I feel upset in a month.So I have a little notebook to track my emotions. I found it helps me to better manage my feelings. For example, I most likely try harder to calm myself down if I find myself upset most of the time. This is so true that ' Nobody can make you happy until you're happy with yourself FIRST. 'So~ here is how it works. Be honest with yourself and simply record your emotions by clicking RecordEmo and you can track all of your records by clicking EmoBox and that's it! Login and start from today!

## **Table of Contents**

- [**CNEbroidery**](#overview)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)
    - [**1. What Is It?**](#1-what-is-it)
    - [**2. How to Achieve?**](#2-how-to-achieve)
    - [**3. Testing and Launch**](#3-testing-and-launch)
    - [**4. Deployment**](#4-deployment)
    - [**5. Support**](#5-support)
    - [**6. Reference and Research**](#6-reference-and-research)

## **1. What Is It?**

- How Do You Do (Moody Box)
This is a website allows you to record your emotions and hope that eventually will help you become happier everyday.

[Back to the top](#overview)

## **2. How to Achieve?**

- ## **Strategy**

  - The target audience for 'Moody Box' are:
    - People who enjoy writing diary

    - People who like to record their moments

    - People who try to manage their emotions
  
  - These users will be looking for:

    - A website is simple and easy to use

    - A private place to write diary

    - A full record of their feelings

- ## **User Stories**

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

- ## **User View**

  - This is fairly simple. A home and a logo link will take the User back to the index. An unauthenticated User has a chance to register or login the website. An authenticated User will be able to add emotions and review records.

  - At the How it works page, A User will explain how this website is going to work.

  - At the RecordEmo page, A User is able to select a date, a feeling and input some contents for record purpose.

  - At the EmoBox page, A User is able to review all individual's emo, User is able to delete any emo on this page. However, deleting emo is not recommended. So once the delete button is clicked. All records will be cleared.

  - At the Profile page (on the top right), A User is able to give himself a display name.

- ## **Coder View**

  - RecordEmo page is built based on CRUD - Create, Update and Delete method.

  - EmoBox page and is built based on CRUD - Read and Delete method.

  - Profile page and is built based on CRUD - Read and Update method.

  - Only an authenticated User is able to create, modify and delete data belonging to themselves.

  - Heroku was used for deployment.

  - AWS S3 was used for storing CSS and media.

  - DMB was used for styling.

  - Email verification with Google.

- ## **Design**

  - [Wireframes can be viewed here](https://github.com/CrankyCat-Loves-Coding/how-do-you-do/blob/main/media/doc/moody-box-wireframe.pdf)
  - Selected colors that represent peace and calm to build the website.
  ![color image](media/doc/color.jpg)
  - Selected Google Font Righteous
  ![font](media/doc/font-righteous.jpg)

[Back to the top](#overview)

## 3. **Testing and Launch**

- Manual testing details can be found [here](https://github.com/CrankyCat-Loves-Coding/how-do-you-do/blob/main/mood/README.md).

- Errors and Solution
  - ***Error 1***
    - ***Error message***: ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects
    - ***Solution***:
      - ```Heroku login -i``` (login to Heroku)
      - ```heroku stack:set heroku-20 -a <app name>```
      - runtime.txt (root directory, with the content of: python-3.8.14)
      - save, commit, push, deploy to heroku
      - [Article](https://devcenter.heroku.com/articles/heroku-20-stack)
  
  - ***Error 2***
    - ***Error message***: TypeError: expected str, bytes or os.PathLike object, not tuple
    - ***Solution***: ```MEDIA_ROOT = os.path.join(BASE_DIR, 'media')```, media_root was incorrectly set

  - ***Error 3***
    - ***Error message***: Class Product has no objects member
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

- Technology Stack
  There is a list of tools or method had been used during the period of development:

  *Building methods*
  - [x] [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
  - [x] [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - [x] [Django-countries](https://pypi.org/project/django-countries/)
  - [x] [AWS](https://aws.amazon.com/)
  - [x] [DMB](https://mdbootstrap.com/docs/standard/getting-started/installation/)
  - [x] [Heroku]( https://dashboard.heroku.com/apps)
  - [x] [pixabay - background image](https://pixabay.com/users/saydung89-18713596/?tab=most-relevant&pagi=3)
  - [x] [balsamiq](https://balsamiq.com/)
  - [x] [colormind](http://colormind.io/)

[Back to the top](#overview)

## 4. **Deployment**

- The site was deployed to [How do you do(Moody Box)]( https://hdyd.herokuapp.com/) page. The steps to deploy are as follows:

- In the Heroku page, select ‘Create new app’

- Create app name and choose a region

- Navigate to the setting tab. Add Python and node.js buildpacks

- At the deploy section, connect to Github, search and link to HDYD repository.

- Scroll down to set up automatic deploys, it enables Heroku to rebuild the app every time push code to Github.

- The live link can be found here [link]( https://hdyd.herokuapp.com/)

[Back to the top](#overview)

## 5. **Support**

- Code Institute Tutor Assistance
- [Coder 凯歌响起](https://blog.csdn.net/a13554371686?type=ask)

[Back to the top](#overview)

## 6. **Reference and Research**

- Reference
  - [x] [BugBytes](https://www.youtube.com/watch?v=MZwKoi0wu2Q&list=PL-2EBeDYMIbQSGbpvB59DJbf4Ox7hXPSU&ab_channel=BugBytes)

[Back to the top](#overview)
