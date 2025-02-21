como clonar y usar repositorio:
Abre una terminal y ejecuta:

git clone https://github.com/villarinocarlos/testeo1.git
y despues: cd testeo1
despues crea un entorno virtual: 
# En macOS / Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
Despues instala las dependencias:
pip install -r requirements.txt
despues haz las migraciones y corre el servidor: 
python manage.py migrate
python manage.py runserver
Abre el navegador y ve a localhost:8000 y simplemente abre el programa
favor de tener cuidado con la base de dato ya que obviamente esta abierta y no se necesita hacer nada
