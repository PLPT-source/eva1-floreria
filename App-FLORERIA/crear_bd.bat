@echo off
REM Crea la base de datos en MariaDB de XAMPP (XAMPP debe tener MySQL iniciado)
set MYSQL=C:\xampp\mysql\bin\mysql.exe
"%MYSQL%" -u root -e "CREATE DATABASE IF NOT EXISTS floreriadb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
if errorlevel 1 (echo ERROR: ¿esta MySQL iniciado en XAMPP? & exit /b 1)
echo Base de datos floreriadb lista.
