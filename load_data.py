import os
import sys
from django.core.wsgi import get_wsgi_application

# Определение абсолютного пути к текущей директории
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
application = get_wsgi_application()

from advertisement.utils import load_data_to_db

if __name__ == "__main__":
    file_name = "Занятость города 2023.xlsx"
    file_path = os.path.join(BASE_DIR, file_name)
    load_data_to_db(file_path)
