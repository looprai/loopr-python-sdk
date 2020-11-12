import sys

from dotenv import load_dotenv
from loguru import logger

load_dotenv()
fmt = "{time} - {name} - {level} - {message}"
logger.configure(handlers=[{"sink": sys.stdout, "level": "WARNING", "format": fmt}])
_LOOPR_API_KEY = "LOOPR_API_KEY"
_LOOPR_API_ENDPOINT = "LOOPR_API_ENDPOINT"
DEFAULT_API_ENDPOINT = "https://api.loopr.ai/"
