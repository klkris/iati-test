# IATIHDXAPINEPAL

Clone this repository
```
git clone https://github.com/klkris/iati-test.git
```

Create project directory
```
mkdir iatihdxapinepal
cd iatihdxapinepal
```

Install virtual env and activate 
```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Upgrade pip if needed
```
pip install --upgrade pip
```

Install the python requirements 
```
pip install -r requirements.txt
```

Create a Postgres user (use 'iatihdxapi' as password)
```
sudo -u postgres createuser -P -d iatihdxapi
```

Create a Postgres database
```
sudo -u postgres createdb -O iatihdxapi iatihdxapi
```

Set env variables
```
export FLASK_APP=iatiapi.py
export DATABASE_URL="postgresql://iatihdxapi:iatihdxapi@localhost/iatihdxapi"
```

Migrate the database
```
flask db init
flask db migrate
flask db upgrade
```

Run the project
```
python3 -m app.update
```

Connect to database to verify
```
sudo psql -d iatihdxapi -U iatihdxapi -W
select * from organisation;
```
