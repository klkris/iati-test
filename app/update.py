import requests
import json
import xml.etree.ElementTree as ET
from .models import Organisation
from app import db

#@app.route('/updateOrganisation')
#def updateOrganisation():
uri = 'http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=NP&limit=200'
response = requests.get(uri)
root = ET.fromstring(response.content)
for activities in root.findall('iati-activities/iati-activity'):
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
	org = Organisation(iatiId, title, reportingOrg, "", "", "")
	db.session.add(org)
	db.session.commit()
