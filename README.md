# AirBnB_clone

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

## The project as a whole is composed of:

-A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

-A website (the front-end) that shows the final product to everybody: static and dynamic.

-A database or files that store data (data = objects).

-An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
 
We won’t build this application all at once, but step by step.

## The console:

The project currently only implements the back-end console.

    -Create your data model
    -Manage (create, update, destroy, etc) objects via a console / command interpreter
    -Store and persist objects to a file (JSON file)

## Usage:

The command interpreter runs both in the interactive mode  and also  the non-interactive mode: (like the Shell project in C)

The interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

The non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

All tests should also pass in non-interactive mode: 

    $ echo "python3 -m unittest discover tests" | bash

Classes in the project:
========================================

|   | PUBLIC INSTANCE ATTRIBUTES | PUBLIC INSTANCE METHODS |
| :------------ |:--------------------------:|:------------------------|
| BaseModel     | created_at |  save      |
|               | updated_at |  to_dict   |
|               | id         |        |
