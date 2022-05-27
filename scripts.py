import django
import os
import argparse
from random import choice
from django.core.exceptions import ObjectDoesNotExist


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from datacenter.models import Commendation, Lesson, Schoolkid, Mark, Chastisement


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=choice([4, 5]))


def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def create_commendation(schoolkid, subject):
    praises = [
        'Хвалю',
        'Молодец',
        'Так держать',
        'Хорошо',
        'Умничка'
    ]
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
    ).order_by('?').first()

    Commendation.objects.create(
        text=choice(praises),
        teacher=lesson.teacher,
        subject=lesson.subject,
        schoolkid=schoolkid,
        created=lesson.date
    )


def check_name(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        print('Найденный ученик: {}, Год обучения: {}, Буква класса: {}'.format(
            schoolkid.full_name,
            schoolkid.year_of_study,
            schoolkid.group_letter
        ))

    except ObjectDoesNotExist:
        print('Имя не найдено.')
        quit()
    return schoolkid


def get_args():
    parser = argparse.ArgumentParser(description='Изменение оценок')
    parser.add_argument('name', help='ФИО ученика: "Фролов Иван Григорьевич" ')
    parser.add_argument('subject', help='Нужный предмет: "История", "Русский язык" и тд')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    schoolkid = check_name(args.name)
    print('Желаете продолжить? y/n')

    if input() == 'y':
        fix_marks(schoolkid)
        remove_chastisements(schoolkid)
        create_commendation(schoolkid, args.subject)
        print('Скрипт сработал')
