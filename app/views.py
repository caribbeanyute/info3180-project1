"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    userForm = ProfileForm()
    print(userForm)
    
    if request.method == 'POST' :
        if userForm.validate_on_submit():
            first_name = userForm.firstname.data
            last_name = userForm.lastname.data
            location = userForm.location.data
            email = userForm.email.data
            biography = userForm.biography.data
            gender = userForm.gender.data
            file = userForm.file.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(
            app.instance_path, app.config['UPLOAD_FOLDER'], filename))
            user = UserProfile(first_name,last_name,gender,email,location,biography,filename)
            db.session.add(user)
            db.session.commit()

    return render_template('form.html',form=userForm)

@app.route('/profiles')
def profiles():
    """Render the website's profile page."""
    user_profiles = db.session.query(UserProfile).all()
    return render_template('profile.html',user_profiles=user_profiles)

@app.route('/specprofile/<id>')
def specficProfiles(id):
    """Render the website's profile page."""
    user = db.session.query(UserProfile).filter_by(id=int(id)).first()
    return render_template('profile.html',user=user)
    


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
