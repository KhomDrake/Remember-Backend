from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, RememberAccount
import factory

class UserTestFactory(factory.Factory):
    class Meta:
        model = RememberAccount
    username = factory.Faker('email')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    bio = factory.Faker('text')
    birth_date = factory.Faker('date')

class UserTest(APITestCase):

    def createAccount(self, username, email):
        user = {
            "username": username, 
            "password": "testpassword", 
            "email": email,
            "name": "alkdjaldksaj",
            "photo": None,
            "nickname": "teste",
            "bio": "dksajldajdkl",
            "birth_date": "1997-09-25",
            "gender": "gender"
        }
        RememberAccount.create_account(**user)

    def createAccountApi(self, username, email):
        user = {
            "username": username, 
            "password": "testpassword", 
            "email": email,
            "name": "alkdjaldksaj",
            "nickname": "teste",
            "bio": "dksajldajdkl",
            "birth_date": "1997-09-25",
            "gender": "gender"
        }
        return self.client.post(
            "/api/v1/accounts/",
            data=user,
            format='json'
        )
        
    def login(self, username):
        url = reverse('api.accounts.login')
        data = {'username': username, 'password':'testpassword'}
        return self.client.post(url, data, format='json')

    def isEmailValid(self, email):
        return self.client.post(
            '/api/v1/accounts/verify_email/',
            data={
                "email": email
            },
            format='json'
        )

    def isUsernameValid(self, username):
        return self.client.post(
            '/api/v1/accounts/verify_username/',
            data={
                "username": username
            },
            format='json'
        )


    def test_create_user_model(self):
        User.objects.create_user("testuser", password="testpassword", email="testuser@test.com")

        # test create more 100 users
        for n in range(100):
            user = UserTestFactory()
            user.email = str(user.email) + str(n)
            user.save()

        self.assertEqual(User.objects.count(), 102)

        # Test create user unique email exception
        with self.assertRaises(Exception):
            for n in range(2):
                user = UserTestFactory()
                user.email = "teste@email.com"
                user.save()

    def test_login_api_with_username(self):
        """
        Teste do endpoint de login usando username
        """
        self.createAccount("testuser", "testuser@test.com")       
        response = self.login("testuser")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_api_with_email(self):
        """
        Teste do endpoint de login usando email
        """
        self.createAccount("testuser", "testuser@test.com")       
        response = self.login("testuser@test.com")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        request = self.createAccountApi("testuser", "testuser@test.com")
        self.assertTrue(request.status_code)
        requestLogin = self.login("testuser")
        self.assertEqual(requestLogin.status_code, status.HTTP_200_OK)

    def test_login_failed(self):
        self.createAccount("testuser", "testuser@test.com")
        requestLogin = self.login("testuser2")
        self.assertEqual(requestLogin.status_code, 401)

    def test_valid_email(self):
        request = self.isEmailValid("testuser@test.com")
        self.assertEqual(request.status_code, 200)

    def test_not_valid_email(self):
        self.createAccount("testuser", "testuser@test.com")
        request = self.isEmailValid("testuser@test.com")
        self.assertEqual(request.status_code, 400)

    def test_valid_username(self):
        request = self.isUsernameValid("testuser")
        self.assertEqual(request.status_code, 200)

    def test_not_valid_username(self):
        self.createAccount("testuser", "testuser@test.com")
        request = self.isUsernameValid("testuser")
        self.assertEqual(request.status_code, 400)

    
