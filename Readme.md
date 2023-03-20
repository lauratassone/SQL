# SQL Project

## Hello everyone, welcome to my SQL project !
### Reminder of the project :
The goal of the project was to know how to migrate information to a new database.
So the subject is:

“ You have been contacted by TeamLikwid to migrate their old database to their new schema. They want you to:
- Create a .sql script that will create the new database schema
- Create a second script that will transfer data from the old database to the new one.

Also, to make sure they can still access their data, they want you to show queries + results for the following: 
- List all tournaments for a given game name - Given a game name , get average player salary 
- List all tournaments by location 
- Get number of players by gender. »

A help diagram was also provided.
It allowed me to visualize the shape of the old database as well as that of the new one.
Finally, it was necessary to recover the file containing the old database.
Once all this analyzed, it was finally time to start !


### In this project we will see how to migrate data from one database to another.
For this there are several steps:
- I first started taking the old database file that was provided
- I then created a new database
- I then created the tables to make the new database schema as requested in the instructions
- I then migrated the data from the old database to the new
- I then ended up doing the requested queries to check that everything worked


### Script Bash
To launch the file in a simpler way I created a bash script which allows me to execute everything at the same time.

To run my file, just run the command in the terminal, and choose the option that suits you best

#### The command is : sh script.sh

### Script Python 
I quickly realized that Bash script had limitations in its use.
The functionality I wanted to add to my script was not available.
So I decided to create a python script.
This allows me to exchange with the user for additional information.
So I started on the same basis as my Bash script, only the syntax changes since the language is different.

To run my Python script, we can do it, just like the bash script.

So just run the command in the terminal, and choose the option that suits you best

#### The command is : python3 migration.py 