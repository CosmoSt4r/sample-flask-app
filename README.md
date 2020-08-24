# Sample Flask application

> Implemented systems of login, logout, registration and one interesting feature.


## What can I do with this?

![Login and Signup forms](https://github.com/CosmoSt4r/sample-flask-app/blob/master/readme/Login_Signup.png?raw=true)

__________

You can *register* or *login* if you already have an account.
You will see a **beautiful inscription** with your name, **account number** and **personal pattern**.

_________

![Homepage](https://github.com/CosmoSt4r/sample-flask-app/blob/master/readme/Homepage.png?raw=true)

_________

### What is personal pattern?

Click on it and find out!

<br>

## How to install?



### Clone

Clone this repo to your local machine using `https://github.com/CosmoSt4r/sample-flask-app`

### Required packages

To start the server you need the following packages: 

 - Flask
 - Flask_SQLAlchemy
 - Pillow
 - Pypasswords

> go to project folder and type

```py
pip install -r requirements.txt
```

### Starting the server

```py
python main.py
```
> or just open `main.py`

### Opening app in browser

Open your browser and go to the `127.0.0.1:5000` address. You will see the login page.

<br>

## Why do we need this packages?

### SQLAlchemy
- The **SQLAlchemy** package is used to **store information** about users with an **SQLite database** connected to it.

<br>

### Pypasswords
- Upon login, the **password** from the form is compared with the **hash** stored in the database using the method
**match_it** from **pypasswords** package. If there is a match, ~~they go on a date~~, the user gets to the home page.

###

- When user is registering new account, the **password** from the form is **hashed** with the **sha-256** algorithm using the function
**hash_it** from the same **pypasswords** package and along with the login is added to the database.

<br>

### Pillow

- **Pillow** is used to create a **personalized pattern**. For this, the hash of the username is taken, the first 25 digits are selected from it and used as information for generating image. Initially, it has a resolution of 5 by 5 pixels.

![Sample patterns](https://github.com/CosmoSt4r/sample-flask-app/blob/master/readme/Sample_patterns.png?raw=true)

- Then it is simply **mirrored** along the axes and a symmetrical 10 x 10 pixels pattern is obtained.

![Pattern mirroring](https://github.com/CosmoSt4r/sample-flask-app/blob/master/readme/Pattern_mirroring.png?raw=true)

- The **number of possible combinations**: there are only 25 unique pixels to fill 3 colors are used. This means the number of possible combinations is **3<sup>25</sup>**. (more than 840 billion)

<br>

## Where did I get such beautiful HTML and CSS templates?

- I used "[Login V3](https://colorlib.com/wp/template/login-form-v3/)" template for both **Log In** and **Sign Up** forms from colorlib.com
- Thanks to [Tee Diang](https://codepen.io/cybercountess) for this sweet [neon lettering](https://codepen.io/cybercountess/pen/RwNXxyq).
- This beatiful [font](https://www.fontsc.com/font/beon) for neon lettering is mage by [Bastien Sozoo](https://www.fontsc.com/font/designer/bastien-sozoo)
