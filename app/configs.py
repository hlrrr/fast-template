from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import false, true

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=('.env','env.prod'),
                                      env_file_encoding='utf-8',
                                      extra='allow',)
    DATABASE_URL: str
    # some_extra_value: str = 'extra'

settings = Settings() # type: ignore
# settings = Settings(_env_file='.env.prod', _env_file_encoding='utf-8')

print(settings)