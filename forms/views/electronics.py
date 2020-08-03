from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from forms.models import db


bp = Blueprint('electronics', __name__)

@bp.route('/')
def index():
    return render_template('electronics/index-el.html')


@bp.route('/form', methods=['GET', 'POST'])
def create_request():
    form = None

    if request.method == 'POST':
        pass

    return render_template('electronics/emplyment-form.html', form=form)
