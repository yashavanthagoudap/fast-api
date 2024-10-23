from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    replicate_api_token: str

    class Config:
        env_file = ".env"  # Make sure .env file is correctly configured

settings = Settings()
