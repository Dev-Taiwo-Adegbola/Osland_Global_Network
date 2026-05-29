#!/usr/bin/env bash
# Runtime startup script for Osland Global Network on Render

# exit on error
set -o errexit

# Handle Persistence on Render at Runtime
if [ -n "$PERSISTENT_DATA_PATH" ]; then
    echo "Configuring persistent volume at $PERSISTENT_DATA_PATH..."
    
    # Create media directory if it doesn't exist on the volume
    mkdir -p "$PERSISTENT_DATA_PATH/media"
    
    # 1. Handle SQLite DB Seeding
    # If the database doesn't exist on the persistent volume, copy the initial one from the repo
    DB_TARGET="$PERSISTENT_DATA_PATH/db.sqlite3"
    if [ ! -f "$DB_TARGET" ]; then
        if [ -f "db.sqlite3" ]; then
            echo "Initializing persistent database from repository..."
            cp db.sqlite3 "$DB_TARGET"
        else
            echo "Warning: No initial database found to seed."
        fi
    else
        echo "Persistent database already exists. Skipping initialization."
    fi

    # 2. Handle Media Seeding (Logo, Placeholders, etc.)
    # Copy missing assets from the repository to the persistent volume
    if [ -d "media" ]; then
        echo "Updating persistent media assets from repository (non-destructive)..."
        cp -rn media/* "$PERSISTENT_DATA_PATH/media/" || true
    fi
fi

# Final check: Ensure we are up to date and static is collected (redundant but safe)
python manage.py migrate --no-input

# Start the application
echo "Starting Gunicorn..."
gunicorn osland.wsgi:application
