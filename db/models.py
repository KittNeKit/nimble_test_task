from sqlalchemy import Column, Integer, String

from db.engine import Base


class DBContacts(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), nullable=True)
