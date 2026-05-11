from flask import Flask,render_template,request,redirect

app = Flask(__name__)
users_list = [
    {'id':1,'name':'adithya','email':'adithya@gmail.com'},
    {'id':2,'name':'adi','email':'adi@gmail.com'},
    {'id':3,'name':'appu','email':'appu@gmail.com'},
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html','name'='adithya',users=users_list)
@app.route('/submit',methods = ['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    id = len(users_list)+1
    users_list.append({'id':id,'name':name,'email':email})
    return redirect('users')
@app.route('/users/<int:id>')
def user(id):
    return f"id is{id}"

if __name__=='__main__':
    app.run(debug=True)