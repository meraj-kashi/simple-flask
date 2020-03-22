from flask import Flask, render_template
import random

app= Flask(__name__)

@app.route('/')
def hello_world():
    rand=random.randint(0,1)
    if rand==1 :
        var_name='True'
    else:
        var_name='False'

    return render_template("index.html",var_name=var_name)
