from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests
from models.entities.Agent import Agent
from models.ModelAgent import ModelAgent
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "super secret key"
logginManager = LoginManager(app)
csrf = CSRFProtect()

@app.route('/', methods=['GET'])
def showEndpoints():
    return render_template("menu.html")


@logginManager.user_loader
def loadAgent(agentId):
    agent = ModelAgent.getAgentById(agentId)
    return agent

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('agentName')
        password = request.form.get('pwd')
        agent = Agent("0", name, password)
        loggedUser = ModelAgent.login(agent)
        if loggedUser != None:
            print(loggedUser)
            login_user(loggedUser)
            result = False
            return render_template("newIssue.html", result=result)
        else:
            return render_template("login.html")
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    #return render_template('login.html')
    return redirect(url_for('login'))

@app.route('/agent', methods=['GET', 'POST'])
def register():
    result = False
    print(request.method)
    if request.method == 'POST':
        url = 'https://652add954791d884f1fd723c.mockapi.io/agent'
        name = request.form.get('agentName')
        password = request.form.get('password')
        hashedPassword = Agent.encryptPassword(password)
        newAgent = {
            "agentName": name,
            "password": hashedPassword
        }
        response = requests.post(url, json=newAgent)
        print("Se envio")
        result = response.ok  
        print(response.ok)
    else:
        print(request.method)
        print("No se envio")
    print("-----------")
    return render_template('register.html', result=result)


@app.route('/issues', methods=['GET'])
def getIssues():
    print(request.method)
    url = 'https://652add954791d884f1fd723c.mockapi.io/issue'
    response = requests.get(url)
    print(response.json)
    print("EN ISSUES")
    return render_template('issuesList.html', datos=response.json())


@app.route('/issue', methods=['GET','POST'])
@login_required
def addIssue():
    result = False
    print(request.method)
    url = 'https://652add954791d884f1fd723c.mockapi.io/issue'
    if request.method == 'POST':
        date = request.form.get('dateIssue')
        title = request.form.get('titleIssue')
        description = request.form.get('descriptionIssue')
        agent = "agente agente!"
        newIssue = {
            "titleIssue": title,
            "descriptionIssue": description,
            "dateIssue": date,
            "agent": agent
        }
        response = requests.post(url, json=newIssue)
        print("Se envio")
        result = response.ok  
        print(response.ok)
        print("-----------")
        return render_template('newIssue.html', result=result)
    else:
        print("EN ISSUE")
        return render_template('newIssue.html', result=result)

#Redirige cuando se intente acceder a una ruta protegida
def status401(error):
    return redirect(url_for('login'))

if __name__ == '__main__':
    #Crea al token de acceso
    csrf.init_app(app)
    app.register_error_handler(401, status401)
    app.run(host="0.0.0.0", port=4000, debug=True)

