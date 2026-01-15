# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

# calling templates
templates = Jinja2Templates(directory="templates")

# calling route 
@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
# index / Homepage
@app.get("/notes-get", response_model=list[schemas.Note_output])
def read_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

# App addfunction , reroute to homepage
@app.post("/notes-create", response_model=schemas.Note_output)
def create_note(note: schemas.NoteCreate_inherit_class, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

# # App delete-fx , refresh data from db, should be updated
# @app.post("/notes-delete", response_model=schemas.Note_output)
# def delete_note(note: schemas.NoteCreate_inherit_class, db: Session = Depends(get_db)):
#     return crud.delete_note(db, note)

# App delete-fx , refresh data from db, should be updated
@app.post("/notes-delete/{note_id}", response_model=schemas.Note_output)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    return crud.delete_note(db, note_id)