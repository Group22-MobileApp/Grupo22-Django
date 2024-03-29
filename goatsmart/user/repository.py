from django.conf import settings
from user.models import User

class UserRepository:
   # Usando sqlite3
    def get_user(self, user_id):
        return User.objects.get(id=user_id)
    
    def create_user(self, user):
        return User.objects.create(**user)
    
    def update_user(self, user_id, user):
        return User.objects.filter(id=user_id).update(**user)
    
    def delete_user(self, user_id):
        return User.objects.filter(id=user_id).delete()
    
    def get_all_users(self):
        return User.objects.all()
    
    def get_user_by_email(self, email):
        return User.objects.get(email=email)
    
    def get_user_by_username(self, username):
        return User.objects.get(username=username)
    
    def get_user_by_credentials(self, email, password):
        return User.objects.get(email=email, password=password)


    # def __init__(self):
    #     self.db = settings.db # Firebase database instance

    # def get_user(self, user_id):
    #     return self.db.child('users').child(user_id).get().val()
    
    # def create_user(self, user):
    #     return self.db.child('users').push(user)
    
    # def update_user(self, user_id, user):
    #     return self.db.child('users').child(user_id).update(user)
    
    # def delete_user(self, user_id):
    #     return self.db.child('users').child(user_id).remove()
    
    # def get_all_users(self):
    #     return self.db.child('users').get().val()
    
    # def get_user_by_email(self, email):
    #     users = self.get_all_users()
    #     for user_id, user in users.items():
    #         if user['email'] == email:
    #             return user
    #     return None
    
    # def get_user_by_username(self, username):
    #     users = self.get_all_users()
    #     for user_id, user in users.items():
    #         if user['username'] == username:
    #             return user
    #     return None
    
    # def get_user_by_credentials(self, email, password):
    #     user = self.get_user_by_email(email)
    #     if user and user['password'] == password:
    #         return user
    #     return None