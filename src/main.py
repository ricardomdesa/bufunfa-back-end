import logging

from fastapi import Body, Depends, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm

from app_factory import app_factory
from controllers import (
    AuthenticationController,
    FetchCurrentStockPriceController,
    GetDashboardInfoController,
    GetInvestmentController,
    GetStockController,
    LoadInvestmentController,
    SignUpController,
    StockController,
)
from repositories import UserRepository

LOGGER = logging.getLogger(__name__)


app, login_manager = app_factory()


@login_manager.user_loader
def load_user(username: str):
    user = UserRepository().find_by_username(username)
    return user


@app.post("/login")
def login_token(data: OAuth2PasswordRequestForm = Depends()):
    controller = AuthenticationController(login_manager)
    return controller.authenticate_user(data.username, data.password)


@app.post("/load-stocks")
def load_stock(stock_file: UploadFile = File(...), username=Depends(login_manager)):
    controller = StockController()
    controller.set_username(username.username)
    return controller.load_stocks(stock_file.file)


@app.post("/load-investments")
def load_transactions(investment_file: UploadFile = File(...), username=Depends(login_manager)):
    controller = LoadInvestmentController()
    controller.set_username(username.username)
    return controller.load_investments(investment_file.file)


@app.post("/fetch-current-prices")
def fetch_current_prices(username=Depends(login_manager)):
    controller = FetchCurrentStockPriceController()
    controller.set_username(username.username)
    return controller.fetch_current_stock_price()


@app.post("/get-investments")
def get_investment(username=Depends(login_manager)):
    LOGGER.info("main get inv user -- " + username.username)
    controller = GetInvestmentController()
    controller.set_username(username.username)
    return controller.get_investments()


@app.post("/get-stocks")
def get_stocks(username=Depends(login_manager)):
    controller = GetStockController()
    controller.set_username(username.username)
    return controller.get_stocks()


@app.post("/get-dashboard-info")
def get_dashboard_info(username=Depends(login_manager)):
    controller = GetDashboardInfoController()
    controller.set_username(username.username)
    return controller.get_dashboard()


@app.post("/signup")
def signup(data: dict = Body(...)):
    controller = SignUpController()
    return controller.signup(data)
