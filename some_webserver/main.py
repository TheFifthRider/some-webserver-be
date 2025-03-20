from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy import create_engine

from some_webserver.models.persistence import Base
from some_webserver.routes import router


app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost:5173",
    "http://localhost:8000"
]

engine = create_engine('sqlite:///database.db')
app.add_middleware(DBSessionMiddleware, custom_engine=engine, commit_on_exit=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}
