import csv
import os
import urllib.request



from django.core.management.base import BaseCommand

from main import settings
from phones.models import Phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                self.download_image(line[1], line[2])
                p = Phones(id=line[0], name=line[1], price=line[3], image=f'image_phone/{line[1]}.jpeg', release_date=line[4],
                           lte_exists=line[5],
                           slug=line[1].replace(' ', '_'))
                p.save()

    def download_image(self, name_image, url_image, folder='/image_phone'):
        '''
        the function downloads images from a link
        :param name: type str
        :param url: link
        :param folder: a folder where is downloaded images, default '/static/image_phone/'
        :return: None
        '''
        try:
            os.mkdir(settings.STATICFILES_DIRS[0] + f'{folder}')
        except Exception as error_info:
            print(error_info)


        os.chdir(os.path.join(settings.STATICFILES_DIRS[0] + f'{folder}'))
        urllib.request.urlretrieve(url_image, f'{name_image}.jpeg')
