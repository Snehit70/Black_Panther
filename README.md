# Black Panther - Student Collaboration Platform

A web application that helps students and developers showcase their projects and find collaborators. Built as a hackathon project using Flask backend and Bootstrap frontend.

## Team Members
- **Madhura** - Team Leader
- **Sejal**
- **Atulya**

## Project Overview

Black Panther is a collaboration platform designed for students and developers to share projects, connect with like-minded individuals, and build a portfolio of their work. The platform allows users to express interest in projects they'd like to contribute to, fostering collaboration and knowledge sharing.

[Project Demo Video](https://www.canva.com/design/DAGmOdtxOOQ/ukCKGqb_ZIBfFqcdx5b6hw/edit)

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap, HTML, CSS, JavaScript
- **Database**: SQLAlchemy with SQLite
- **Authentication**: Custom Flask authentication system
- **Form Validation**: WTForms and custom validators

## Features

- **User Authentication**: Create an account, login, and logout securely
- **Project Management**: Create, view, and search for projects
- **Interest System**: Express interest in projects to connect with creators
- **Profile Management**: Update your profile information and password
- **Comment System**: Discuss projects through comments
- **Search Functionality**: Find projects by title or technologies

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
   ```
   git clone https://github.com/snehit70/Black_Panther.git
   cd Black_Panther
   ```

2. Create a virtual environment (optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database

   Simply run the application once to create the database:
   ```
   python app.py
   ```

   The database tables will be automatically created on first run.

5. Run the application
   ```
   python app.py
   ```

   If you get "module not found" errors, make sure all dependencies are properly installed:
   ```
   pip install flask flask-sqlalchemy flask-bootstrap
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`

### Installation Troubleshooting

If you're experiencing issues with the requirements installation:

1. Try installing with pip in verbose mode to see detailed errors:
   ```
   pip install -v -r requirements.txt
   ```

2. Version compatibility: Some packages in requirements.txt are very recent versions:
   - Flask 3.1.0 requires Python 3.8+
   - SQLAlchemy 2.0.40 requires Python 3.7+
   - Several packages have interdependencies that might conflict

   Try installing with a slightly relaxed version constraint:
   ```
   pip install -r requirements.txt --no-deps
   pip install flask sqlalchemy flask-sqlalchemy flask-bootstrap flask-wtf
   ```

3. If some packages fail to install, you can try installing the core dependencies without version constraints:
   ```
   pip install flask flask-sqlalchemy flask-bootstrap
   pip install flask-wtf email-validator flask-login flask-session
   ```
5. Check Python version compatibility - this project works best with Python 3.8-3.10 due to the recent package versions used.

6. If all else fails, try creating a new requirements file with relaxed versions:
   ```
   pip install "flask>=2.0.0,<4.0.0" "flask-sqlalchemy>=2.5.0,<4.0.0" "flask-bootstrap>=3.3.7.0,<4.0.0" "flask-wtf>=1.0.0,<2.0.0" "email-validator>=1.0.0,<3.0.0"
   ```

7. Using `uv` as an alternative to `pip`:
   
   If you're experiencing issues with `pip` (slow performance, dependency conflicts, or installation failures), you can try using `uv`, a faster alternative:

   ```
   # First, install uv
   pip install uv
   
   # Then use uv to install requirements
   uv pip install -r requirements.txt
   ```

   `uv` offers improved speed and dependency resolution compared to standard `pip`. It's fully compatible with our requirements.txt file but processes dependencies much faster, which can help resolve installation issues on some systems.

## Project Structure

- **app.py**: Main application file with Flask setup and route registration
- **config.py**: Configuration settings for the application
- **models/**: Database models (User, Project, Comment, Interest)
- **routes/**: Application routes organized by feature (auth, project, profile, comment)
- **services/**: Business logic layer for separation of concerns
- **templates/**: Bootstrap-based HTML templates
- **static/**: CSS, JavaScript, and other static files

## Key Implementation Highlights

- **Clean Architecture**: Separation of concerns with models, routes, and services
- **Responsive Design**: Bootstrap-based responsive UI that works on various devices
- **Security Features**: Password hashing, CSRF protection, and session management
- **RESTful Routes**: Organized route structure following RESTful principles

## Future Development Plans

- Administrator dashboard for content moderation
- Enhanced security features
- Project categories and tags
- User notifications system
- Direct messaging between users

## Troubleshooting

### Common Issues

1. **Requirements installation problems**
   - The requirements.txt file includes very recent versions (Flask 3.1.0, SQLAlchemy 2.0.40)
   - Try using a fresh virtual environment: `python -m venv fresh_venv`
   - Install packages with relaxed version constraints (see Installation Troubleshooting)
   - Make sure your Python version is 3.8 or newer: `python --version`
   - Make sure pip is updated: `pip install --upgrade pip`

2. **Database errors on startup**
   - If you see errors about tables not existing:
     - Make sure db.create_all() in app.py is not commented out
   - If you see "already exists" errors:
     - Delete the instance/database.db file and retry: `rm instance/database.db`
     - Or delete the entire instance directory: `rm -rf instance/`

3. **Missing dependencies**
   - Run `pip install -r requirements.txt` to ensure all dependencies are installed
   - Check for any error messages during installation

4. **Page not found errors**
   - Verify the URL you're accessing
   - Check the routes defined in app.py and blueprint files

5. **Login issues**
   - Clear browser cookies
   - Reset your password if necessary
   - Check if your email/username is entered correctly

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Special thanks to all team members who contributed to this hackathon project and the organizers for the opportunity to create this platform.

## Contact

For questions or support, please open an issue on the GitHub repository.