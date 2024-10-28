## Сайт ресторана с услугой онлайн-бронирования столиков

**Установка:**

1 - Клонирование репозитория 'gitclone (https://github.com/OldSumerian/Resraurant_Reservation_Service.git)'

2 - Установите необходимые зависимости, указанные в файле pyproject.toml ('poetry install')

3 - Заполнить данные в файле '.env' согласно списку из 'env.sample'

4 - Настройка базы данных, примените миграции для настройки базы данных: 'python manage.py migrate'

5 - Запуск сервера разработки: 'python manage.py runserver'

---

Для запуска файла в Docker необходимо ввести команду в терминал:

docker-compose up -d --build

---

Использованнный стек: Django, Bootstrap, Python, HTML, CSS, JS, PosgreSQL, ORM, MVP, Git, ORM, PEP8, Docker, Docker Compose, Permissions, Auth, Forms, Templates, FBV/CBV
