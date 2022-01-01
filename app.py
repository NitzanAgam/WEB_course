from flask import Flask, redirect, url_for, render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
@app.route('/home')
def hello_func():
    found = False
    if found:
        name = 'Nitzan Agam'
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')


@app.route('/catalogs')
def catalogs_func():
    return redirect('/catalog')


@app.route('/about')  # this is another page
def about_func():
    return render_template('about.html',
                           uni='BGU',
                           profile={'First Name': 'Nitzan',
                                    'Last Name': 'Agam'},
                           degrees=['BSc', 'MSc'],
                           hobbies=('dancing',
                                    'art',
                                    'reading',
                                    'surfing'))


@app.route('/catalog')
def catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html',p_name=product,p_size=size, color='green')
    return render_template('catalog.html')


@app.route('/login',methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # DB
        session.username = request.form['username']
        session.password = request.form['password']
        return render_template('index.html', username=session.username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    session['LoggedIn'] = False
    return render_template('index.html')


@app.route('/assignment8')
def hobbies_func():
    currentUser = 'Nitzan'
    return render_template('assignment8.html',
                           name=currentUser,
                           travel={'New York', 'Bangkok', 'London', 'Barcelona'},
                           Dancing={'Folklore', 'Jazz', 'Mainstream'},
                           bShows={'Mama Mia', 'Frozen', 'Kinky Boots'})


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    MyUsers = [
        {'id': 1, 'email': "nitzan.agam@gmail.in", 'firstname': "Nitzan", 'lastname': "Agam"},
        {'id': 2, 'email': "kimkardash@gmail.in", 'firstname': "Kim", 'lastname': "Kardashian"},
        {'id': 3, 'email': "Khloe.kardash@gmail.in", 'firstname': "Khloe", 'lastname': "Kardashian"},
        {'id': 4, 'email': "Kortney.kardash@gmail.in", 'firstname': "Kortney", 'lastname': "Kardashian"},
        {'id': 5, 'email': "kylie.jenner@gmail.in", 'firstname': "Kylie", 'lastname': "Kardashian"},
        {'id': 6, 'email': "kendel.jenner@gmail.in", 'firstname': "Kendel", 'lastname': "Kardashian"}
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    elif request.method == 'POST':
        if 'username' in request.form:
            username = request.form['username']
            session['LoggedIn'] = True
            session['username'] = username
        else:
            session['LoggedIn'] = False
            session['username'] = ''
            username = ''
    return render_template('Assignment9.html',
                           MyUsers=MyUsers,
                           username=username,
                           firstname=firstname,
                           request_method=request.method)


# assignment 10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)

