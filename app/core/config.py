from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Amharic POS Tagger API"
    MODEL_PATH: str = "tuned_crf_pos_tagger.pkl"
    RATE_LIMIT: str = "20/minute"

    class Config:
        env_file = ".env"

settings = Settings()
