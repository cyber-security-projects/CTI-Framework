import json
import re
import uuid

class ManageUsers:
    def __init__(self, filename="data/users.json"):
        self.file = filename
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_users(self):
        with open(self.file, "w") as file:
            json.dump(self.users, file, indent=4)
    
    def create_user(self, email:str, password:str) -> str:
        if re.match("^\S+@\S+\.\S+$", email) == None:
            raise Exception("Endereço de e-mail inválido!")
        if self.get_user_by_email(email) != {}:
            raise Exception("Endereço de e-mail já cadastrado!")
        uid = str(uuid.uuid4())
        self.users[uid] = {"email": email, "password": password, "usernames": {}}
        self._save_users()
        return uid
    
    def set_username(self, uid:str, username:str, desc:str = "general"):
        if uid in self.users:
            self.users[uid]["usernames"][desc] = username
            self._save_users()
            return True
        return False
    
    def get_user(self, uid:str):
        return self.users.get(uid, "Usuário não encontrado!")
    
    def get_user_by_email(self, email: str):
        for uid, user in self.users.items():
            if user["email"] == email:
                return {"uid": uid, "email": user["email"], "password": user["password"], "usernames": user["usernames"]}
        return {}
    
    def get_all_users(self):
        return self.users
    
    def delete_user(self, uid):
        if uid in self.users:
            del self.users[uid]
            self._save_users()
            return True
        return False
