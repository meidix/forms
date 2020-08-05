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
        
        db.session.add(applicant)
        db.session.commit()

        flash('درخواست شما با موفقیت ارسال شد', 'success')
        return redirect(url_for('index'))
    
    else:
        flash('لطفا ایرادات زیر را قبل از ارسال دوباره فرم برطرف کنید', 'danger')
        return render_template('electronics/employment-form.html', form=form)
