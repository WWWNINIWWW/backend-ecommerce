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


      
        
class UsersStatusCodeViewTestCase(TestCase):
    
    def test_status_code_users_get_authorization(self):
        response = self.client.get('/users/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_users_get_not_authorization(self):
        response = self.client.get('/users/')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_users_post_authorization(self):
        response = self.client.post('/users/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_users_post_not_authorization(self):
        response = self.client.post('/users/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_users_put_authorization(self):
        response = self.client.put('/users/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_users_put_not_authorization(self):
        response = self.client.put('/users/')
        self.assertEquals(response.status_code, 403)
    
    
    def test_status_code_users_delete_authorization(self):
        response = self.client.delete('/users/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_users_delete_not_authorization(self):
        response = self.client.delete('/users/')
        self.assertEquals(response.status_code, 403)    
        
    
class UsersDetailsStatusCodeViewTestCase(TestCase):
    
    def test_status_code_users_details_get_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.get(f'/users/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_users_details_get_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.get(f'/users/{user.pk}/')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_users_details_post_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.post(f'/users/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 405)
        
    
    def test_status_code_users_details_post_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.post(f'/users/{user.pk}/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_users_details_put_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.put(f'/users/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_users_details_put_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.put(f'/users/{user.pk}/')
        self.assertEquals(response.status_code, 403)
    
    
    def test_status_code_users_details_delete_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.delete(f'/users/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 204)
        
    
    def test_status_code_users_details_delete_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.delete(f'/users/{user.pk}/')
        self.assertEquals(response.status_code, 403)    
      
      
class CartStatusCodeViewTestCase(TestCase):
    
    def test_status_code_cart_get_authorization(self):
        response = self.client.get('/users/cart/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_get_not_authorization(self):
        response = self.client.get('/users/cart/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_post_authorization(self):
        response = self.client.post('/users/cart/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_post_not_authorization(self):
        response = self.client.post('/users/cart/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_put_authorization(self):
        response = self.client.put('/users/cart/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_put_not_authorization(self):
        response = self.client.put('/users/cart/')
        self.assertEquals(response.status_code, 403)
    
    
    def test_status_code_cart_delete_authorization(self):
        response = self.client.delete('/users/cart/',HTTP_AUTHORIZATION=f'Token {token_login(self)}')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_delete_not_authorization(self):
        response = self.client.delete('/users/cart/')
        self.assertEquals(response.status_code, 403)
      
      
class CartDetailsStatusCodeViewTestCase(TestCase):
    
    def test_status_code_cart_details_get_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.get(f'/users/cart/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 200)
        
    
    def test_status_code_cart_details_get_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.get(f'/users/cart/{user.pk}/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_details_post_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.post(f'/users/cart/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 405)
        
    
    def test_status_code_cart_details_post_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.post(f'/users/cart/{user.pk}/')
        self.assertEquals(response.status_code, 403)
        
    
    def test_status_code_cart_details_put_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.put(f'/users/cart/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 405)
        
    
    def test_status_code_cart_details_put_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.put(f'/users/cart/{user.pk}/')
        self.assertEquals(response.status_code, 403)
    
    
    def test_status_code_cart_details_delete_authorization(self):
        token = token_login(self)
        user = user_details()
        response = self.client.delete(f'/users/cart/{user.pk}/',HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEquals(response.status_code, 405)
        
    
    def test_status_code_cart_details_delete_not_authorization(self):
        token_login(self)
        user = user_details()
        response = self.client.delete(f'/users/cart/{user.pk}/')
        self.assertEquals(response.status_code, 403)  
        
        