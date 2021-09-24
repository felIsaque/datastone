#!/bin/bash
# Use this script to test if a given TCP host/port are available

echo "================================="
echo "Inicializando o banco de dados..."
echo "================================="

while :
do
    curl http://datastone:123456@data_stone_db:5432
    db_up="$?"

    if [ $db_up -eq 52 ]
    then
        echo "postgres inicializado"
        break
    fi

    echo "esperando pelo postgres..."
    sleep 1
done

while ! python manage.py makemigrations 2>&1; do
    echo "makemigrations está sendo executado"
    sleep 2
done

while ! python manage.py migrate 2>&1; do
    echo "migrate está sendo executado"
    sleep 3
done

if [ "$DEB" == "FALSE" ]
then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn --bind 0.0.0.0:8000 app.wsgi
fi
