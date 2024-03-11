0x00. AirBnB clone - The console

Description
This is the first of several lite clones of the AirBnB (online platform for rental accommodations) website. Classes for User, Place, State, City, Amenity, and Review are specified and they all inherit from the BaseModel class.

Instances are serialized and saved to a JSON file then reloaded and deserialized back into instances. Also, there is a simple command line interface (CLI) that abstracts the process used to create these instances.

Requirements
Python 3.4.3 or later

More Info
Execution
This shell program is executed like this in interactive mode:

$ ./console.py
(hbnb) help

# Documented commands (type help <topic>):

EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help quit
(hbnb)
$
