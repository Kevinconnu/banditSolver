# banditSolver
banditSolver.py is a basic python3 program made to solve levels of the [Bandit Labs CTF](https://overthewire.org/wargames/bandit/) using a json config file as input

## Dependencies
-pwntools (use [pip](https://pip.pypa.io/en/stable/) to install)

```bash
pip install pwntools
```

## Usage 
The program functions by connecting via SSH to level 0 of bandit, using the password from the first config file 'bandit0.cfg'. Next, any necessary commands to complete the level (noted in the config file) will be executed. When the password is returned from the bandit server, a file will be created in the user's cwd called 'banditPasswords.txt', and the new password will be stored in this file. The program will then repeat itself for every consecutive config file found in the users cwd, using the password it has previously saved to the text document to gain access to the next level.

### Input
###### The config document
All input and direction of the program comes from json format config files, files must be named for the level they pertain to aka 'bandit0' contains the log in info and commands to complete level 0, etc. The first 4 fields must contain the address, port, username and password information.

```bash
    "address": "bandit.labs.overthewire.org",
    "port": "2220",
    "username": "bandit0",
    "password": "bandit0"
```
NOTE: Only the level 0 config file (aka 'bandit0.cfg') will actually contain a password, since finding each level's password is what this program will do. In all consecutive levels' config files, the password value should remain blank.

After the 4 SSH info fields will come the commands. Remember the config document is in json formatting, so each command must follow the same formatting rules. Commands must be named for the order they should be executed, ie 'cmd1', 'cmd2' etc.

### Output
Any passwords the program obtains will be saved to a new file called 'banditPasswords.txt' in the cwd. This file is referenced by the program when it logs on to the next level.

## Disclaimer

I am a noob, and this is the largest thing I've built to date without a step by step guide - Please let me know how I can be more effecient and effective!
