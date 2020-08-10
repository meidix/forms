from werkzeug.utils import secure_filename

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from forms.models import db, Applicant, ElectronicApplicant, UniversityDegreeEnum
from forms.electronic_forms import ApplicantsCreationForm, ElectricalApplicantCreationForm
from forms import ALLOWED_EXTENSIONS


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
        return redirect(url_for('electronics.upload_resume', id=applicant.pk))
    
    else:
        flash('لطفا ایرادات زیر را قبل از ارسال دوباره فرم برطرف کنید', 'danger')
        return render_template('electronics/employment-form.html', form=form)


def allowed_file(filename):    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/resume/<id>', methods=['GET', 'POST'])
def upload_resume(id):
    if request.method == 'POST':
        if not request.files:
            flash('شما فایلی آپلود نکردید')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('فایل انتخاب نشده است')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            user = ElectronicApplicant.query.get(id)
            if user:
                user.resume = file
                user.save()
            
            flash('هیچ درخواستی با این شماره ملی وجود ندارد')
            return redirect(request.url)
        
        flash('فرمت فایل پذیرفته نیست')
        return redirect(request.url)

    return render_template('electronics/resume-upload.html')
