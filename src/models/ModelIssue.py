import requests
from models.entities.Issue import Issue
from datetime import datetime

class ModelIssue():
    
    def getAllIssues():
        url = 'https://652add954791d884f1fd723c.mockapi.io/issue'
        response = requests.get(url)
        issues = response.json()
        return issues

    def filterIssues(agent, date):
        issues = ModelIssue.getAllIssues()
        filteredIssues = []
        for issue in issues:
            print(issue)
            if (agent != "") and (date != ""):
                print("En ambos")
                dateFormat = "%d/%m/%Y %H:%M:%S"
                dateAsDateType = datetime.strptime(date, dateFormat)
                print("fechas:")
                print(dateAsDateType)
                timestamp = dateAsDateType.timestamp()
                print(timestamp)
                print("En date")
                print(date)
                print(issue['dateIssue'])
                if (issue['agent'] == agent) and (issue['dateIssue'] == timestamp):
                        print('Agregandola')
                        findedIssue = {
                            'dateIssue': issue['dateIssue'],
                            'descriptionIssue': issue['descriptionIssue'],
                            'titleIssue': issue['titleIssue'],
                            'agent': issue['agent']
                        }
                        filteredIssues.append(findedIssue)
            else:
                if agent != "":
                    print("En agent")
                    if issue['agent'] == agent:
                        print('Agregandola')
                        findedIssue = {
                            'dateIssue': issue['dateIssue'],
                            'descriptionIssue': issue['descriptionIssue'],
                            'titleIssue': issue['titleIssue'],
                            'agent': issue['agent']
                        }
                        filteredIssues.append(findedIssue)
                else:
                    if date != "":
                        dateFormat = "%d/%m/%Y %H:%M:%S"
                        dateAsDateType = datetime.strptime(date, dateFormat)
                        print("fechas:")
                        print(dateAsDateType)
                        timestamp = dateAsDateType.timestamp()
                        print(timestamp)
                        print("En date")
                        print(date)
                        print(issue['dateIssue'])
                        if issue['dateIssue'] == timestamp:
                            print('Agregandola')
                            findedIssue = {
                                'dateIssue': issue['dateIssue'],
                                'descriptionIssue': issue['descriptionIssue'],
                                'titleIssue': issue['titleIssue'],
                                'agent': issue['agent']
                            }
                            filteredIssues.append(findedIssue)
                    else:
                        print("En ninguna")
        if len(filteredIssues) == 0:
            return None
        
        return filteredIssues