# SHOES SHOP
> This project is an e-commerce website created to advert and sell shoes. The user can easily register and use the platform to buy shoes, create his own favourite wish list and give also a feedback to the seller after buying an item using the review and rating functionality provided.
The user receive also a confirmation email after registering for the first time, and after submitting any order request, this using Gmail account and deployment in Heroku.
The user can choose from 5 different categories of shoes and can easily buy any item available using the stripe payment gateway system.


## Table of Contents
* [Technologies](#technologies)
* [Features](#features)
* [Database](#database)
* [Testing](#testing)


## Technologies
### Languages
* [HTML5](#https://en.wikipedia.org/wiki/HTML5)
* [CSS3](#https://en.wikipedia.org/wiki/CSS)
* [JavaScript](#https://en.wikipedia.org/wiki/JavaScript)
* [Python3](#https://www.python.org/)

### Frameworks and Libraries
* [Django](#https://www.djangoproject.com/)
* [Pip3](#https://pip.pypa.io/en/stable/)
* [jQuery](#https://jquery.com/)
* [FontAwesome](#https://fontawesome.com/)
* [Bootstrap](#https://getbootstrap.com/)

### Others
* [Heroku](#https://id.heroku.com/login) used to deploy live site.
* [Stripe](#https://stripe.com/en-ie) used for the payments system.
* [AWS](#https://aws.amazon.com/) used for file storage.
* [GitHub](#https://github.com/) used to host repository.
* [GitPod](#https://www.gitpod.io/) used to develop project and organise version control.


## Features
### Wishlist page
One logged-in user can save his favourite products on his wishlist page.
On the wishlist page, the user can view:
- List of products of his favorite.
- By click remove button, one can remove the product from his wishlist.

### Orders page
On the orders page, the user can view the list of all his own orders.

### Order details page
On the order details page, the user can view:
- List all his purchased products for a specific order.
- Review form for feedback.

### Review
One user can give feedback and rate for a product of his purchased product.
The rating and feedback will be shown on the product details page.


## Database
Two relational databases were used to create this site - during development SQLite was used and then Postgres was used for the production on Heroku. Below is an image of ERD how the database models relate to each other:

<img alt="ERD" src="docs/ERD.png" width="700">


## Testing
### Testing from user stories
#### As an unregistered, I want to 

  + *be able to browse through all products available.*

All users, regardless of registered/logged in status, can browse through all products, add to bag and make a purchase:

<img alt="Unregistered user story" src="docs/user-stories/unregistered-01.jpg" width="700">

---

  + *have the ability browse through the categories on the site.*

All users, regardless of registered/logged in status, can browse through the listed categories:

<img alt="Unregistered user story" src="docs/user-stories/unregistered-02.jpg" width="700">

---

  + *have the ability to show details of a specific product on the site.*

All users, regardless of registered/logged in status, can see the products details: 

<img alt="Unregistered user story" src="docs/user-stories/unregistered-03.jpg" width="700">

---

  + *have the ability to see the reviews of a product details page.*

All users, regardless of registered/logged in status, can see the reviews of a specific product: 

<img alt="Unregistered user story" src="docs/user-stories/unregistered-04.jpg" width="700">

---


#### As an registered user, I want to 

  + *be able to create wishlist of my favourite products.*

An authenticated user, can add their favourite products in their wishlist:

<img alt="Registered user story" src="docs/user-stories/registered-01.jpg" width="700">

---

  + *have the ability browse through the 'My Wishlist' menu on the site.*

An authenticated user, can see his wishlists products:

<img alt="Registered user story" src="docs/user-stories/registered-02.jpg" width="700">

---

  + *have the ability browse through the 'My Orders' menu on the site.*

An authenticated user, can see his all orders:

<img alt="Registered user story" src="docs/user-stories/registered-03.jpg" width="700">

---

+ *have the ability to see specific orders details with purchased products through click on view button.*

An user, able to give feedback and rate the products from this page.

<img alt="Registered user story" src="docs/user-stories/registered-04.jpg" width="700">

---