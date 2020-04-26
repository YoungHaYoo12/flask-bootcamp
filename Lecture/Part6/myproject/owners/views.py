from flask import Blueprint,render_template,redirect,url_for, flash
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners',__name__,template_folder='templates/owners')

@owners_blueprint.route('/add', methods=['GET','POST'])
def add():
  form = AddForm()

  if form.validate_on_submit():
    owner = Owner(form.owner_name.data,form.puppy_id.data)
    db.session.add(owner)
    db.session.commit()
    flash(f"Owner {owner.name} has been registered")
    return redirect(url_for('puppies.list'))
  
  return render_template('add_owner.html',form=form)
