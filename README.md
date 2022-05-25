# FastAPI

------------------

## Getting Started

**Note** that this project requires `python >=3` for running project successfully.

(1) Clone repo locally with SSH:
```bash
$ cd ~
$ git clone https://github.com/dhruvang9083/FastAPIDemo.git
```

(2) Check if `pip` is installed:
```bash
$ pip --version

#If `pip` is not installed, follow steps below:
$ cd ~
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

(3) Install your local copy into a virtualenv. This is how you set up your repo for local run or development:
```
$ cd ~/FastAPI/
$ python3 -m pip install --user virtualenv
$ python3 -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

(4) When you're done with installation, you can run project:

```
uvicorn main:app --reload
```  

(5) Open API specification:

```
http://127.0.0.1:8000/docs
```  

## Directory Structure

```
├── src/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
├── .gitignore
├── README.md
├── requirements.txt
```
