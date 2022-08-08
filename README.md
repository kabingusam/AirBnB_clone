# AirBnB_clone

<div align = "left">
The goal of the project is to deploy on your server a simple copy of the AirBnB website.A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
A website (the front-end) that shows the final product to everybody: static and dynamic.A database or files that store data (data = objects).
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
 
We won’t build this application all at once, but step by step.
</div>

## The console:

The project currently only implements the back-end console.

    Create your data model
    Manage (create, update, destroy, etc) objects via a console / command interpreter
    Store and persist objects to a file (JSON file)

## Usage:

The command interpreter runs both in the interactive mode  and also  the non-interactive mode: (like the Shell project in C)

The interactive mode:

    $ ./console.py
    (hbnb) help

<<<<<<< HEAD
=======
**Documented commands (type help <topic>):**
>>>>>>> da769404f09a9d798eee720bf1f1ac73d3b3c38f

    EOF  help  quit

<<<<<<< HEAD

## Documented commands (type help <topic>):
=======
## Documented commands (type help <topic>):
=======
    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $
>>>>>>> da769404f09a9d798eee720bf1f1ac73d3b3c38f

### The non-interactive mode:

    $ echo "help" | ./console.py
    (hbnb)

**Documented commands (type help <topic>):**

    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

**Documented commands (type help <topic>):**

    EOF  help  quit
    (hbnb) 
    $

All tests should also pass in non-interactive mode: 

    $ echo "python3 -m unittest discover tests" | bash

### Classes in the project:

| CLASS          | PUBLIC INSTANCE ATTRIBUTES | PUBLIC INSTANCE METHODS |PUBLIC CLASS ATTRIBUTES | PRIVATE CLASS ATTRIBUTES |
| ---------------| -------------------------- | ----------------------- |----------------------- | -----------------------  |
| BaseModel      | created_at,updated_at,id   | save,to_dict            |                        |                          |
| FileStorage    |                            | all,new,save,reload     |                        | objects                  |
| User           | Inherits from BaseModel    |               |email,password,first_namelast_name|                          |
| State          | Inherits from BaseModel    |                         |                        |                          | 
| City           | Inherits from BaseModel    |                         | state_id               |                          |
| Amenity        | Inherits from BaseModel    |                         | name                   |                          |
| Review         | Inherits from BaseModel    |                         | place_id,user_id,text  |                          |
| Place          | Inherits from BaseModel    |                         |name,description,number_rooms,number_bathrooms,max_guest,price_by_night,latitude,longitude,amenity_ids |
