import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from data.profiles import profiles

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"), profiles=profiles)
