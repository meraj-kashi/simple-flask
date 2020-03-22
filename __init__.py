from flask import Flask, render_template, request
import random, os

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
    if not request.form.get('num'):  #If no name enetered 
        response="No number found! please try again."
    else:
        response=request.form.get('num')  #exp: http://localhost:5000/?name=meraj but here I use POST method! 
        response="Odd" if int(response)%2 else "Even"
    
    return render_template("index.html", response=response,var_name=var_name )
