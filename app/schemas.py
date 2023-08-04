from pydantic import BaseModel


class ContactsBase(BaseModel):
    first_name: str
    last_name: str
    email: str | None = None
