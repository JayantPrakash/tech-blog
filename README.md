# tech-blog
A real world blog built with fastapi



## Technology Stack:
* FastAPI
* Uvicorn
* Pytest
* Sqlalchemy
* Postgres


## How to start the app ?
```
python -m venv env   #create a virtual environment
.\env\Scripts\activate  #activate your windows virtual environment (Linux/Mac: source env/bin/activate)
cd .\backend\
pip install -r .\requirements.txt
uvicorn main:app --reload     #start server
visit  127.0.0.1:8000/
```

Features:
 -   Connecting to Database
 -   Migration by alembic
 -   Schemas
 -   Dependency Injection
 -   Password Hashing
 -   Unit Testing (What makes an app stable)
 -   Authentication login/create user/get token
 -   Authorization/Permissions

 --------------------------------- Intermediate Stuffs --------------------------------
 -  Caching
 -  Deployment on Linux Server
 -  Webapp (Monolithic)

 --------------------------------- Advanced Stuffs ------------------------------------
 - 🚧 Load Testing
 - 🚧 Fully Asyc
 - 🚧 Dockerization
 - 🚧 Creating a frontend using React
 - 🚧 CI and CD