from .models import Note
from . import db

def create_note(title, content):
    note = Note(title=title, content=content)
    db.session.add(note)
    db.session.commit()
    return note

def get_all_notes():
    return Note.query.all()
