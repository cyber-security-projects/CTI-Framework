import os
import json
import uuid

class ManageUsers:
    def __init__(self, storage_dir="data"):
        self.storage_dir = storage_dir + "/users"
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_user_file(self, user_id):
        return os.path.join(self.storage_dir, f"{user_id}.json")
    
    def create_user(self, email:str, password:str):
        user_id = str(uuid.uuid4())
        new_user = {
            "uid": user_id,
            "email": email,
            "password": password,
            "usernames": []
        }
        file_path = self._get_user_file(user_id)
        with open(file_path, "w") as f:
            json.dump(new_user, f, indent=4)
        return user_id
    
    def get_users(self) -> list:
        ret = []
        with open(self.FILE_PATH, 'r') as file:
            for row in  file.readlines():
                user = row[0:len(row)-1]
                json.loads(user)
        return ret
    
users = ManageUsers()
users.create_user("Marcos", "sla")
