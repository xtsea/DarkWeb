try:
    from DarkWeb.database.SQL import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String
from sqlalchemy import Column, Integer, String, Text

class Note(BASE):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    keyword = Column(String(128))
    text = Column(Text)

    def __init__(self, chat_id, keyword, text):
        self.chat_id = chat_id
        self.keyword = keyword
        self.text = text

def add_note(chat_id, keyword, text):
    new_note = Note(chat_id, keyword, text)
    SESSION.add(new_note)
    SESSION.commit()
    SESSION.close()

def get_note_text(chat_id, keyword):
    try:
        note = SESSION.query(Note).filter_by(chat_id=chat_id, keyword=keyword).first()
        if note:
            return note.text
        else:
            return None
    finally:
        SESSION.close()

def delete_note(chat_id, keyword):
    try:
        note = SESSION.query(Note).filter_by(chat_id=chat_id, keyword=keyword).first()
        if note:
            SESSION.delete(note)
            SESSION.commit()
            return True
        else:
            return False
    finally:
        SESSION.close()
