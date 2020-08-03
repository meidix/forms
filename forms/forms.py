from flask_wtf import FlaskForm
from wtforms import (
    StringField, validators, DateField, TextAreaField, SelectField
)

from models.UniversityDegreeEnum import diploma, associate, bachelor, senior, phd


DEGREE_CHOICES = [(diploma, 'دیپلم'), (associate, 'فوق دیپلم'), (bachelor,'کارشناسی'), (senior, 'کارشناسی ارشد'), (phd, 'دکتری')]
class ApplicantsForm(FlaskForm):
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
            validators.Length(min=10, max=10, 'کد ملی به درستی وارد نشده')
        ]
    )

    date_of_birth = DateField(
        label='تاریخ تولد',
        validators=validators.InputRequired('تاریخ تولد الزامیست')
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
            validators.Length(min=11, max=11, 'شماره موبایل وارد شده صحیح نمی باشد'),
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