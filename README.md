# 0x00. AirBnB clone - The console

## About
A command line interpreter to manage future AirBnB projects.

 - put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future  instances
 - A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
 - classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 - first abstracted storage engine of the project: File storage.
 - unittests to validate all our classes and storage engine

## Usage

Example in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $

```

### Allowed Commands
All commands can be located in the [console.py](https://github.com/scurry222/AirBnB_clone/blob/master/console.py) file.
| Command                                                      | Description                             |
|:------------------------------------------------------------ |:--------------------------------------- |
| `./console.py`                                               | Runs the console                        |
| `quit`                                                       | Quits the console                       |
| `help <command>`                                             | Display help for command                |
| `create <class>`                                             | create an object and print its id       |
| `all` or `all <class>`                                        | shows all objects in stack              |
| `show <class> <id>` or `<class>.show(<id>)`                  | show a specified object                 |
| `destroy <class> <id>` or `<class>.destroy(<id>)`            | remove an object                        |
| `update <class> <id> <attribute name> "<attribute value>"`   | update an attribute of an object        |
      
## Models
All model classes are located in the [models](https://github.com/scurry222/AirBnB_clone/tree/master/models) folder.
| File          | Description                       | Attributes                            |
| ------------- |:--------------------------------- |:------------------------------------- |
| [base_model.py] (https://github.com/scurry222/AirBnB_clone/blob/master/models/base_model.py) | Base model for all other classes. | id, created_at, updated_at            |
| user.py       | Class for future users.           | email, password, first_name, last_name|
| state.py      | Class for State info.             | state_id, name                        |
| city.py       | Class for City info.              | name                                  |
| place.py      | Class for Place info.             | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_id |
| amenity.py    | Class for Amenity info.           | name                                  |
| review.py     | Class for Review info.            | place_id, user_id, text               |

## File Storage

The engine folder is to handle serialization and deserialization of the data by using the JSON format. The control flow looks like this:

`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`

## Tests

Tests for all code is in the [test_models](https://github.com/scurry222/AirBnB_clone/tree/master/tests/test_models) folder.

To run unittests for this program, cd into root directory and run the following command: `python3 -m unittest discover tests`

## Authors

[Scout Curry](https://github.com/scurry222)

[George Solorio](https://github.com/GeorgeSolorio)
