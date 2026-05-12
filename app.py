from flask import Flask, render_template, request,redirect
import sqlite3
app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    #logic
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About page'

@app.route('/contact')
def contact():
    return 'Contact Page'

@app.route('/users')
def users():
    conn = get_db_connection()
    user_list = conn.execute(
        'SELECT * FROM users'
    ).fetchall()
    conn.close()
    return render_template('users.html',name="adhi", users =user_list)

@app.route('/submit',methods = ['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    conn = get_db_connection()
    
    conn.execute('''
            INSERT INTO users (name,email) VALUES (?,?)  
    ''',(name,email))
    
    conn.commit()
    conn.close()
    
    return redirect('/users')

@app.route('/users/<int:id>')
def user(id):
    print(id)
    conn = get_db_connection()
    user_details = conn.execute(
        'SELECT * FROM users WHERE id = ?',(id,)
    ).fetchone()
    return render_template('user.html',user = user_details)

@app.route('/edit/<int:id>')
def edituser(id):
    print(id)
    conn = get_db_connection()
    user_details = conn.execute(
        'SELECT * FROM users WHERE id = ?',(id,)
    ).fetchone()
    return render_template('edit.html',user = user_details)

@app.route('/update/<int:id>',methods = ['POST'])
def edit_user(id):
    name = request.form['name']
    email = request.form['email']
    
    conn = get_db_connection()
    conn.execute("""
        UPDATE
    
    """)





if __name__=='__main__':
    app.run(debug=True)