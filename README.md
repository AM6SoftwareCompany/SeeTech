# SeeTech

This is a very simple e-commerce website built with Django.


## Project Summary

The website displays products. Users can add and remove products to/from their cart while also specifying the quantity of each item. They can then enter their address and choose Stripe to handle the payment processing.


---

## Running this project

### what to do everytime to open it

open the main folder that has the virtual environment and the project
activate the env with this command on

mac/linux:

```
source dj/bin/active
```

windows:

```
dj\Scripts\activate
```

then go to the project folder

```
cd seetech
```

Now you can run the project with this command

```
python manage.py runserver
```


### Starting

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv dj
```

That will create a new folder `dj` in your project directory. Next activate it with this command on

mac/linux:

```
source dj/bin/active
```

windows:

```
dj\Scripts\activate
```
then go to the project folder

```
cd seetech
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

