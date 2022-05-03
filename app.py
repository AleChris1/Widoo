from flask import(
    Flask,
    jsonify,
    render_template
)
from flask_sqlalchemy import SQLAlchemy


#Configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:H75887152_AB@localhost:5432/widoodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    creation_date = db.Column(db.String, nullable = False)
    modification_date = db.Column(db.String, nullable = True)
    user_who_modified_it = db.Column(db.String, nullable = True)

    def __repr__(self):
        return 'User: Id={}, Username={}, Password={}, Creation Date={}, Modification Date={}, User Who Modified It={}'.format(
            self.id, self.username, self.password, self.creation_date, self.modification_date, self.user_who_modified_it)

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable =True)

    def __repr__(self):
        return 'User: Id={}, Title={}, Description={}'.format(
            self.id, self.title, self.description)

db.create_all()


#Controllers 
#main page with login and sing up
@app.route('/')
def index():
    return render_template('index.html')

#login
@app.route('/login')
def login():
    return None

#sing up
@app.route('/sing_up')
def sing_up():
    return None

#matrix page
@app.route('/home')
def home():
    return render_template('home.html')

#task configuration
@app.route('/home/task_settings')
def task_settings():
    return None

#creation of tasks
@app.route('/home/task_settings/create')
def create():
    return None

#task visualization
@app.route('/home/task')
def task():
    return None

#task deletion
@app.route('/home/task/delate_task')
def delate_task():
    return None


#Run
if __name__ == '__main__':
    app.run(debug=True, port=5000)
