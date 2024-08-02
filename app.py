from flask import Flask, render_template, request 
import psycopg2  # Import the PostgreSQL library 
app = Flask(_name, template_folder='Templates') # Connect to the PostgreSQL database

conn = psycopg2.connect(     
    host="127.0.0.1",     
    user="postgres",  # Replace with your PostgreSQL username     
    password="root",  # Replace with your PostgreSQL password     
    database="postgres" 
    ) 
cursor = conn.cursor() 

@app.route('/') 
def login():     
    return render_template("login.html") 

@app.route('/login_validation', methods=['POST']) 
def login_validation():     
    user_name = request.form.get('Uname')     
    password = request.form.get('Pass')    
     # Get valid users with the entered user name and password     
    cursor.execute("SELECT * FROM login_table WHERE user_name LIKE %s AND password LIKE %s", (user_name, password))     
    user = cursor.fetchall()     
    if len(user) > 0:         
        return render_template("home.html")     
    else:         
        return render_template("login.html") 
@app.route('/home') 
def home():     
        return render_template("home.html") 

@app.route('/add_user', methods=['POST']) 
def add_user():     
        user_name = request.form.get('Uname')     
        email = request.form.get('Email')     
        password = request.form.get('Pass')     
        cursor.execute(         
            "INSERT INTO login_table (user_name, email, password) VALUES (%s, %s, %s)",         
            (user_name, email, password)     
        )     
        conn.commit()     
        return render_template('login.html') 
@app.route('/register') 
def register():     
    return render_template("register.html") 
if __name_ == '_main_':     
    app.run(debug=True)  