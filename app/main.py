from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import schemas, CRUD
from db.engine import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/contacts/", response_model=list[schemas.ContactsBase])
def read_contacts(query: str = "", db: Session = Depends(get_db)):
    contacts = CRUD.get_contacts(db, query)
    return contacts
