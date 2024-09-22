from dotenv import load_dotenv

# Load environment variables from .env file
import logging

logger = logging.getLogger(__name__)
logger.info("loading env var from .env file...")
load_dotenv(dotenv_path=".env")
