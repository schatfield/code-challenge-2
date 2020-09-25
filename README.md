# Rest API using Flask, Marshmallow, SqlAlchemy, and Docker

Challenge: Build a RESTful API with Flask framework and some other supporting tools.

# How was this built?

- Flask - Python framework
- Docker - Container for running your database in
- SqlAlchemy - ORM connects to your database (communicates between your Python and database)
- Marshmallow - ORM, utilizing schemas for data serialization 

# What can you do with this?

- GET: Get information about all Budget Items / get one Budget Item
- POST: Add a new Budget Item
- DELETE: Remove a Budget Item
- PATCH: Edit a Budget Item

# Want to run this app? Follow the instructions below:

To build and run a Docker container with docker-compose:

```
docker-compose up --build -d
```

To start the Flask app:

```
# In a new terminal
python3 -m venv env
source .env/bin/activate
pip install -r requirements.txt
```
 ```
 # To load env variables
 export FLASK_APP=app.py
flask run
# Running on http://127.0.0.1:5000
```

# Budget Item Table
![ERD](https://i.imgur.com/fAjYETy.png)
