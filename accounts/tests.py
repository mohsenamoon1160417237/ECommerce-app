from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
from .forms import UserRegistrationForm
from orderss.models import Order , OrderItem


class TestUserAccount(TestCase):

    def setUp(self):

        self.user_a = User.objects.create(username='mohsen' ,
                                          email='dramatic225@gmail.com')
        
        self.user_a_pw = 'mohsen1160417237'
        self.user_a.set_password(self.user_a_pw)
        self.user_a.save()
    

    def test_user_exists(self):

        users = User.objects.all()
        self.assertTrue(users.count() == 1)
        self.assertTrue(users.count() != 0)
    

    def test_user_username_and_email(self):

        user = get_object_or_404(User , username__iexact='mohsen')
        self.assertTrue(user is not None)
        self.assertTrue(user.email == 'dramatic225@gmail.com')
    

    def test_user_password(self):

        user = User.objects.all().first()
        self.assertTrue(user.check_password(self.user_a_pw))
    
    
    def test_user_login_redirect(self):

        login_url = settings.LOGIN_URL
        data = {'username' : 'mohsen',
                'password' : self.user_a_pw}
        login_redirect_url = settings.LOGIN_REDIRECT_URL
        response = self.client.post(login_url , data , follow=True)
        path_info = response.request.get('PATH_INFO')
        status_code = response.status_code
        self.assertEqual(path_info , login_redirect_url)
        self.assertEqual(status_code , 200)
    

    def test_user_registration(self):


        data = {'username' : 'hamed',
                 'email' : 'dramatic225@gmail.com' ,
                 'first_name' : 'mohsen' ,
                 'password' : 'mohsen1160417237',
                 'password2' : 'mohsen1160417237'}

        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    
    def test_user_registration_existing_username(self):

        data = {
            'username' : 'mohsen' ,
            'email' : 'dramatic225@gmail.com',
            'first_name' : 'mohsen',
            'password' : 'mohsen1160417237',
            'password2' : 'mohsen1160417237'
        }

        form = UserRegistrationForm(data=data)
        self.assertEqual(form.errors['username'][0] ,
                         'A user with that username already exists.')
        
    
    def test_user_registration_not_equal_passwords(self):

        data = {
            'username' : 'hamed',
            'email' : 'dramatic225@gmail.com' ,
            'first_name' : 'mohsen' ,
            'password' : 'sadfsdfsdf',
            'password2'  :'sdkfsdf'
        }

        response = self.client.post('/accounts/register/' , data=data)
        self.assertEqual(response.status_code , 200)
        form = UserRegistrationForm(data=data)
        self.assertEqual(form.errors['password2'][0] , 'Passwords do not match')
    
   
    def test_user_registration_wrong_email(self):

        data = {
            'username' : 'hamed',
            'first_name' : 'hamed',
            'email' : 'sdfsd',
            'password' : 'mohsen1160417237',
            'password2'  :'mohsen1160417237'
        }

        form = UserRegistrationForm(data=data)

        self.assertEqual(form.errors['email'][0] , 'Enter a valid email address.')
    

    def test_dashboard(self):

        dashboard_url = '/accounts/dashboard/{}/'.format(self.user_a.username)
        response = self.client.get(dashboard_url , 
                                    data={'username' : self.user_a.username})
        
        status_code = response.status_code
        self.assertEqual(status_code , 200)
        self.assertTrue(response.context['user'] is not None)
        self.assertTrue(response.context['user'].check_password(self.user_a_pw))

        

        