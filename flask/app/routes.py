from app import app
from flask import render_template, request
import numpy as np
import pandas as pd
import os
import sys
from flask import render_template, flash, redirect
from app.forms import LoginForm
import matplotlib.pyplot as plt





@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    user = {'username': 'Christian'}
    return render_template('index.html', title='Home', user=user, form=form)
