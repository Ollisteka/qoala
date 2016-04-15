from django.core.management import BaseCommand
from quests.models import Quest
from os.path import dirname, join, exists, isdir
from os import symlink, makedirs, listdir
from django.conf import settings
import shutil

__author__ = 'Last G'


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        for task in Quest.objects.all():
            print("Collectiong static files for {}".format(task.shortname))
            staticdir = join(dirname(task.provider_file), 'static')
            if exists(staticdir) and isdir(staticdir):
                prefix = task.get_hashkey
                dst = join(settings.STATIC_ROOT, 'taskstatic', str(task.id), prefix)
                if exists(dst):
                    print("Removing old static files at {}".format(dst))
                    shutil.rmtree(dst)

                print("Coping files")
                #shutil.copytree(staticdir, dst)
                if not exists(dst):
                    makedirs(dst)
                print staticdir, '->', dst
                for inner_file in listdir(staticdir):
                    symlink(join(staticdir, inner_file), join(dst, inner_file))
            else:
                print("Have  no static files")


