# Orange Portal Project

A Django-based web application featuring interactive 3D portals, animations, and visual effects.

## Description
This project creates an immersive web experience with 3D portals and animations.

## Features
- 3D Portal transitions
- Interactive bunny animations
- Rain effects
- Universe exploration
- Lock mechanism
- etc...

## Docker Setup
1. Clone the repository:
```
git clone https://github.com/W-Mirshod/orange.git
```

2. Build and run with Docker:
```
docker build -t orange .
docker run -d -p 1407:1407 orange
```

3. Access the application:
Open your browser and navigate to `http://host:1407`

## Development Setup
1. Create and activate virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install requirements:
```
pip install -r requirements.txt
```

3. Run migrations:
```
python manage.py migrate
```

4. Start development server:
```
python manage.py runserver 1407
```

## Technologies
- Python 3.10
- Django
- Docker
- HTML5
- CSS3
- JavaScript
- Three.js
- WebGL
- Nginx
- Gunicorn
- PostgreSQL
