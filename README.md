# db-hack

Проект создан для учебного процесса и не является полноценным.

## Как начать

1. ![Python 3.x](https://img.shields.io/pypi/pyversions/vk_api.svg) должен быть установлен.

2. Скачайте ['scripts.py'](https://github.com/ruk228/db-hack), [БД](https://dvmn.org/filer/canonical/1562234129/166/), [Онлайн реподзиторий](https://github.com/devmanorg/e-diary/tree/master)

3. Распакуйте файлы и закиньте их в одну папку.

4. Зайдите в консоль и перейдите в каталог с файлом 'scripts.py'

* Пример:
```bash
$ cd путь до файла/
```
```bash
$ cd git-hub/db-hack
```

5. разверните виртуальное окружение

```bsh
virtualenv -p python3 venv
. venv/bin/activate
```

6. Установите зависимости


```bash
pip install -r requirements.txt
```

7. Запустите скрипт

* Пример:
```bash
$ python scripts.py "Имя ученика" "Название предмета"
```
```bash
$ python scripts.py "Фролов Иван Григорьевич" "Русский язык"
```
##### Ты увидишь:
```bash
$ Найденный ученик: Фролов Иван Григорьевич, Год обучения: 6, Буква класса: А
Желаете продолжить? y/n
```
Если это желаемые данные ученика, то введите 'y', а если это не те данные, то нажмите n и попробуйте еще раз запустить скрипт(шаг 5).

Если вы нажали 'y' и появилась надпись 'Скрипт сработал', то вы сделали все правильно.
```bash
$ y
$ Скрипт сработал
```

8. Запустите электронный дневник


```bash
python manage.py runserver
```

10. Зайдите в электронный дневник и првоерьте оценки.

### Ошибки в консоле

* `Имя не найдено.`

Причина: Введенного вами ФИО нет в БД или введено неполное имя.

Исправление: Проверьте правильность написания имени.

* `it returned num!`

Причина: Много результатов с вашим ФИО.

Исправление: Введите полное ФИО человека, а не частичное.

* `scripts.py: error: the following arguments are required: name, subject`

Причина: Вы не ввели ФИО ученика или предмет

Исправление: Введите ФИО ученика и предмет

* `scripts.py: command not found`

Причина: команда введена неверно

Исправление: перед командой введите `python` или `python3`

* `Error: That port is already in use.`

Причина: порт уже используется

Исправление: Введите в консоле
```bash
sudo lsof -t -i tcp:8000 | xargs kill -9
```
