from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine

from some_webserver.models.persistence import Base
from some_webserver.routes import router

class Settings(BaseSettings):
    origins: list[str] = ["http://localhost:5173", "http://localhost:8000"]
    db_url: str = "sqlite:///database.db"
    commit_on_exit: bool = True


def initialize(override_settings: Settings | None = None) -> tuple[FastAPI, Settings]:
    _settings = override_settings or Settings()
    _app = FastAPI()

    _app.include_router(router)

    engine = create_engine(_settings.db_url)
    _app.add_middleware(DBSessionMiddleware, custom_engine=engine, commit_on_exit=_settings.commit_on_exit)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=_settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    with engine.begin():
        Base.metadata.create_all(engine)

    return (_app, _settings)


app, settings = initialize()
