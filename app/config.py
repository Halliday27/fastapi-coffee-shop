from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Expense Tracker API"
    secret_key: str = "super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///./expense_tracker.db"


settings = Settings()
