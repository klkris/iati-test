from app import db

class Organisation(db.Model):
	iatiId = db.Column(db.String(2000), primary_key=True)
	title = db.Column(db.String(2000))
	reportingOrg = db.Column(db.String(2000))
	telephone = db.Column(db.String(128))
	email = db.Column(db.String(2000))
	website = db.Column(db.String(2000))

	def __str__(self):
		return self.iatiId
	
	def __init__(self, id=0, title="", reportingOrg="", telephone="", email="", website=""):
		self.iatiId = id
		self.title = title
		self.reportingOrg = reportingOrg
		self.telephone = telephone
		self.email = email
		self.website = website

	def insertOrganisation(self, id, title, reportingOrg, telephone, email, website):
		org = Organisation(id, title, reportingOrg, telephone, email, website)
		print(id)
		db.session.add(org)
		db.session.commit()
