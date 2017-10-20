# Python Hacking - special edition

Instalowanie zależności (zakładając że mamy zainstlowanego pythona3

Linux:

```
python3 -m venv ~/ph_venv/
source ~/ph_venv/bin/activate
pip install -r requirements.txt
```

Windows:

```
python3 -m venv ph_venv
\ph_venv\bin\activate.bat
pip install -r requirements.txt
```


## Server http do serwowania plików

```
python3 -m http.server 8080
```

## Pobranie zawartości strony google.pl

```
python3 save_google.py
```

## Prosta strona internetowa

```
python3 website.py
```

## Baza danych

### Stworzenie bazy danych

```
python3 db.py
```

### Dodanie danych do bazy danych

```
python3 db_add.py
```

### Wyslistowanie danych z bazy danych

```
python3 db_list.py
```


### Okienko z progress bar

```
python3 tk.py
```


# Materiały:


Python:
https://www.python.org/

PyCharm:
https://www.jetbrains.com/pycharm/

Python - podstawy
https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

Tkinter:
http://www.tkdocs.com/tutorial/
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

Requests
http://docs.python-requests.org/en/master/

Flask
http://flask.pocoo.org/

SQLAlchemy
http://docs.sqlalchemy.org/en/rel_1_1/