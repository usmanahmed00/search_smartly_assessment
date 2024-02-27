from django.core.management.base import BaseCommand
from poi.models import PointOfInterest
from poi.utils import process_files_helper
import os


class Command(BaseCommand):
    help = 'Import PoI data from files'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory to file(s)')

    def handle(self, *args, **options):
        files_directory = options['directory']
        for file_path in os.listdir(files_directory):
            poi_data = process_files_helper.process_files(os.path.join(files_directory, file_path))
            obj_list = [PointOfInterest(**data_dict) for data_dict in poi_data]
            if obj_list:
                objs = PointOfInterest.objects.bulk_create(obj_list)


