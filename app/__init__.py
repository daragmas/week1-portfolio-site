import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from data.profiles import profiles

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"), profiles=profiles)


@app.route('/about/anitha')
def about_anitha():
    anitha = next(
        (profile for profile in profiles if profile['name'] == 'Anitha Amarnath'), None)
    return render_template('anitha_about_page.html', title="Anitha", url=os.getenv("URL"), profile=anitha)
