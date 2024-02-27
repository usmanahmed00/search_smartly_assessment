# SearchSmartly Assessment

## Overview

This program processes POI files and saves them into a database, and provides a django admin panel to view that information
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/usmanahmed00/search_smartly_assessment.git
   cd search_smartly_assessment

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv searchsmartly_env
   source searchsmartly_env/bin/activate  # On macOS/Linux
   searchsmartly_env\Scripts\activate     # On Windows

3. **Install the required dependencies:**
    ```bash
   pip3 install -r requirements.txt

4. **Apply Migrations**
   ```bash
   python manage.py migrate # Migrations are already applied if using database provided

5. **Create a superuser account**
   ```bash
   python manage.py createsuperuser # User already exists with admin, admin

## Usage
1. **Running the Program**

   To import PoI data from files located in the data_files/ directory, use the following management command:

    ```bash
   python manage.py process_files data_files/
- Place poi files in data_files/ directory

2. **Run the Development Server**
    ```bash
   python manage.py runserver

3. **Access the admin interface**
 Access the admin interface at `localhost:8000/admin`. Use the superuser credentials:
   - Username: admin
   - Password: admin



## Project Improvements

- **Database**: Update the DATABASES setting in settings.py for production use, possibly switching to PostgreSQL.
- **Version Control**: Add data_files/ and the SQLite database to your .gitignore to avoid committing large or sensitive files.
- **Code Formatting**: Use a code formatter like Black to maintain consistent code style.
- **Django Project Structure**: Consider using Cookiecutter to generate a Django project with a predefined structure.
- **Constants Module**: Create a constants module for storing project-wide constants.
- **Update Operations**: Enhance the management command to handle update operations instead of creating new objects everytime.
- **File Handling**: Extend the management command to support more types of files for data extraction.
- **Production Environment** Use a production deployment environment using Nginx etc instead of a development server.
- **Testing** Implement testing, such as Unit tests etc.
- **Logging** Implement a logger module to use logging where required.

## Assumptions
 - Assumed that internal_id is going to be the primary key for the models and external_id is the id fetched from the files.