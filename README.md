# course_project_9

## Описание

Данный репозиторий представляет собой сервис по распознаваниб лиц, написанный в рамках курсового проекта по дисциплине "Защита в операционных системах"

Данный сервис умеет находить лица на изображении и:
- Добавлять их в базу данных
- Удалять из базы данных
- Сравнивать с имеющимися в базе данных

## Запуск

1. Склонировать репозиторий
1. Перейти в корень репозитория
1. Собрать docker image
    `docker build -t facer_image .`
1. Запустить docker container
    `docker run -d --name facer -v "$(pwd)"/db:/db -p 8000:8000 facer_image`

Через непродолжительное время (при старте ему необходимо скачать веса модели ~80 Мб) сервис будет доступен по адресу `http://0.0.0.0:8000/`. 
Интерактивная документация доступна по адресу `http://0.0.0.0:8000/docs`

Для остановки сервиса используйте:
`docker stop facer`

Для последующего запуска используйте:
`docker start facer`

## База данных

Файл базы данных появится в корне проекта по пути `<project_root>/db/database.db`

При последующих запусках командой start он будет переиспользован, и данные не потеряются

## Технологический стек

Использованы следующие технологии:
- python
- pytorch
- fastapi
- sqlite

## Нейросети

Используется классический стек из MTCNN и Face2Vec, взятых из [facenet_pytorch](https://github.com/timesler/facenet-pytorch)