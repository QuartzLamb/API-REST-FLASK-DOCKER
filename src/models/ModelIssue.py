import requests
from models.entities.Issue import Issue

class ModelIssue():
    
    def getAllIssues():
        url = 'https://652add954791d884f1fd723c.mockapi.io/issue'
        response = requests.get(url)
        issues = response.json()
        return issues

    def filterIssuesByAgent(agent):
        issues = ModelIssue.getAllIssues()
        filteredIssues = []
        for issue in issues:
            print(issue)
            if issue['agent'] == agent:
                print('Agregandola')
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