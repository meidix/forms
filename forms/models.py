from flask_sqlalchemy import SQLAlchemy

from .types import ChoiceType


db = SQLAlchemy()

class Applicant(db.Model):
    __tablename__ = 'applicants'

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    national_id = db.Column(db.String(10), unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_phone = db.Column(db.String(11), unique=True, nullable=False)
    Address = db.Column(db.Text)
    university = db.Column(db.String(80), nullable=True)
    university_subject = db.Column(db.String(50), nullable=True)

    university_degree = db.Column(ChoiceType({'دیپلم': 'diploma',
                            'کاردانی': 'over diploma',
                            'کارشناسی': 'bachelor',
                            'کارشناسی ارشد': 'seneior',
                            'دکتری': 'PHD'
                        }), nullable=False)

    work_reputations = db.Column(db.Text, nullable=True)

    


class ElectronicApplicant(Applicant):
    __tablename__ = 'ElectronicApplicants'

    pk = db.Column(db.Integer, primary_key=True)
    altium_designer = db.Column(db.Boolean, nullable=True, default=False)
    arduino = db.Column(db.Boolean, nullable=True, default=False)
    code_vision = db.Column(db.Boolean, nullable=True, default=False)
    proteus = db.Column(db.Boolean, nullable=True, default=False)
    atmel_studio = db.Column(db.Boolean, nullable=True, default=False)
    microcontroller = db.Column(db.Boolean, nullable=True, default=False)
    power = db.Column(db.Boolean, nullable=True, default=False)
    others = db.Column(db.Text, nullable=True)
    resume = db.Column(db.LargeBinary)


