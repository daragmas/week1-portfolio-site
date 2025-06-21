import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

profiles = [
    {
        "name": "Nate",
        "profile_picture": "./static/img/profilepic_nate.jpg",
        "short_bio": "A freelance web developer, with a background in mechanical engineering",
        "long_bio": "The should be a much longer bio here about Nate, but he put writing off until he was finished "
                    "with getting the website up and running. So, enjoy a Lorem Ipsum-esque placeholder.",
        "work_history": [
            {
                "position": "AI Quality Control Engineer",
                "company": "Data Annotation Tech",
                "years_employed": "2024 - Present"
            },
            {
                "position": "Associate Developer",
                "company": "BGG Creative Studio",
                "years_employed": "2023 - Present"
            },
            {
                "position": "Mechanical Engineer",
                "company": "General Services Administration",
                "years_employed": "2018 - 2022"
            },
        ],
        "education": {
            "university": "The College of New Jersey",
            "major": "Engineering Management",
            "graduation_year": 2016
        },
        "hobbies": [("name", "img_url")]
    },
    {
        "name": "Anitha",
        "profile_picture": "picture_address",
        "short_bio": "stuff",
        "long_bio": "longer stuff",
        "work_history": [("position1", "years worked")],
        "education": {
            "university": "TCNJ",
            "major": "Engineering Management",
            "graduation_year": 2016
        },
        "hobbies": [("name", "img_url")]
    }
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellows", url=os.getenv("URL"), profiles=profiles)
