# Video Game Store
Django 3.2.10, the administration UI and the Django data model

* browsing video games by category
* performing searches using different criteria 
* viewing detailed information about each game
* adding games to a shopping cart and placing an order

### Requirements
* Python 3.8
* Pipenv
* Node npm

## Setup

### Installation
Install Python dependencies
```sh
pipenv install --dev
```

Install Npm dependencies
```sh
npm install
```

Run the migrations
```
(gamestore) $ python manage.py migrate
```

Run the application as usual
```shell
(gamestore) $ python manage.py runserver
```