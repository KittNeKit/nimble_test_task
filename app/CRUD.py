from sqlalchemy import func
from sqlalchemy.orm import Session

from db import models


def get_contacts(
    db: Session,
    fulltext: str = "",
) -> list:
    combined_name = func.concat(
        models.DBContacts.first_name,
        " ",
        models.DBContacts.last_name,
        " ",
        models.DBContacts.email,
    )

    return (
        db.query(models.DBContacts).filter(combined_name.icontains(f"{fulltext}")).all()
    )
