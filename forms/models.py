from forms import db

import enum


class UniversityDegreeEnum(enum.Enum):
    diploma = 'دیپلم'
    associate = 'کاردانی'
    bachelor = 'کارشناسی'
    senior = 'کارشناسی ارشد'
    phd = 'دکتری'


class Applicant(db.Model):
    __tablename__ = 'applicants'

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    national_id = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_phone = db.Column(db.String(11), unique=True, nullable=False)
    Address = db.Column(db.Text)
    university = db.Column(db.String(80), nullable=False)
    university_subject = db.Column(db.String(50), nullable=False)

    university_degree = db.Column(db.Enum(UniversityDegreeEnum),
                            default=UniversityDegreeEnum.diploma,
                            nullable=True
                        )

    work_reputations = db.Column(db.Text, nullable=True)



class ElectronicApplicant(Applicant):
    __tablename__ = 'ElectronicApplicants'

    altium_designer = db.Column(db.Boolean, nullable=True, default=False)
    arduino = db.Column(db.Boolean, nullable=True, default=False)
    code_vision = db.Column(db.Boolean, nullable=True, default=False)
    proteus = db.Column(db.Boolean, nullable=True, default=False)
    atmel_studio = db.Column(db.Boolean, nullable=True, default=False)
    microcontroller = db.Column(db.Boolean, nullable=True, default=False)
    power = db.Column(db.Boolean, nullable=True, default=False)
    others = db.Column(db.Text, nullable=True)
    resume = db.Column(db.LargeBinary, nullable=True)
    expected_salary = db.Column(db.String(7), nullable=True)


