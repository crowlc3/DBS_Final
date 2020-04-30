# Final Project Technical Instructions

As the application you develop for your final project requires a number of interconnected parts, it's important that the various infrastructure components are consistent, so that your project will build and run properly on another machine with minimal intervention.

The `code` directory contains the minimum files your final submission should have. You may add additional files if you find that you need them, but their purpose should be clear, and where they fit into your overall application should also be clear.

## Supporting Files

There's an empty `readme.md` file. You should populate it with sufficient notes to allow someone to properly run and use the application.

## Database Setup

The database you use for your final project will be defined in `db-setup.sql`. Any of your code may create other database users, and grant them privileges, as you feel is necessary, but your initial access will be limited to the database and user created by the script.

Run it as a superuser: `psql -U postgres postgres < db-setup.sql`.

## Loading Data

In your code directory, there's a `datasets.txt` file. This file should contain the URLs for your datasets, one per line.

Running `retrieve_data.py` will download the datasets specified and place them in a newly created `datasets` directory within the `code` directory. (Any existing `datasets` directory will be destroyed in the process.)

There's currently a `load_data.py` file that will be invoked to load the data from your datasets into your database. You need to add code to have it create your schema, read the data files, and load the data into the database appropriately. It should be able to run from the command line with no additional arguments.

Your schema should go in the `schema.sql` file, and your `load_data.py` will need to make sure it's run at the appropriate time. Your data-loading code (either `schema.sql` or `load_data.py`) should contain appropriate code so that if there are already tables and data in the database, an additional run of `load_data.py` still leaves the database in a correct state (i.e., there shouldn't be multiple copies of the data, and it shouldn't fail).

## Running the Application

The entry point to your application should be in `application.py`. It should run properly from the command line with no additional arguments.

### Organization

Your database code should be separated from your application code. The interface/entrypoint for your database code should be in `database.py`. For this project, you can put all of your database-related code there if you'd like, but you're free to create additional python files in support of both `application.py` and `database.py` as you feel is appropriate.

Your code should be readable, through the appropriate choice of method, field, and variable names, and the appropriate use of comments. Personally, I prefer "self-documenting" code to excessive comments. Something like this:

```python
user_county_input = input("Enter a county name")
```

is generally preferable to 

```python
# Allow the user to choose a county
usr_ipt = input("Enter a county name")
```



### Queries

Your application should facilitate exploration of the data. Remember that the goal is to demonstrate (and hopefully practice and solidify) your understanding of the concepts discussed in class. In practice, it will be difficult to do that if your application doesn't meet at least the following:

- Five separate queries
- At least two queries that select at least some data from both of your datasets
- At least two queries that showcase syntax beyond the basic `SELECT-FROM-WHERE` clauses (e.g., Grouping, Subqueries, etc.)
- At least two queries that accept input entered by the user (as opposed to just allowing selection from a list of options)

Note that some queries are likely to fulfill more than one of the above requirements simultaneously.

### User Interface

This is not a UI/UX class. A simple text-based command line interface is completely acceptable. If you choose to do more (e.g., a web application) that's fine, but the UI isn't one of the graded components. If you do use something like a web application, `application.py` still needs to be the entry point for starting that application: ideally it will output a URL that can be opened in the browser (and that information should also be present in the readme).

While the database-related code will be reviewed for the security problems we discuss in class, you may assume for the purposes of this assignment that the UI will not be attacked: don't stress about making it resilient.

## Dependencies

There's a `requirements.txt` file in the `code` directory. It will be run on a fresh python 3.8 virtual environment before running your application.

## Submission

You should submit the contents of your `code` directory to submitty. As no data should be submitted, the entire submission should be small in size.