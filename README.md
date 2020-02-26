# Connectary

## Setup development environment

Create an python virtual environment.
```
python3 -m pip install virtualenv
python3 -m virtualenv .venv
```

Activate the virtual environment.

On Windows:
```
\.venv\Scripts\activate.bat
```

On Linux:
```
source ./.venv/bin/activate
```

And then install dependencies:
```
pip install -r requirements.txt
```

## Run Project

Start the development server.
```
python manage.py runserver 0:8000
```