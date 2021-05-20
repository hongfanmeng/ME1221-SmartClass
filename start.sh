#!/bin/bash
set -e

echo "Check Python installation..."
python3 --version

echo "Check virtual environment..."

if [ ! -d "venv" ]; then
  echo "Create virtual environment..."
  python3 -m venv venv
  echo "Activate virtual environment..."
  . venv/bin/activate
  echo "Install dependencies"
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
else
  echo "Activate virtual environment..."
  . venv/bin/activate
fi

python manage.py runserver 0:8000
