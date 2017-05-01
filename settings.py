import os.path

ROOT_PATH = os.path.dirname(os.path.abspath(__file__)).encode()
PUBLIC_FOLDER = os.path.join(ROOT_PATH, b'public')