# Nimble Backend contacts

## Technologies:
- FastAPI
- Celery
- SQLAlchemy
- Alembic

## Features:
- Updating the contact database once a day
- Using the Nimble API to update the contact database
- Finding users by searching by Name, Surname or email
- Documentation is located at /docs/

## Installing using GitHub:

1. Clone the repository:

```bash
git clone https://github.com/your-username/nimble_test_task
```
2. Change to the project's directory:
```bash
cd nimble_test_task
```
3. Сopy .env_sample file with your examples of env variables to your .env
file.

Also enter you DB URL into alembic.ini sqlalchemy.url

```
sqlalchemy.url = postgresql://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HOST/postgres
```
4. Once you're in the desired directory, run the following command to create a virtual environment:
```bash
python -m venv venv
```
5. Activate the virtual environment:

On macOS and Linux:

```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```
5. Set up the database:

Run the migrations

```bash
alembic upgrade head
```

6. Start the development server

```bash
 uvicorn app.main:app --reload
```

7. Access the website locally at http://localhost:8000.

8. Run celery to update the database daily
```bash
celery -A tasks:app worker -l info
```
```bash
celery -A tasks beat
```