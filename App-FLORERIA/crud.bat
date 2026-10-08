@echo off
REM CRUD directo en MariaDB desde CMD / terminal de VSCode (nivel BD).
REM Uso:  crud.bat "SELECT * FROM floreriaapp_producto;"
set MYSQL=C:\xampp\mysql\bin\mysql.exe
if "%~1"=="" (
  "%MYSQL%" -u root floreriadb -t -e "SELECT * FROM floreriaapp_producto;"
) else (
  "%MYSQL%" -u root floreriadb -t -e "%~1"
)
