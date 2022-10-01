## Инструкция к запуску

1. Необходимо установить себе `docker` и `docker-compose`\
На разных системах это делается по разному:
* Linux: https://docs.docker.com/desktop/install/linux-install/
* Ubuntu: https://docs.docker.com/desktop/install/ubuntu/
* Windows: https://docs.docker.com/desktop/install/windows-install/

2. С корневой папки выполнить команду `docker compose up`

3. Дождаться загрузки всех библиотек, загрузки датасета, инициализации всех служб

### Как открыть jupyter
- Перейти по адресу http://localhost:8888
- Ввести пароль `docker`

### Как открыть swagger
- Перейти по адресу http://localhost:8000/docs

## Заметки
Папки `backend`, `saved_notebooks` и `datasets` являются **volumes** \
Это значит, что они используются и контейнером и системой-хостом \
Так же это означает то, что изменения этих папок в контейнере затрагивают и такие же папки в репозитории \

Если бд долго не загружется, то это может означать, что файлы с гугл диса не подгрузились до конца. Вариант решения - скачать вручную и положить в папку datasets\
