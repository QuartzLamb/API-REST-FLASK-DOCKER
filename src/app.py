from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({ "response": "hello world" })

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/agent', methods=['GET', 'POST'])
def register():
    result = False
    print(request.method)
    if request.method == 'POST':
        url = 'https://652add954791d884f1fd723c.mockapi.io/agent'
        name = request.form.get('agentName')
        password = request.form.get('password')
        print(name)
        print(password)
        newAgent = {
            "userName": name,
            "password": password
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


@app.route('/issue', methods=['GET','POST'])
@app.route('/issues', methods=['GET'])
def getIssues():
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
        if request.path == '/issue':
            print("EN ISSUE")
            return render_template('newIssue.html', result=result)
        else:
            response = requests.get(url)
            print(response.json)
            print("EN ISSUES")
            return render_template('issuesList.html', datos=response.json())



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

