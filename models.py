from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = "BARCODE_DETAILS"
    Barcode = db.Column(db.String(32), primary_key=True)
    Name = db.Column(db.String(32))
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(32))
    Date = db.Column(db.String(32))
    Benf_id = db.Column(db.String(32))
    Ehr_id = db.Column(db.Integer)
    Visit_id = db.Column(db.String(32))
    Payment_status = db.Column(db.String(32))
    Hra_status = db.Column(db.String(32))
    Member_id = db.Column(db.Integer)
    email_id = db.Column(db.String(32))
    language = db.Column(db.String(32))
    v2 = db.Column(db.String(32))

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True