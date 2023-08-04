import requests
from celery import Celery
from celery.schedules import crontab

from db.engine import SessionLocal
from db import models
from app.CRUD import get_contacts


app = Celery("tasks", backend="redis://localhost", broker="redis://localhost")
URL = "https://api.nimble.com/api/v1/contacts/"
db = SessionLocal()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="0", hour="0"), save_contacts.s(), name="update contacts"
    )


def scrape_contacts():
    data = requests.get(
        URL, headers={"Authorization": "Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu"}
    ).json()
    users = []
    for info in data["resources"]:
        if info["record_type"] == "person":
            try:
                email = info["fields"]["email"][0]["value"]
            except KeyError:
                email = None

            users.append(
                {
                    "first_name": info["fields"]["first name"][0]["value"],
                    "last_name": info["fields"]["last name"][0]["value"],
                    "email": email,
                }
            )
    return users


@app.task
def save_contacts():
    for contact in scrape_contacts():
        db_contacts = models.DBContacts(
            first_name=contact["first_name"],
            last_name=contact["last_name"],
            email=contact["email"],
        )
        in_db = False
        for users in get_contacts(db):
            if (
                users.first_name == db_contacts.first_name
                and users.last_name == db_contacts.last_name
                and users.email == db_contacts.email
            ):
                in_db = True
                break

        if not in_db:
            db.add(db_contacts)
            db.commit()
            db.refresh(db_contacts)
