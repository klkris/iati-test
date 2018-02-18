# IATIHDXAPINEPAL

Clone this repository
```
git clone https://github.com/klkris/iati-test.git
```

Cd to project directory
```
cd iati-test
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

Start the server
```
flask run
```
Update Organisation table by fetching records from IATI datastore API
```
http://localhost:5000/updateOrganisation
```

Connect to database to verify
```
sudo psql -d iatihdxapi -U iatihdxapi -W
select * from organisation;
```
Get all organisations present in the database
```
http://localhost:5000/orgs
```

Get organisation by passing id
```
http://localhost:5000/orgs/<id>
```
