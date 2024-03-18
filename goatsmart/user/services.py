
class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)
    
    def create_user(self, user):
        return self.user_repository.create_user(user)
    
    def update_user(self, user_id, user):
        return self.user_repository.update_user(user_id, user)
    
    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)
    
    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
    
    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)
    
    def get_user_by_credentials(self, email, password):
        return self.user_repository.get_user_by_credentials(email, password)
    