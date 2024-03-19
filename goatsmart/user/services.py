
import datetime
from django.conf import settings

from user.models import User
from user.repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)
    
    def create_user(self, data):    
        user_created = self.user_repository.create_user(user=data)
        return user_created.user_id
    
    def update_user(self, user_id, user):
        return self.user_repository.update_user(user_id, user)
    
    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)
    
    def get_all_users(self):
        users_query = self.user_repository.get_all_users()
        # Extract name and email from the query
        users_query_red = users_query.values('first_name', 'last_name', 'email')
        # Transform the query into a list
        return list(users_query_red)        
    
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
    
    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)
    
    def get_user_by_credentials(self, email, password):
        return self.user_repository.get_user_by_credentials(email, password)
    