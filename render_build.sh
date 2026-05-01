#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static

# Rebuild Tailwind CSS if needed (assumes node/npx is available)
# cd theme/static_src && npx tailwindcss -i src/styles.css -o ../static/css/dist/styles.css && cd ../../

python manage.py collectstatic --no-input
python manage.py migrate

# Handle SQLite persistence on Render
if [ -n "$DB_PATH" ]; then
    DB_DIR=$(dirname "$DB_PATH")
    mkdir -p "$DB_DIR"
    
    # If DB doesn't exist on persistent volume, seed it from the repo version
    if [ ! -f "$DB_PATH" ] && [ -f "db.sqlite3" ]; then
        echo "Seeding persistent database from repository..."
        cp db.sqlite3 "$DB_PATH"
    fi
fi
