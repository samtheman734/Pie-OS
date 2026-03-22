# Pie-OS
An operating system that runs entirely in user space and is only made up of 2 python scripts
# How to use
 Available Commands:
    - help                  : Show this help message
    - mk file               : Create a new file
    - open file             : Open and display a file
    - list [directory]      : List files in a directory
    - delete file           : Delete a specified file
    - rename file           : Rename a file
    - search                : Search for text within files
    - info                  : Show info about a file
    - clear                 : Clear the terminal screen
    - exit                  : Exit the system
    - applications          : List and launch apps
    - neutron               : Neutron Programming Language
    - launch app            : Launch a real installed app
    - python                : Launch the python interpreter
# Booting up:
step 1: clone into this repository. Do this by entering command prompt or opening a terminal and 
typing "git clone [repo url]" replace repo url with the actual url.

step 2: Download python3, this can be done by going into microsoft store or doing this command:
"sudo apt install python3" on linux systems.

step 3: Go into terminal and do "python3 PIE_OS.py".

# When you enter the environment:

you will see this screen:

Welcome to Pie OS!

Boot sequence initiated... Loading core modules and
environment. Ready for user commands.
Version: 1.0.0 | Build: Pie-2026
Status: All systems operational. Ready to accept commands.
Note: This is an operating system that
runs entirely in user space, designed for learning,
experimentation, and development.

Available Commands:
  - help                  : Show this help message
  - mk file               : Create a new file
  - open file             : Open and display a file
  - list [directory]      : List files in a directory
  - delete file           : Delete a specified file
  - rename file           : Rename a file
  - search                : Search for text within files
  - info                  : Show info about a file
  - clear                 : Clear the terminal screen
  - exit                  : Exit the system
  - applications          : List and launch apps
  - neutron               : Neutron Programming Language
  - launch app            : Launch a real installed app
  - python                : Launch the python interpreter

[Command]: *input command here!

# Please note that this is an os environment, not designed to run on actual hardware.
You can run it on hardware by making a custom bootloader that runs python as an environment.

Disclaimer: making a custom bootloader is an extensive task that requires knowledge of low level
programming and operating system design. This is primarily for education and development.
