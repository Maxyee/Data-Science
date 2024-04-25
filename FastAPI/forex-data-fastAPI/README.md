1. check the python version 
- python -V
2. create a virtual environment
- python -m venv env
3. create a file called `requirements.txt`
- touch requirements.txt
4. mention all the needed libraries into the txt file
5. now we need to activate the virtual environment by typing in git bash
- source ./env/Scripts/activate
6. after activating the virtual environment we need to run the requirements file
- pip install -r requirements.txt
7. now we have to create a `main.py` file
- touch main.py
8. after mentioning the fastAPI library we need to run the server
- uvicorn main:app
9. for real time server we need to run the command
- uvicorn main:app --reload
10. after running previous command it will run the server by default port 8000
11. if we want to see the output in swaggerUI then write in URL
- localhost:8000/docs
12. 
