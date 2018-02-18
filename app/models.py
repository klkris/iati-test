from app import db
from app import app
from marshmallow import Schema, fields

class Organisation(db.Model):
	iatiId = db.Column(db.String(2000), primary_key=True)
	title = db.Column(db.String(2000))
	reportingOrg = db.Column(db.String(2000))
	telephone = db.Column(db.String(128))
	email = db.Column(db.String(2000))
	website = db.Column(db.String(2000))
	last_updated = db.Column(db.DateTime)

	def __str__(self):
		return self.iatiId
	
	def __init__(self, id=0, title="", reportingOrg="", telephone="", email="", website="", last_updated=""):
		self.iatiId = id
		self.title = title
		self.reportingOrg = reportingOrg
		self.telephone = telephone
		self.email = email
		self.website = website
		self.last_updated = last_updated

class OrganisationSchema(Schema):
	class Meta:
		fields = ('iatiId', 'title', 'reportingOrg', 'telephone', 'email', 'website', 'last_updated')

org_schema = OrganisationSchema()
orgs_schema = OrganisationSchema(many=True)
