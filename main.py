from fastapi import FastAPI, File, UploadFile, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
import uvicorn
from environment import WEBAPP_URL, SECRET
from repositories.user_repository import UserRepository
from controllers.authentication_controller import AuthenticationController

app = FastAPI()

origins = {
    WEBAPP_URL
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "X-Content-Filename",
        "Content-Disposition",
        "application/x-www-form-urlencoded",
    ]
)

login_manager = LoginManager(SECRET, '/login')


@login_manager.user_loader
def load_user(username: str):
    user = UserRepository().find_by_username(username)
    return user


@app.post('/login')
def login_token(data: OAuth2PasswordRequestForm = Depends()):
    controller = AuthenticationController(login_manager)
    return controller.authenticate_user(data.username, data.password)


@app.post('/teste')
def teste_route(username = Depends(login_manager)):
    return {'teste rota': ''}


if __name__ == '__main__':
    print('Bufunfa Back-end')
    uvicorn.run("main:app", host="localhost", port=8001, reload=True)
    print(origins)

