Event Network Project
This is a event networking web application developed using Django.

Features
User registration and authentication
User profiles
Creating, editing, and deleting events
Searching for users and events
Friendship requests and management
Installation
Clone the repository:

bash
Copy code
Navigate into the project directory:

bash
Copy code
cd social-network
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:

bash
Copy code
env\Scripts\activate
On macOS and Linux:

bash
Copy code
source env/bin/activate
Install the dependencies:

Copy code
pip install -r requirements.txt
Run database migrations:

Copy code
python manage.py migrate
Create a superuser (admin):

Copy code
python manage.py createsuperuser
Run the development server:

Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000/

Usage
Register an account or log in with an existing account.
Create events, search for other users or events, and manage your profile.
Send and accept friendship requests to connect with other users.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
test
