How to Run the Project

Install Python
Make sure Python (preferably version 3.8 or higher) is installed on your system. You can download it from python.org
.

Install MySQL Server
Install MySQL Community Server and MySQL Workbench if needed. Make sure the server is running.

Install Required Python Libraries
Open a terminal or command prompt and run:

pip install customtkinter pillow mysql-connector-python


Set Up the Database

Open MySQL Workbench or your preferred MySQL client.

Run the provided SQL script (database.sql) to create the database and required tables.

Prepare the Project Files

Place the Python file (main.py), user_pass.txt, and all image files in the same folder.

In user_pass.txt, enter your MySQL username and password. Example format:

username: your_mysql_username
password: your_mysql_password


Run the Application

Open a terminal in the project folder.

Run the Python script:

python main.py


The GUI will launch. You can now sign up, log in, select movies, choose seats, and book tickets.
