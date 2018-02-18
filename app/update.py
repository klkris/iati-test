import requests
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from .models import Organisation
from app import db

#@app.route('/updateOrganisation')
def updateOrganisation():
	uri = 'http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=NP&limit=1000'
	response = requests.get(uri)
	root = ET.fromstring(response.content)
	for activities in root.findall('iati-activities/iati-activity'):
		try:
			last_updated = datetime.strptime((activities.attrib['last-updated-datetime'])[:19], '%Y-%m-%dT%H:%M:%S')
			iatiId = ''
			title = ''
			reportingOrg = ''
			for node in activities.getiterator():
				if node.tag == 'iati-identifier':
					iatiId = node.text
				if node.tag == 'title':
					title = node.text
				if node.tag == 'reporting-org':
					reportingOrg = node.text
#		if node.tag == 'contact-info':
#			email = node.find('email').text
#			phone = node.find('telephone').text
#			website = node.find('website').text
			exists = db.session.query(db.exists().where(Organisation.iatiId == iatiId)).scalar()
			if exists:
				org = Organisation.query.get(iatiId)
				if last_updated > org.last_updated:
					org.iatiId = iatiId
					org.title = title
					org.reportingOrg = reportingOrg
					org.last_updated = datetime.now()
			else:
				org = Organisation(iatiId, title, reportingOrg, "", "", "", datetime.now())
			print(iatiId + ' date: ' + str(last_updated)) 
			try:
				org
			except NameError:
				pass
			else:
				db.session.add(org)
		except Exception as e:
			print(e)
	db.session.commit()

if __name__ == "__main__":
	updateOrganisation()

