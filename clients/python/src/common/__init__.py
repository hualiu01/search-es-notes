from dotenv import load_dotenv

# Load environment variables from .env file
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("loading env var from .env file...")
load_dotenv(dotenv_path=".env")
