from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from .routers import health, short_url

app = FastAPI()
app.include_router(health.router)
app.include_router(short_url.router)