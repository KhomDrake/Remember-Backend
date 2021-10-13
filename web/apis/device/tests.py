from django.urls import reverse
from rest_framework.test import APITestCase
import json
from .models import Device
from apis.accounts.models import RememberAccount

class DeviceTest(APITestCase):

    def addDevice(self, firebaseToken, device_id, name):
        return self.client.post(
            '/api/v1/device/add/',
            data={
                "device_id": device_id,
                "name": name,
                "os_version": "Android 10",
                "firebase_token": firebaseToken
            },
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def createAccount(self, username, email):
        user = {
            "username": username, 
            "password": "testpassword", 
            "email": email,
            "name": "alkdjaldksaj",
            "photo": None,
            "nickname": "teste",
            "bio": "dksajldajdkl",
            "birth_date": "1997-09-05",
            "gender": "gender"
        }
        RememberAccount.create_account(**user)

    def configAuthentication(self, username):
        data = {'username': username, 'password':'testpassword'}
        response = self.client.post(self.urlLogin, data, format='json')
        body = json.loads(response.content)
        authorization = body["access"]
        self.bearerToken = "Bearer " + authorization

    def setUp(self):
        self.urlLogin = reverse('api.accounts.login')
        self.createAccount("kelsier", "kelsier@hotmail.com")
        self.createAccount("hoid", "hoid@hotmail.com")
        self.configAuthentication("kelsier")

    def test_add_device_and_should_show(self):
        self.addDevice("token", "id 1", "Hoid Phone")

        device = Device.objects.filter(device_id="id 1").first()

        self.assertTrue(device != None)
        self.assertEqual(device.firebase_token, "token")
        self.assertEqual(device.name, "Hoid Phone")
        self.assertEqual(device.owner.username, "kelsier")

    def test_add_device_and_add_again_with_new_token_should_show_new_token(self):
        self.addDevice("token", "id 1", "Hoid Phone")
        self.addDevice("token 2", "id 1", "Hoid Phone 2")

        device = Device.objects.filter(device_id="id 1").first()

        self.assertTrue(device != None)
        self.assertEqual(device.firebase_token, "token 2")
        self.assertEqual(device.name, "Hoid Phone 2")
        self.assertEqual(device.owner.username, "kelsier")

    def test_add_device_and_add_again_with_new_user_should_other_user(self):
        self.addDevice("token", "id 1", "Hoid Phone")

        self.configAuthentication("hoid")

        self.addDevice("token 2", "id 1", "Hoid Phone 2")

        device = Device.objects.filter(device_id="id 1").first()

        self.assertTrue(device != None)
        self.assertEqual(device.firebase_token, "token 2")
        self.assertEqual(device.name, "Hoid Phone 2")
        self.assertEqual(device.owner.username, "hoid")

    def test_add_two_differents_devices(self):
        self.addDevice("token", "id 1", "Hoid Phone")

        self.configAuthentication("hoid")

        self.addDevice("token 2", "id 2", "Hoid Phone 2")
        device1 = Device.objects.filter(device_id="id 1").first()
        device2 = Device.objects.filter(device_id="id 2").first()

        self.assertTrue(device1 != None)
        self.assertEqual(device1.device_id, "id 1")
        self.assertEqual(device1.firebase_token, "token")
        self.assertEqual(device1.name, "Hoid Phone")
        self.assertEqual(device1.owner.username, "kelsier")

        self.assertTrue(device2 != None)
        self.assertEqual(device2.device_id, "id 2")
        self.assertEqual(device2.firebase_token, "token 2")
        self.assertEqual(device2.name, "Hoid Phone 2")
        self.assertEqual(device2.owner.username, "hoid")