"""
FastAPI WebApp
"""
from fastapi import FastAPI
from youtube_ripper.version import __version__
from youtube_ripper.routers import example


web_app = FastAPI(title='youtube-ripper', version=__version__,
                  description='Youtube video and audio ripper API')
web_app.include_router(example.router)
