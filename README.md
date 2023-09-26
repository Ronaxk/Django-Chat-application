This is a Django chat application that allows users to create accounts, login, view online users, start chats with online users, and restrict sending messages to offline users.

Requirements
Python 3.6+
Django 3.2+
Django REST Framework (DRF)
Django Channels
Redis
Installation
Clone the GitHub repository:
git clone https://github.com/YOUR_USERNAME/django-chat-application.git
Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Create a database and migrate the models:
python manage.py makemigrations
python manage.py migrate
Create a superuser account:
python manage.py createsuperuser
Start the Django development server:
python manage.py runserver
Usage
To register a new user, send a POST request to the /api/register/ endpoint with the following JSON body:
JSON
{
    "username": "username",
    "email": "email@example.com",
    "password": "password"
}
Use code with caution. Learn more
To login a user, send a POST request to the /api/login/ endpoint with the following JSON body:
JSON
{
    "username": "username",
    "password": "password"
}
Use code with caution. Learn more
To get a list of all online users, send a GET request to the /api/online-users/ endpoint.
To start a chat with an online user, send a POST request to the /api/chat/start/ endpoint with the following JSON body:
JSON
{
    "recipient": "recipient_username"
}
Use code with caution. Learn more
To send a message in a chat, send a WEBSOCKET request to the /api/chat/send/ endpoint with the following JSON body:
JSON
{
    "chat_id": "chat_id",
    "message": "message_text"
}
Use code with caution. Learn more
To get a list of suggested friends, send a GET request to the /api/suggested-friends/<user_id>/ endpoint.
Preventing users from sending messages to offline users
Before sending a message, the sender can validate the recipient's online status by sending a GET request to the /api/users/<user_id>/online-status/ endpoint. If the recipient is offline, the sender can display an error message to the user.

Test cases
The following test cases should be written to verify the functionality of the APIs and chat application:

Test that users can register and login successfully.
Test that users can view a list of all online users.
Test that users can start chats with online users.
Test that users can send and receive messages in chats.
Test that users cannot send messages to offline users.
Test that the suggested friends API endpoint returns a list of suggested friends for a given user.
GitHub repository
The GitHub repository for this project is [insert repository URL here].

Sharing the repository with the designated team
To share the repository with the designated team, you can add them as collaborators to the repository.

Conclusion
This Django chat application provides a basic framework for building a real-time chat application. It is important to note that this is just a starting point, and you may need to add additional features or functionality depending on your specific needs
