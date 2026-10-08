@echo off
REM Prepara todo desde CMD: venv + dependencias + BD + migraciones
cd /d "%~dp0"
if not exist venv (python -m venv venv)
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
call crear_bd.bat
python manage.py makemigrations floreriaapp
python manage.py migrate
echo.
echo Listo. Ejecuta:  venv\Scripts\activate  y luego  python manage.py runserver
