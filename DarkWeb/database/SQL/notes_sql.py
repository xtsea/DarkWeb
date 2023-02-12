from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from DarkWeb.database.SQL import BASE, SESSION
from config import DB_URL

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

Session = sessionmaker(bind=engine)
SESSION = Session()

def add_note(chat_id, keyword, text):
    with SESSION as session:
        new_note = Note(chat_id, keyword, text)
        session.add(new_note)
        session.commit()

def get_note_text(chat_id, keyword):
    with SESSION as session:
        note = session.query(Note).filter_by(chat_id=chat_id, keyword=keyword).first()
        if note:
            return note.text
        else:
            return None

def delete_note(chat_id, keyword):
    with SESSION as session:
        note = session.query(Note).filter_by(chat_id=chat_id, keyword=keyword).first()
        if note:
            session.delete(note)
            session.commit()
            return True
        else:
            return False
