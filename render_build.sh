#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Build Tailwind CSS (v4)
echo "Building Tailwind CSS..."
cd theme/static_src
npm install
npx tailwindcss -i ./src/styles.css -o ../static/css/dist/styles.css --minify
cd ../..

# Create static directory if it doesn't exist
mkdir -p static

python manage.py collectstatic --no-input
python manage.py migrate

# Handle Persistence on Render
if [ -n "$PERSISTENT_DATA_PATH" ]; then
    echo "Configuring persistence at $PERSISTENT_DATA_PATH..."
    mkdir -p "$PERSISTENT_DATA_PATH/media"
    
    # 1. Handle SQLite DB Seeding
    DB_TARGET="$PERSISTENT_DATA_PATH/db.sqlite3"
    if [ ! -f "$DB_TARGET" ] && [ -f "db.sqlite3" ]; then
        echo "Seeding persistent database from repository..."
        cp db.sqlite3 "$DB_TARGET"
    fi

    # 2. Handle Media Seeding (Logo, Page images)
    if [ -d "media" ]; then
        echo "Seeding persistent media from repository..."
        cp -rn media/* "$PERSISTENT_DATA_PATH/media/" || true
    fi
fi
