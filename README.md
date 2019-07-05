# AirBnb Clone version 0 - Console and Engine
______________________________________________________________________________
A command line interpreter to manage future AirBnB projects.

(https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190705T034345Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b86af63f24ff8d54946729c88d9012383d832b8f85e307a74115a6312624ec3)

## File Storage
______________________________________________________________________________________

The engine folder is to handle serialization and deserialization of the data by using the JSON format. The control flow looks like this:
`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`

## Usage
______________________________________________________________________________
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
_____________________________________________________________________________

- ```./console.py``` - Runs the console

- `(hbnb) quit` - Quits the console

- `(hbnb) help <command>` - Display help for command

- `(hbnb) create <class>` - Create an object, prints its id

- `(hbnb) all` or `(hbnb) all <class>` - shows all objects in file

- `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` - show an object

- `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` - remove an object

- `(hbnb) update <class> <id> <attribute name> "<attribute value>"` - update an attribute of an object

## Models
___________________________________________________________________________________________

- `base_model.py`: Base model for all other classes. Attributes: `id, created_at, updated_at`

- `user.py`: Class for future users. Attributes: `email, password, first_name, last_name`

- `state.py`: Class for State info. Attributes: `state_id, name`

- `city.py`: Class for City info. Attributes: `name`

- `place.py`: Class for Place info. Attributes: `city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids`

- `amenity.py`: Class for Amenity info. Attributes: `name`

- `review.py`: Class for Review info. Attributes: `place_id, user_id, text`

## Project Requirements

- Formatted with Betty style standards
- Compiled with gcc 4.8.4 (C90) using the flags -Wall -Werror -Wextra and -pedantic
- Maximum of one global variable
- No more than 5 functions per file
- Function prototypes should be included in a header file called monty.h
- Header files should be include guarded

## Project Data Structure
```
/**
 * struct stack_s - doubly linked list representation of a stack (or queue)
 * @n: integer
 * @prev: points to the previous element of the stack (or queue)
 * @next: points to the next element of the stack (or queue)
 *
 * Description: doubly linked list node structure
 * for stack, queues, LIFO, FIFO Holberton project
 */
typedef struct stack_s
{
        int n;
        struct stack_s *prev;
        struct stack_s *next;
} stack_t;



/**
 * struct instruction_s - opcoode and its function
 * @opcode: the opcode
 * @f: function to handle the opcode
 *
 * Description: opcode and its function
 * for stack, queues, LIFO, FIFO Holberton project
 */
typedef struct instruction_s
{
        char *opcode;
        void (*f)(stack_t **stack, unsigned int line_number);
} instruction_t;
```
_______________________________________________________________________________

## File Descriptions
- `monty.h` - function declarations
- `main.c` - entry point, getline loop
- `ll_helpers_1` - add node at end function
- `ll_helpers_2` - linked list functions to manipulate the stack
- `main_helpers.c` - struct of opcodes corresponding functions
- `op_helpers_1` - push, pall, pop, pint, and nop opcodes
- `op_helpers_2` - add, sub, mul, div, and mod opcodes
- `op_helpers_3` - stack, queue, rotl, rotr, and swap opcodes
- `str_helpers 1 & 2` - string modifying functions

________________________________________________________________________________

## Authors

[Scout Curry](https://github.com/scurry222)

[George Solorio](https://github.com/GeorgeSolorio)
