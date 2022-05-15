from flask import Flask, render_template,g, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG']= True

def connect_db():
    sql =sqlite3.connect(r'C:\Users\HP\Desktop\Courses\Flask App\food_log.db')
    sql.row_factory=sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()   


@app.route('/')
def index():
    return render_template('home.html');

@app.route('/view')
def view():
    return render_template('day.html');

@app.route('/food',methods=['GET','POST'])
def food():
    if request.method =='POST':
        name=request.form['food_name']
        carborhydrates= int(request.form['carb'])
        protein= int(request.form['protein'])
        fat= int(request.form['fat'])
        
        calories= carborhydrates * 4 + protein * 4 + fat * 9
        
        db= get_db()
        db.execute('insert into food (name,protein,carbohydrates,fat,calories) values('????)')
    else:
        return render_template('add_food.html')


