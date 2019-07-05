# 0x00. AirBnB clone - The console

A command line interpreter to manage future AirBnB projects.

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

|                       Command                            |             Description                 |
|:-------------------------------------------------------- |:--------------------------------------- |
| ./console.py                                             | Runs the console                        |
| quit                                                     | Quits the console                       |
| help <command>                                           | Display help for command                |
| create <class>                                           | create an object and print its id       |
| all` or all <class>                                      | shows all objects in stack              |
| show <class> <id> or <class>.show(<id>)                  | show a specified object                 |
| destroy <class> <id> or <class>.destroy(<id>)            | remove an object                        |
| update <class> <id> <attribute name> "<attribute value>" | update an attribute of an object        |
      
## Models
| File          | Description                       | Attributes                            |
| ------------- |:--------------------------------- |:------------------------------------- |
| base_model.py | Base model for all other classes. | id, created_at, updated_at            |
| user.py       | Class for future users.           | email, password, first_name, last_name|
| state.py      | Class for State info.             | state_id, name                        |
| city.py       | Class for City info.              | name                                  |
| place.py      | Class for Place info.             | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_id |
| amenity.py    | Class for Amenity info.           | name                                  |
| review.py     | Class for Review info.            | `place_id, user_id, text`             |

## File Storage

The engine folder is to handle serialization and deserialization of the data by using the JSON format. The control flow looks like this:

`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`

## Tests

Tests for all code is in the test_models folder.

## Authors

[Scout Curry](https://github.com/scurry222)

[George Solorio](https://github.com/GeorgeSolorio)
