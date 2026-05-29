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
python manage.py migrate --no-input
