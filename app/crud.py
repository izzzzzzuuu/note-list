# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_notes(db: Session):
    return db.query(models.Note).all()

def create_note(db: Session, note: schemas.NoteCreate_inherit_class):
    db_note = models.Note(text=note.text)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
