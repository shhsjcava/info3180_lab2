"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for, flash
from random import randint
from form import MyForm
from werkzeug.utils import secure_filename
import time, os






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
    
filefolder = './files'

@app.route('/profile', methods =['POST', 'GET'])
def profile():
    """Should be able to view profile"""
    form = MyForm()
    if request.method == 'POST' and form.validate():
        userid = genrateid(form.fname.data, form.lname.data)
        created_on = timenow()
        
       
        photo=form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        photo=photo.filename
        
        users = User(userid,
        form.fname.data, 
        form.lname.data, 
        form.sex.data, 
        form.email.data, 
        form.address.data, 
        form.bio.data, 
        photo,
        created_on)
        db.session.add(users)
        db.session.commit()
        
        flash('You have been successfully added!')
        return redirect(url_for('allusers'))
    
        
    return render_template('profile.html', form =form)

def genrateid(fn, ln):
    "generates a unique id for each user"
    uid= fn[0] + ln[0] +str(randint(100, 999))
    return uid 
    
@app.route('/profiles')
def allusers():
    """Should be able to view all profiles in the database"""
   
    users = db.session.query(User).all()
    return render_template('profiles.html', users =users)


@app.route('/profile/<userid>')
def userprofile(userid):
    'Should see the profile for a userid'
    user = db.session.quety(User).filter_by(userid =userid).first()
   # user = User.query.filter_by(userid=userid).first()
    return render_template('profile.html',user=user)


def timenow():
    now = time.strftime(" %M %d" + "," + "%Y")
    return (now)

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
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def format_date_joined():
    return 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
