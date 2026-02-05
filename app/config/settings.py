import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

OMIE_BASE_URL = os.getenv("OMIE_BASE_URL")

with open(os.path.join(BASE_DIR, "locais.json"), encoding="utf-8") as f:
    LOCAIS = json.load(f)