from flask_wtf import FlaskForm
from wtforms import (
    StringField, validators, DateField, TextAreaField, SelectField, SubmitField, BooleanField, FileField, RadioField, IntegerField
)

from . import models

DEGREE_CHOICES = [
    (models.UniversityDegreeEnum.diploma, 'دیپلم'),
    (models.UniversityDegreeEnum.associate, 'فوق دیپلم'),
    (models.UniversityDegreeEnum.bachelor, 'کارشناسی'),
    (models.UniversityDegreeEnum.senior, 'کارشناسی ارشد'),
    (models.UniversityDegreeEnum.phd, 'دکتری')]


class ApplicantsCreationForm(FlaskForm):
    first_name = StringField(
        label="نام",
        validators=[
            validators.DataRequired('وارد کردن نام الزامیست'),
            validators.Length(max=30)
        ]
    )
    
    last_name = StringField(
        label='نام خانوادگی',
        validators=[
            validators.DataRequired('وارد کردن نام خانوادگی الزامیست'),
            validators.Length(max=45)
        ]
    )

    national_id = StringField(
        label='کد ملی',
        validators=[
            validators.DataRequired('وارد کردن کد ملی الزامیست'),
            validators.Length(min=10, max=10, message='کد ملی به درستی وارد نشده')
        ]
    )

    age = IntegerField(
        label='سن',
        validators=[
            validators.InputRequired('وارد کردن سن الزامیست')
        ]
    )

    email = StringField(
        label='ایمیل',
        validators=[
            validators.Email('آدرس ایمیل وارد شده صحیح نمیباشد'),
            validators.InputRequired('وارد کردن ایمیل الزامیست')
        ]
    )

    mobile_phone = StringField(
        label='شماره موبایل',
        validators=[
            validators.Length(min=11, max=11, message='شماره موبایل وارد شده صحیح نمی باشد'),
            validators.InputRequired('وارد کردن شماره موبایل الزامیست')
        ]
    )

    Address = TextAreaField(
        label='آدرس',
        validators=[
            validators.Length(max=500)
        ]
    )

    university = StringField(
        label='دانشگاه',
        validators=[
            validators.InputRequired('وارد کردن دانشگاه محل تحصیل الزامیست'),
        ]
    )

    university_subject = StringField(
        label='رشته تحصیلی',
        validators=[
            validators.InputRequired('وارد کردن رشته تحصیلی الزامیست'),
        ]
    )

    university_degree = SelectField(
        label='مدرک تحصیلی',
        validators=[
            validators.InputRequired('وارد کردن مدرک تحصیلی الزامیست')
        ],
        choices=DEGREE_CHOICES
    )

    work_reputations = TextAreaField(
        label='سوابق کاری',
        validators=[validators.Optional()]
    )

    submit = SubmitField()


class ElectricalApplicantCreationForm(ApplicantsCreationForm):
    altium_designer = BooleanField(
        label='آلتیوم دیزاینر(Altium Designer)',
        validators=[
            validators.Optional()
        ]
    )

    arduino = BooleanField(
        label='آردوینو(Arduino)',
        validators=[
            validators.Optional()
        ]
    )

    code_vision = BooleanField(
        label='کد ویژن(code vision)',
        validators=[
            validators.Optional()
        ]
    )

    proteus = BooleanField(
        label='پروتئوس(proteus)',
        validators=[
            validators.Optional()
        ]
    )

    atmel_studio = BooleanField(
        label='اتمل استودیو(Atmel Studio)',
        validators=[
            validators.Optional()
        ]
    )

    microcontroller = BooleanField(
        label='میکروکنترلر ها',
        validators=[
            validators.Optional()
        ],
    )

    power = BooleanField(
        label='مدارات تغذیه',
        validators=[
            validators.Optional()
        ]
    )

    others = TextAreaField(
        label='مهارت های دیگر',
        validators=[
            validators.Optional()
        ]
    )

    expected_salary = StringField(
        label='حقوق پیشنهادی',
        validators=[
            validators.Length(max=7, message=':))))')
        ]
    )


    