# bufunfa-back-end

**Trade following back-end**

## Run code

**Install a virtualenv:**

https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/

https://www.liquidweb.com/kb/how-to-install-pyenv-virtualenv-on-ubuntu-18-04/

````
pyenv install 3.8.8
pyenv virtuaenv 3.8.8 bufunfa
pyenv activate bufunfa

pip install -r requirements.txt

python main.py
````
**Testes:**

python -m pytest --verbose -rP tests/test_stock_repository.py
