# Portfolio Website - Django Project

## Overview
This project is a Django-based portfolio website that showcases internship experiences and portfolio items. It includes user authentication to restrict access to content, ensuring that only authenticated users can view detailed portfolio and internship information.

## Live Website

The portfolio website is now accessible online at:
**[GamingWithToimen.pythonanywhere.com](https://GamingWithToimen.pythonanywhere.com)**

Feel free to visit the live site to see the project in action!

## Features

- **Responsive Design**: Works on mobile, tablet, and desktop devices
- **User Authentication**: 
  - Login/Registration system
  - Protected content for authenticated users only
  - Home page is publicly accessible
- **Portfolio Showcase**: Grid-based display of portfolio projects
- **Internship Documentation**: Organized documentation of internship experiences
- **Django Framework**: Leverages Django for robust backend functionality

## Technical Changes

This project has been converted from a static HTML5 site to a dynamic Django web application. Key changes include:

- **Django Architecture**: Implemented proper Django project structure with apps
- **Template System**: Converted static HTML to Django templates with inheritance
- **Authentication**: Added user registration and login functionality
- **Static Files**: Reorganized CSS, JS, and images to follow Django conventions
- **URL Routing**: Implemented Django URL patterns for better navigation
- **Security**: Protected routes with login_required decorators
- **Deployment**: Successfully deployed to PythonAnywhere hosting platform

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kw1c-VervoortTijme/portfolio-website.git
   cd portfolio-website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - Visit the live site at [GamingWithToimen.pythonanywhere.com](https://GamingWithToimen.pythonanywhere.com)
   - Or access your local development server at http://127.0.0.1:8000/
   - Login with the superuser account or register a new account

## Project Structure

```
portfolio_project/
├── portfolio/                 # Main Django app
│   ├── static/
│   │   └── portfolio/         # Static files (CSS, images)
│   │       ├── css/
│   │       ├── images/
│   │       └── bootstrap-icons/
│   ├── templates/
│   │   └── portfolio/         # HTML templates
│   │       ├── base.html      # Base template with header/footer
│   │       ├── index.html     # Home page
│   │       ├── login.html     # Login page
│   │       ├── register.html  # Registration page
│   │       ├── portfolio_page.html
│   │       ├── stage_1.html   # Internship pages
│   │       ├── stage_2.html
│   ├── forms.py               # User registration form
│   ├── views.py               # View functions
│   └── urls.py                # App URL patterns
├── portfolio_project/         # Project configuration
│   ├── settings.py
│   └── urls.py                # Project URL patterns
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Technologies Used

- **Django**: Web framework for Python
- **Bootstrap**: Frontend framework for responsive design
- **JavaScript**: For interactive elements
- **HTML5/CSS3**: Standard web technologies
- **SQLite**: Database (default for development)
- **PythonAnywhere**: Hosting platform for the live site

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## User Guide

- **Home Page**: Publicly accessible
- **Login/Register**: Create an account or sign in
- **Internship Pages**: View details of internship experiences (requires login)
- **Portfolio**: View portfolio projects and descriptions (requires login)

## License

This project is for educational purposes. All rights reserved.
