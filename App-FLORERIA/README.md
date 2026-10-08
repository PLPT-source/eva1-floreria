# 🌸 App Florería — Django + MySQL/MariaDB (XAMPP)
Evaluación Sumativa 02 · Programación Backend · Temática: **Florería** · Entidad: **Producto**

## 1. Preparar (todo desde CMD / terminal de VSCode)
1. Abrir **XAMPP Control Panel** → *Start* en **MySQL**.
2. Abrir la carpeta en VSCode (`code .`) y una terminal **Command Prompt**.
3. Ejecutar:
```
setup.bat
```
Esto hace: `python -m venv venv` → instala `requirements.txt` → crea la BD `floreriadb` → `makemigrations` + `migrate`.

Manual (equivalente):
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
crear_bd.bat
python manage.py makemigrations floreriaapp
python manage.py migrate
python manage.py runserver
```
Abrir http://127.0.0.1:8000/

> Si `pip install mysqlclient` falla: `pip install --upgrade pip` y reintentar (Python 3.12 trae wheel para Windows).

## 2. CRUD desde VSCode
**Web:** http://127.0.0.1:8000/productos/ (Crear, Ver, Editar, Eliminar).
**Base de datos (CMD):**
```
crud.bat                                              :: SELECT * (Read)
crud.bat "INSERT INTO floreriaapp_producto (nombre,categoria,descripcion,precio,stock,proveedor_email,disponible,fecha_ingreso) VALUES ('Orquídea','planta','Orquídea blanca',18000,4,'a@b.cl',1,CURDATE());"
crud.bat "UPDATE floreriaapp_producto SET precio=19000 WHERE nombre='Orquídea';"
crud.bat "DELETE FROM floreriaapp_producto WHERE nombre='Orquídea';"
```
Script completo: `C:\xampp\mysql\bin\mysql -u root floreriadb < crud_demo.sql`
También: `Ctrl+Shift+P` → *Tasks: Run Task* (setup, migrar, servidor, SELECT, tests) y `F5` para depurar.
Tests: `python manage.py test`.

## 3. Git / GitHub (CMD) — cada integrante con su branch
```
git init
git branch -M main
git add .
git commit -m "Proyecto Django base Floreria"
git remote add origin https://github.com/TU_USUARIO/App-FLORERIA.git
git push -u origin main
```
Cada integrante:
```
git config user.name "Tu Nombre"
git config user.email "tu_correo@gmail.com"
git checkout -b feature/tu-nombre
git add .
git commit -m "Descripción de tu aporte"
git push -u origin feature/tu-nombre
```
Luego *Pull Request* en GitHub y `git checkout main` + `git pull` para integrar.
Clonar en otro PC: `git clone <url>` → `setup.bat`.

## 4. Estructura
`floreria/` (settings, urls) · `floreriaapp/` (models, forms, views, urls, templates, migrations)
Validaciones: nombre ≥ 3 letras, precio > 0, stock ≥ 0, email válido, sin stock ⇒ no disponible.
