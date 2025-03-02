import os

from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
full_path = os.path.join(BASE_DIR, ".env")
normal_path = os.path.normpath(full_path)

env = load_dotenv(normal_path)
API_KEY = os.getenv('API_KEY')
FOLDER_ID = os.getenv('FOLDER_ID')
