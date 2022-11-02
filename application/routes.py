from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.forms import LoginForm, RegisterForm, EventForm, UpdateForm
from application.models import User, Event

#Index Page
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index=True)

#Schedule Page
@app.route('/schedule', methods=['POST', 'GET'])
def schedule():
    if not session.get('username'):
        return redirect('/login')
    form = EventForm()
    if form.validate_on_submit():
        event_id     = Event.objects.count() + 1
        user_id = session.get('user_id')

        Event_Name    = form.Event_Name.data
        Event_Date    = form.Event_Date.data

        Event(event_id=event_id, Event_Name=Event_Name, Event_Date=Event_Date, user_id = user_id).save()
        flash("Event save successful","success")
        return redirect(url_for('index'))
    return render_template("schedule.html", title="Schedule", form=form, schedule=True)

#Check Event Page
@app.route('/event', methods = ['GET', 'POST'])
def event():
    user_id = session.get('user_id')
    classes = list(User.objects.aggregate(*[
    {
        '$lookup': {
            'from': 'event', 
            'localField': 'user_id', 
            'foreignField': 'user_id', 
            'as': 'r1'
        }
    }, {
        '$unwind': {
            'path': '$r1', 
            'includeArrayIndex': 'r1_id', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$match': {
            'user_id': user_id
        }
    }
]))
    # EventData = Event.objects.all()

    if classes == None:
        return "You don't have any event scheduled"

    if session.get('event_id'):
        event_id = session.get('event_id')
        Event_Name = request.form.get('Event_Name')
        Event_Date = request.form.get('Event_Date')
        event = Event.objects(event_id=event_id).first()
        event.update(Event_Name=Event_Name, Event_Date=Event_Date)
        session['event_id'] = False
        return redirect('/event')
    return render_template("showdata.html", event=True, classes = classes)

#Login Page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect("/index")

    form = LoginForm()
    if form.validate_on_submit() == True:
        email = form.Email.data
        password = form.Password.data

        user = User.objects(Email=email).first()
        if user and user.get_password(password):         
            flash(f"{user.First_Name}You are logged in!", "success")
            session.clear()
            session['user_id'] = user.user_id
            session['username'] = user.First_Name
            return redirect("/index")
        else:
            flash("You are not logged in!", "danger")
    return render_template("login.html", form = form, login = True, title = 'Login')

@app.route('/logout')
def logout():
    session.clear()
    session['logout'] = False
    session.pop('username', None)
    return redirect(url_for('index'))

# Register Page
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if session.get('username'):
        return redirect("/index")
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     = user_id + 1

        first_name  = form.First_Name.data
        last_name   = form.Last_Name.data
        Email       = form.Email.data
        password    = form.Password.data


        user = User(user_id=user_id, Email = Email, First_Name=first_name, Last_Name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route('/update', methods = ['POST', 'GET'])
def Update_event():
    event_id = request.form.get('event_id')
    Event_Name = request.form.get('Event_Name')
    Event_Date = request.form.get('Event_Date')

    session['event_id'] = event_id
    event = Event.objects(event_id=event_id).first()
    if not event:
        return "No Event found"
    EventData = Event.objects.all()
    return render_template('update.html', EventData = EventData)

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    event_id = request.form.get('event_id')
    Event_Name = request.form.get('Event_Name')
    Event_Date = request.form.get('Event_Date')

    event = Event.objects(event_id=event_id).first()

    event.delete()

    return redirect('/event')

def logout():
    session['user_id'] == False
    return redirect('/index')