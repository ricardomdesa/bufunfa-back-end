import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager

from controllers.get_investments_controller import GetInvestmentController
from controllers.get_stock_controller import GetStockController
from controllers.signup_controller import SignUpController
from environment import WEBAPP_URL, SECRET
from repositories.user_repository import UserRepository
from controllers.authentication_controller import AuthenticationController
from controllers.stock_controller import StockController
from controllers.load_investment_controller import LoadInvestmentController
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


@app.post('/load-investments')
def load_transactions(investment_file: UploadFile = File(...), username=Depends(login_manager)):
    controller = LoadInvestmentController(username.username)
    return controller.load_investments(investment_file.file)


@app.post('/fetch-current-prices')
def fetch_current_prices(username=Depends(login_manager)):
    controller = FetchCurrentStockPriceController(username.username)
    return controller.fetch_current_stock_price()


@app.post('/get-investments')
def get_investment(username=Depends(login_manager)):
    controller = GetInvestmentController(username.username)
    return controller.get_investments()


@app.post('/get-stocks')
def get_stocks(username=Depends(login_manager)):
    controller = GetStockController(username.username)
    return controller.get_stocks()


@app.post('/signup')
def signup(data: dict = Body(...)):
    controller = SignUpController()
    return controller.signup(data)


# if __name__ == '__main__':
#     uvicorn.run("main:app", host="localhost", port=8002, reload=True)

