# DZImage
- Приложение на основе Django и Django REST framework, позволяющее загружать изображения с компьютера пользователя.
- Изображения загружаются путем перетаскивания на специальную "dropbox зону".
- Во время загрузки, уменьшается размер изображения в 2 раза и меняется угол наклона на 45 градусов.
- Максимальный размер файлов - 2 MB.
- Поддерживаемые форматы файлов: .jpg,.jpeg,.JPEG,.JPG,.png,.PNG

**Проверить работу приложения можно по ссылке:**
http://sergeipogorelov.pythonanywhere.com/

# Установка
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

**Перед тем, как начать:**
Если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`.
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

### Запуск проекта (на примере Linux)
- Создайте на своем компьютере папку проекта `mkdir dz_image` и перейдите в нее `cd dz_image`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/SergePogorelov/dz_image.git .`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Накатите миграции `python manage.py migrate`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`

## В разработке использованы

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Dropzone](https://www.dropzone.dev/js/)
