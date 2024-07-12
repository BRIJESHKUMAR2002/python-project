#!/bin/bash

brew install libreoffice
python3.10 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt
# Set environment variables (if needed)
export FLASK_APP=app.py
export FLASK_ENV=development

# Run your Flask application
flask run
