from django.urls import reverse
from rest_framework.test import APITestCase
import json
from apis.accounts.models import RememberAccount
from .models import Type, TypeOwner

class TypeTest(APITestCase):

    def createType(self, name):
        dataType = {
            'name': name
        }

        return self.client.post(
            "/api/v1/type/", 
            dataType, 
            format='json', 
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def requestTypes(self, page=1):
        return self.client.get(
            "/api/v1/type/?page=" + str(page), 
            format='json', 
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def createMoreThanSixTypes(self):
        self.createType("mistborn")
        self.createType("stormlight archive")
        self.createType("warbreaker")
        self.createType("elantris")
        self.createType("mistborn 2")
        self.createType("mistborn 3")
        self.createType("mistborn 4")

    def createLessThanSixTypes(self):
        self.createType("mistborn")
        self.createType("stormlight archive")
        self.createType("warbreaker")
        self.createType("elantris")

    def updatePriorityType(self, id, priority):
        self.client.put(
            "/api/v1/type/" + id + "/priority/",
            data={
                "priority": priority
            },
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken,
        )

    def updatePriorityManyType(self, data):
        self.client.put(
            "/api/v1/type/many/",
            data=data,
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken,
        )

    def setUp(self):
        self.urlLogin = reverse('api.accounts.login')
        user = {
            "username": "typeuser", 
            "password": "testpassword", 
            "email": "type@hotmal.com",
            "name": "alkdjaldksaj",
            "photo": None,
            "nickname": "teste",
            "bio": "dksajldajdkl",
            "birth_date": "1997-09-05",
            "gender": "gender"
        }
        RememberAccount.create_account(**user)
        data = {'username': 'typeuser', 'password':'testpassword'}
        response = self.client.post(self.urlLogin, data, format='json')
        body = json.loads(response.content)
        authorization = body["access"]
        self.bearerToken = "Bearer " + authorization

    def test_create_type(self):
        responseType = self.createType("mistborn")

        self.assertEqual(Type.objects.count(), 1)
        self.assertEqual(Type.objects.first().name, "mistborn")
        self.assertEqual(TypeOwner.objects.count(), 1)
        self.assertEqual(responseType.status_code, 201)

    def test_add_types_and_get(self):
        self.createLessThanSixTypes()

        self.assertEqual(Type.objects.count(), 4)

        response = self.requestTypes()

        body = json.loads(response.content)

        self.assertEqual(body["count"], 4)
        self.assertEqual(body["next"], None)
        self.assertEqual(body["previous"], None)

        self.assertEqual(True, True)

    def test_add_more_than_six_types_get_types_check_if_has_next_not_null(self):
        self.createMoreThanSixTypes()

        self.assertEqual(Type.objects.count(), 7)

        response = self.requestTypes()

        body = json.loads(response.content)

        self.assertEqual(body["count"], 7)
        self.assertTrue(body["next"] != None)
        self.assertEqual(body["previous"], None)

        self.assertEqual(True, True)

    def test_get_page_two_with_more_than_six_types(self):
        self.createMoreThanSixTypes()

        response = self.requestTypes(page=2)
        body = json.loads(response.content)

        self.assertEqual(body["count"], 7)
        self.assertTrue(body["next"] == None)
        self.assertTrue(body["previous"] != None)

    def test_get_page_two_without_more_than_six_types(self):
        self.createLessThanSixTypes()
        response = self.requestTypes(page=2)
        self.assertEqual(response.status_code, 404)
        
    def test_add_type_and_change_priority(self):
        self.createLessThanSixTypes()
        body = json.loads(self.requestTypes().content)
        typeId = body["results"][3]["id"]
        self.updatePriorityType(typeId, 1)
        bodyAfterUpdate = json.loads(self.requestTypes().content)
        self.assertEqual(typeId, bodyAfterUpdate["results"][0]["id"])
        self.assertEqual(1, bodyAfterUpdate["results"][0]["priority"])
        
    def test_add_types_and_change_priority_many(self):
        self.createLessThanSixTypes()
        body = json.loads(self.requestTypes().content)
        dataUpdate = []
        priority = 10
        for type in body["results"]:
            dataUpdate.append(
                {
                    "id": type["id"],
                    "type": type["type"]["id"],
                    "priority": priority
                }
            )
            priority = priority - 1

        self.updatePriorityManyType(dataUpdate)

        bodyAfterUpdate = json.loads(self.requestTypes().content)
        results = body["results"]
        resultsAfterUpdate = bodyAfterUpdate["results"]

        self.assertEqual(results[0]["id"], resultsAfterUpdate[3]["id"])
        self.assertEqual(results[1]["id"], resultsAfterUpdate[2]["id"])
        self.assertEqual(results[2]["id"], resultsAfterUpdate[1]["id"])
        self.assertEqual(results[3]["id"], resultsAfterUpdate[0]["id"])

        self.assertEqual(resultsAfterUpdate[3]["priority"], 10)
        self.assertEqual(resultsAfterUpdate[2]["priority"], 9)
        self.assertEqual(resultsAfterUpdate[1]["priority"], 8)
        self.assertEqual(resultsAfterUpdate[0]["priority"], 7)

