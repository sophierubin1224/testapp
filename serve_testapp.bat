cd C:\Users\vcm\Desktop\testapp
git pull https://%TESTAPP_GIT_PAT%@github.com/angoble01/testapp.git
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py
