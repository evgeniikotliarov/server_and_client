import os.path
join = os.path.join

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

INDEX_PAGE = '/index.html'

PUBLIC_FOLDER = join(ROOT_PATH, 'public')

IMAGES_FOLDER = 'image'
ABS_IMAGES_FOLDER = join(PUBLIC_FOLDER, IMAGES_FOLDER)

LOGS_FOLDER = join(ROOT_PATH, 'logs')
