

# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

users = {'Henrique': [1, 5, 9], 'Jony': [2, 6, 10], 'Thiago': [3, 7, 11], 'Samuel': [4, 8, 12]}

@app.route('/')
def hello_world():
    data = datetime.datetime.now().date()
    now = f'{data.day}/{data.month}/{data.year}'

    currentuser = ''
    for u in users.keys():
        if data.month in users[u]: currentuser = u

    usr = list(users.keys())
    nextuser = ''
    try:
        nextuser = usr[usr.index(currentuser) + 1]
    except:
        nextuser = usr[0]
        
    lastuser = usr[usr.index(currentuser) - 1]

    dados = {'currentuser': currentuser, 'lastuser': lastuser, 'nextuser': nextuser, 'now': now}

    return render_template("home.html", dados=dados)

