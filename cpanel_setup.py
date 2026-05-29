import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def main():
    print("Osland Global Network - cPanel Setup Helper")
    print("------------------------------------------")
    
    # 1. Install requirements
    print("\n1. Installing requirements...")
    run_command("pip install -r requirements.txt")
    
    # 2. Run migrations
    print("\n2. Running database migrations...")
    run_command("python manage.py migrate")
    
    # 3. Collect static files
    print("\n3. Collecting static files...")
    run_command("python manage.py collectstatic --noinput")
    
    print("\nSetup complete! Remember to restart your Python app in cPanel.")

if __name__ == "__main__":
    main()
