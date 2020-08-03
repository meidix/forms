from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from forms.models import db, Applicant, ElectronicApplicant
from forms.electronic_forms import ApplicantsCreationForm, ElectricalApplicantCreationForm


bp = Blueprint('electronics', __name__)

@bp.route('/')
def index():
    return render_template('electronics/index-el.html')


@bp.route('/form', methods=['GET', 'POST'])
def create_request():
    form = ElectricalApplicantCreationForm()

    if form.validate_on_submit():
        applicant = ElectronicApplicant(
            first_name=form.first_name,
            last_name=form.last_name,
            national_id=form.national_id,
            date_of_birth=form.date_of_birth,
            email=form.email,
            mobile_phone=form.mobile_phone,
            Address=form.Address,
            university=form.university,
            university_subject=form.university_subject,
            university_degree=form.university_degree,
            work_reputation=form.work_reputations,
            altium_designer=form.altium_designer,
            arduino=form.arduino,
            proteus=form.proteus,
            atmel_studio=form.atmel_studio,
            microcontroller=form.microcontroller,
            power=form.power,
            others=form.others,
            resume=form.resume,
            expected_salary=form.expected_salary
        )
        db.session.add(applicant)
        db.session.commit()

        return redirect(url_for('index'))
    
    else:
        flash('لطفا ایرادات زیر را قبل از ارسال دوباره فرم برطرف کنید', 'danger')
        return render_template('electronics/employment-form.html', form=form)
