from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://cloudy:Saeyoung@fastapi.c0b28yg0kqqf.us-east-1.rds.amazonaws.com/user_api"
    SECRET_KEY: str = "chifuyu"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()