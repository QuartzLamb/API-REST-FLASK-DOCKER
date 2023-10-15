from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Agent(UserMixin):
    def __init__(self, agentID, agentName, password) -> None:
        self.id = agentID
        self.agentName = agentName
        self.password = password
    
    @classmethod #Permite invocar funcion sin necesidad de instanciar la clase.
    def check_password(self, hashedPassword, password):
        result = check_password_hash(hashedPassword, password)
        return result

    @classmethod
    def encryptPassword(self, password):   
        hash = generate_password_hash(password)
        return hash