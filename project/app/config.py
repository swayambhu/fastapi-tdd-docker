import logging,  os
from dotenv import load_dotenv
from pydantic import BaseSettings
from functools import lru_cache

load_dotenv()

log = logging.getLogger(os.getenv("SERVER"))

class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    TESTING: bool = bool(os.getenv("TESTING"))
    
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()