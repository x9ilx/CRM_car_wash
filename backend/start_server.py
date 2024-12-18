import os
import subprocess
import sys
import time


def run_command(command):
    try:
        print(f'Executing: {command}')
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')
        sys.exit(1)


time.sleep(10)
print('------------------------------------------------')
print('START MIGRATIONS')
print('------------------------------------------------')
run_command('python manage.py showmigrations')
run_command('python manage.py makemigrations')
run_command('python manage.py migrate')
print('------------------------------------------------')
print('END MIGRATION')
print('------------------------------------------------')

print('------------------------------------------------')
print('START COLLECT STATIC')
print('------------------------------------------------')
run_command('python manage.py collectstatic --noinput')
run_command('cp -r /app/collected_static/. /static/static/')
print('------------------------------------------------')
print('END COLLECT STATIC')
print('------------------------------------------------')

print('------------------------------------------------')
print('START LOAD BASE DATA')
print('------------------------------------------------')
run_command('python manage.py loadbasedata')
print('------------------------------------------------')
print('END LOAD BASE DATA')
print('------------------------------------------------')

print('------------------------------------------------')
print('RUN SERVER')
print('------------------------------------------------')
run_command('gunicorn --bind 0.0.0.0:8000 backend.wsgi')