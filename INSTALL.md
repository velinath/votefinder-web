```bash
add-apt-repository ppa:deadsnakes/ppa
apt-get install python3.7 mysql-client default-libmysqlclient-dev python3.7-dev build-essential libssl-dev
curl -O https://bootstrap.pypa.io/get-pip-py && python3.7 get-pip.py
pip install virtualenv
virtualenv --python=/usr/bin/python3.7 /var/venvs/venv
apt-get install 
source /var/venvs/venv/bin/activate
git clone https://github.com/aletson/votefinder-web
cd votefinder-web
pip install -r requirements.txt
```
Review all of the settings in `votefinder/settings.py` for accuracy in your environment.
```bash
python manage.py migrate
python -Wall manage.py runserver localhost:8080
```
There must be a player with uid of -1 present in your database.
