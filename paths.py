import os.path
join = os.path.join

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


UPLOADS_FOLDER = 'uploads'
PUBLIC_FOLDER = join(ROOT_PATH, 'public')
COMPONENTS_FOLDER = join(PUBLIC_FOLDER, '_components')
UPLOADS_ABS_FOLDER = join(PUBLIC_FOLDER, UPLOADS_FOLDER)

BASE_PAGE = join(PUBLIC_FOLDER, 'base.html')
LOGIN_PAGE = '/login.html'
INDEX_PAGE = '/index.html'
PUBLICATION_PAGE = '/publication.html'
PROFILE_PAGE = '/profile.html'
CREATE_PUBLICATION = '/create_post.html'
EDIT_PUBLICATION = '/create_post.html'

LOGS_FOLDER = join(ROOT_PATH, "logs")
ERROR_PAGE = '/oops.html'