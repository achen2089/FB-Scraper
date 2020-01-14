from app import app
from flask import render_template, request
import numpy as np
import pandas as pd
import os
import sys
from flask import render_template, flash, redirect
from app.forms import LoginForm
import matplotlib.pyplot as plt
import time
from app.FB_scrape import scrape 





@app.route('/single', methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
    	info = form.date.data
    	scrape(info)
    	time.sleep(1)
    	return render_template('FB_result.html', info = info)

    return render_template('index.html', title='Home', form=form)


@app.route('/', methods=['GET','POST'])
def home():
	return render_template('home.html')