# AirBnb Clone version 0 - Console and Engine

A command line interpreter to manage future AirBnB projects.


## File Storage

The engine folder is to handle serialization and deserialization of the data by using the JSON format. The control flow looks like this:
`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`

## Usage

The shell works like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```
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
```

## Usage


- ```./console.py``` - Runs the console

- `(hbnb) quit` - Quits the console

- `(hbnb) help <command>` - Display help for command

- `(hbnb) create <class>` - Create an object, prints its id

- `(hbnb) all` or `(hbnb) all <class>` - shows all objects in file

- `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` - show an object

- `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` - remove an object

- `(hbnb) update <class> <id> <attribute name> "<attribute value>"` - update an attribute of an object

## Models


- `base_model.py`: Base model for all other classes. Attributes: `id, created_at, updated_at`

- `user.py`: Class for future users. Attributes: `email, password, first_name, last_name`

- `state.py`: Class for State info. Attributes: `state_id, name`

- `city.py`: Class for City info. Attributes: `name`

- `place.py`: Class for Place info. Attributes: `city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids`

- `amenity.py`: Class for Amenity info. Attributes: `name`

- `review.py`: Class for Review info. Attributes: `place_id, user_id, text`



## Authors

[Scout Curry](https://github.com/scurry222)

[George Solorio](https://github.com/GeorgeSolorio)
