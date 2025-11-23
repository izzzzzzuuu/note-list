# app/schemas.py
from pydantic import BaseModel

class NoteBase(BaseModel):
    text: str

class NoteCreate_inherit_class(NoteBase):
    pass

class Note_output(NoteBase):
    id: int

    model_config = {
        "from_attributes": True  # Use this instead of orm_mode=True
    }
