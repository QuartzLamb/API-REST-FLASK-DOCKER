import requests
from models.entities.Agent import Agent

class ModelAgent():
    
    def getAllAgents():
        url = 'https://652add954791d884f1fd723c.mockapi.io/agent'
        response = requests.get(url)
        print("/////////////////////////////////")
        agents = response.json()
        return agents

    def getAgentById(agentID):
        try:
            agents = ModelAgent.getAllAgents()
            for auxAgent in agents:
                #Verifica si existe la propiedad agentName y password en el diccionario
                if 'agentID' in auxAgent: 
                    #Compara el agentName del diccionario con el del objeto obtenido comom parametro
                    if auxAgent['agentID'] == agentID:
                        agentName = auxAgent['agentName']
                        print("Usuario correcto")
                        loggedAgent = Agent(agentID, agentName, None)
                        return loggedAgent
            return None
        except Exception as ex:
            raise Exception(ex)


    def login(agent):
        try:
            #Obtener agentes y buscar el insertado
            agents = ModelAgent.getAllAgents()
            for auxAgent in agents:
                #Verifica si existe la propiedad agentName y password en el diccionario
                if ('agentName' in auxAgent) and ('password' in auxAgent): 
                    #Compara el agentName del diccionario con el del objeto obtenido comom parametro
                    if auxAgent['agentName'] == agent.agentName:
                        agentID = auxAgent['agentID']
                        agentName = auxAgent['agentName']
                        agentPassword = auxAgent['password']
                        correctPassword = Agent.check_password(agentPassword, agent.password)
                        if correctPassword:
                            print("Usuario correcto")
                            loggedAgent = Agent(agentID, agentName, agentPassword)
                            print(loggedAgent)
                            return loggedAgent
                else:
                    print("PROPIEDAD NO EXISTE EN EL DIC")
            print("/////////////////////////////////")
            return None
        except Exception as ex:
            raise Exception(ex)
