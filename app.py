from flask import Flask,render_template, request
# Imports / Setup
import sqlite3



app = Flask(__name__)
@app.route('/')
def index2():
    return render_template('index2.html')
# Routes
@app.route('/form.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        connection = sqlite3.connect("speechie.db")
        cursor = connection.cursor()

        # Form handling logic here
        name = request.form['email']
        password = request.form['password']
        # ...

        print(name,password)

        query= "SELECT name,password FROM users where name= '"+name+"' and password= '"+password+"'"
        cursor.execute(query)
        results= cursor.fetchall()

        if len(results) == 0:
            print("Sorry, incorrect crendential, Try again")
        else:
            return render_template("loginned.html")    
   
    #     # Logic for GET requests (if any)
    return render_template('form.html')
    
if __name__ == '__main__':
    app.run(debug=True)    