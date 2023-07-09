from flask import Flask,render_template,request
import joblib
import numpy as np

# model=joblib.load('heart-risk-reg-model2.sav')

app=Flask(__name__) 

@app.route('/')
def index():
	return render_template('Home.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/item_description')
def item_description():
	return render_template('item_description.html')



app.run(debug=True)