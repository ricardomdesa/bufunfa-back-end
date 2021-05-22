import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from environment import WEBAPP_URL, SECRET
from repositories.user_repository import UserRepository
from controllers.authentication_controller import AuthenticationController
from controllers.stock_controller import StockController
from controllers.transaction_controller import TransactionController
from controllers.fetch_current_stock_price_controller import FetchCurrentStockPriceController

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


@app.post('/load-stocks')
def load_stock(stock_file: UploadFile = File(...), username=Depends(login_manager)):
    controller = StockController(username.username)
    return controller.load_stocks(stock_file.file)


@app.post('/load-transactions')
def load_transactions(cart_file: UploadFile = File(...), username=Depends(login_manager)):
    controller = TransactionController(username.username)
    return controller.load_transactions(cart_file.file)


@app.post('/fetch-current-prices')
def fetch_current_prices(username=Depends(login_manager)):
    controller = FetchCurrentStockPriceController(username.username)
    return controller.fetch_current_stock_price()


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8001, reload=True)

