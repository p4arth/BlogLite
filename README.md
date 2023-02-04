# **BlogLite**
Blog lite is a multi user platform on which users are able to express themselves to the world using the power of their writing.

# **Getting Started**
1. To run BlogLite locally first you will need to download all the source code.
2. Once the first instruction is done. You will need to go into the folder wherein all the source code of the application resides.
3. You will need to install all the pip packages present inside the `requirements.txt`. This can easily be done using the following steps:
    * Open your terminal.
    * Type ```cd \path\to\BlogLite\Folder```
    * Install the requirements using ```pip install -r requirements.txt```

# **Useage**
You can easily get started with running BlogLite by simply typing the following commands into your terminal after all the nessecary package requirements are installed:-
* Open your terminal
* Enter ```cd \path\to\BlogLite\Folder```
* Enter ```python app.py```

This will start the app locally.

# **Module Details**
* `api` module contains the implementaion of API endpoints.
* `app` contains the initialization code for the app.
* `controllers` contain the code regarding all the controllers to manipulate the models.
* `instance` contains the SQL Lite database and a csv for extra data.
* `models` contain the Flask-SQL Alchemy implementation of relational models.
* `static` contains all the static files used within the application.
* `templates` contain all the HTML templates.