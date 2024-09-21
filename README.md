# FastAPI Users POC

This is a proof of concept (POC) project that uses FastAPI to manage users, administrators, products, and transactions. It allows for the creation and authentication of users and administrators, as well as the management of products and transactions.

## Requirements

Make sure you have the following installed:

- [Python 3.9.0](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/lsofiadb/fast-api-users-poc.git
   
2. Create a virtual environment and activate it:
```bash
python -m venv env
  ```
```bash
.\env\Scripts\Activate      
  ```
```bash
deactivate
  ```
Install the dependencies:
```bash
pip install -r requirements.txt
  ```

### Running the Application
To run the application, use the following command:
```bash
uvicorn main:app --reload
  ```

This will start the server at http://127.0.0.1:8000

You can test the endpoints available [here!](https://documenter.getpostman.com/view/17256808/2sAXqtaM5g)
