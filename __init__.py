from flask import Flask, render_template, request
import random

app= Flask(__name__)

@app.route('/',methods=['POST','GET']) # read both GET nad POST method
def hello_world():
    #Create a randome number between 0 and 1 to show on HTML page
    rand=random.randint(0,1)
    if rand==1 :
        var_name='True'
    else:
        var_name='False'
    
    #Get name from request arquemnt
    if not request.form.get('name'):  #If no name enetered 
        name="guest"
    else:
        name=request.form.get('name')  #exp: http://localhost:5000/?name=meraj but here I use POST method! 
    
    return render_template("index.html",name=name,var_name=var_name )
