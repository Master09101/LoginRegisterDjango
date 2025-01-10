# Django Telegram Notification Web Project

This project is a web application built with Django that allows users to **register** and **log in**. The system is integrated with PostgreSQL as its database and uses Telegram Bot API to notify admins whenever a new user registers. The project also utilizes Git for version control to enable collaborative development and maintain a history of changes.

---

## Features

### User Registration
- Users can sign up by providing their details through a registration form.
- The form validates user inputs to ensure data accuracy.
- After successful registration, the user can log in to access the application.

### User Login
- Registered users can log in to their accounts using their credentials.
- Passwords are securely hashed using Django's built-in authentication system.

### Telegram Notifications
- A Telegram bot is used to notify admins about new user registrations.
- Notifications include user details (e.g., username, email) for easy monitoring.

### PostgreSQL Database Integration
- All user data is securely stored in a PostgreSQL database.
- The application is designed to handle relational data efficiently.

### Git Version Control
- The project is version-controlled using Git, enabling easy collaboration and rollback if necessary.
- Branching and merging are used to implement new features or fix issues.

---

## Technology Stack

- **Backend**: Django 4.x (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Bootstrap for responsiveness)
- **Notifications**: Telegram Bot API
- **Version Control**: Git and GitHub
- **Environment**: Python 3.x virtual environment

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.8 or later
- PostgreSQL
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git

---

## Installation Guide

Follow these steps to set up the project on your local machine:

### Step 1: Clone the Repository
Clone the GitHub repository to your local machine:
```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Project
Edit the `settings.py` file to configure the project:
1. **Database**:
   Replace the default database settings with your PostgreSQL connection details:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<your-database-name>',
           'USER': '<your-database-user>',
           'PASSWORD': '<your-database-password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
2. **Telegram Bot**:
   Add your Telegram bot token:
   ```python
   TELEGRAM_BOT_TOKEN = '<your-bot-token>'
   ```
3. **Admin IDs**:
   Specify the Telegram IDs of admins to receive notifications:
   ```python
   TELEGRAM_ADMIN_IDS = [<admin-id1>, <admin-id2>]
   ```

### Step 5: Apply Migrations
Run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser
Create a superuser account to access the Django admin panel:
```bash
python manage.py createsuperuser
```

### Step 7: Run the Server
Start the development server:
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## Setting Up the Telegram Bot

### Step 1: Create a Telegram Bot
1. Open [@BotFather](https://t.me/BotFather) on Telegram.
2. Use the `/newbot` command to create a new bot.
3. Follow the instructions and save the provided token.

### Step 2: Configure the Bot in the Project
Add the bot token to the `settings.py` file as `TELEGRAM_BOT_TOKEN`.

### Step 3: Get Admin Telegram IDs
Use the bot or tools like [@userinfobot](https://t.me/userinfobot) to retrieve the Telegram IDs of admins. Add these IDs to `TELEGRAM_ADMIN_IDS` in `settings.py`.

---

## Usage Workflow

1. **User Registration**:
   - A user signs up via the registration page.
   - Registration details are validated and stored in the PostgreSQL database.

2. **Admin Notification**:
   - Upon successful registration, the system sends a Telegram notification to admins.
   - Notification includes the user's username, email, and registration time.

3. **User Login**:
   - The registered user logs in using their credentials.

4. **Admin Monitoring**:
   - Admins monitor registration activities through Telegram notifications and the Django admin panel.

---

## Git Workflow

To manage version control, follow these steps:

### Basic Commands
1. **Stage Changes**:
   ```bash
   git add .
   ```
2. **Commit Changes**:
   ```bash
   git commit -m "Descriptive commit message"
   ```
3. **Push Changes**:
   ```bash
   git push origin main
   ```

### Branch Management
- Create a new branch for feature development:
  ```bash
  git checkout -b feature-branch-name
  ```
- Merge the branch after completing the feature:
  ```bash
  git checkout main
  git merge feature-branch-name
  ```

---

## Troubleshooting

### Common Issues
1. **Database Connection Error**:
   - Ensure PostgreSQL is running and connection credentials are correct.
2. **Telegram Bot Notifications Not Working**:
   - Verify the bot token and admin IDs in the `settings.py` file.
   - Check internet connectivity on the server.

---

## Author

This project was created and maintained by Rahimov A.  
Feel free to contact me for any questions or contributions.


## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
```

This version includes detailed instructions, troubleshooting tips, and expanded sections for better clarity. Let me know if there’s anything more you’d like to add!
