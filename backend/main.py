from fastapi import FastAPI,  Depends
from sqlalchemy.orm import Session
from model.models import UserResponse
from database import SessionLocal, engine, UserModel, Base
from model.models import ResponseUserModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Create tables on startup
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CORS configuration
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/userSignUp/')
def user_signup(user: ResponseUserModel, db: Session = Depends(get_db)):
    created = False
    try:
        new_user = UserModel(**user.model_dump())
        db.add(new_user)
        db.commit()
        created = True
    except Exception as e:
        print(e)

    return {'userCreationSuccessfull':created}


@app.post('/userLogin')
def user_login():
    return {'username': 'amal', 'access': 'alsjfdlj28390823048', 'refresh': 'aslkfjdlasjdfjasdklfjaosdf', 'isSuperUser': True}


@app.get('/{id}')
def index(id: str):
    return {'data': f"Hello Amal {id}"}
