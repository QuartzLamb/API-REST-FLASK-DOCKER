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
            if (agent != "") and (date != ""):
                dateFormat = "%d/%m/%Y %H:%M:%S"
                dateAsDateType = datetime.strptime(date, dateFormat)
                timestamp = dateAsDateType.timestamp()
                if (issue['agent'] == agent) and (issue['dateIssue'] == timestamp):
                        findedIssue = {
                            'dateIssue': issue['dateIssue'],
                            'descriptionIssue': issue['descriptionIssue'],
                            'titleIssue': issue['titleIssue'],
                            'agent': issue['agent']
                        }
                        filteredIssues.append(findedIssue)
            else:
                if agent != "":
                    if issue['agent'] == agent:
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
                        try:
                            dateAsDateType = datetime.strptime(date, dateFormat)
                        except Exception as ex:
                            return None
                        
                        timestamp = dateAsDateType.timestamp()
                        if issue['dateIssue'] == timestamp:
                            findedIssue = {
                                'dateIssue': issue['dateIssue'],
                                'descriptionIssue': issue['descriptionIssue'],
                                'titleIssue': issue['titleIssue'],
                                'agent': issue['agent']
                            }
                            filteredIssues.append(findedIssue)
                            
        if len(filteredIssues) == 0:
            return None
        
        return filteredIssues