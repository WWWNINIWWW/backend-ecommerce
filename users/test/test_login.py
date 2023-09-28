from django.test import TestCase
from users.models import User

def account():
    data = {
            'username': 'test',
            'password': 'complexpassword',
        }
    return data


def create_account(self):
    data = account()
    self.client.post('/users/signup', data=data )
    

def token_login(self):
    create_account(self)
    data = account()
    response = self.client.post('/users/login', data=data)
    return response.json().get('token')


def user_details():
    data = account()
    return User.objects.get(username=data['username']) 


class LoginAndSignupViewTestCase(TestCase):
    
    def test_status_code_signup(self):
        response = self.client.post('/users/signup')
        self.assertEquals(response.status_code, 200)
        
        
    def test_create_user_signup(self):
        data = account()
        response = self.client.post('/users/signup', data=data )
        user = User.objects.filter(username=response.request.get('username'))
        self.assertIsNotNone(user)
        
        
    def test_status_code_login(self):
        create_account(self)
        data = account()
        response = self.client.post('/users/login', data=data)
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_login_wrong_password(self):
        create_account(self)
        data = {
            'username':'test',
            'password': 'wrongusername',     
        }
        response = self.client.post('/users/login', data=data)
        self.assertNotEquals(response.status_code, 200)
        
        
    def test_account_login(self):
        self.assertIsNotNone(token_login(self))
        
    
    def test_token(self):
        response = self.client.get('/users/test_token',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 200)
        