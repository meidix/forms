from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from forms.models import db, Applicant, ElectronicApplicant, UniversityDegreeEnum
from forms.electronic_forms import ApplicantsCreationForm, ElectricalApplicantCreationForm

from datetime import datetime


bp = Blueprint('electronics', __name__)

@bp.route('/')
def index():
    return render_template('electronics/index-el.html')


@bp.route('/form', methods=['GET', 'POST'])
def create_request():
    form = ElectricalApplicantCreationForm()

    if form.validate_on_submit():

        applicant = ElectronicApplicant()
        form.populate_obj(applicant) 

        if form.degree.data == 'diploma':
            applicant.university_degree = UniversityDegreeEnum.diploma
        elif form.degree.data == 'associate':
            applicant.university_degree = UniversityDegreeEnum.associate
        elif form.degree.data == 'bahcelor':
            applicant.university_degree = UniversityDegreeEnum.bachelor
        elif form.degree.data == 'senior':
            applicant.university_degree = UniversityDegreeEnum.senior
        elif form.degree.data == 'phd':
            applicant.university_degree = UniversityDegreeEnum.phd
        
        db.session.add(applicant)
        db.session.commit()

        flash('درخواست شما با موفقیت ارسال شد', 'success')
        return redirect(url_for('index'))
    
    else:
        flash('لطفا ایرادات زیر را قبل از ارسال دوباره فرم برطرف کنید', 'danger')
        return render_template('electronics/employment-form.html', form=form)
