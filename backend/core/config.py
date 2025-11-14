from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tech Blog API"
    PROJECT_VERSION: str = "1.0.0"
    
    class Config:
        case_sensitive = True


settings = Settings()
