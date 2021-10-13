from django.urls import reverse
from rest_framework.test import APITestCase
import json
from apis.accounts.models import RememberAccount
from .models import MemoryLine

class MemoryLineTest(APITestCase):

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

    def createMemoryLine(self, typeId, name, description):
        self.client.post(
            "/api/v1/memory-lines/",
            data = {
                "title": name,
	            "type": typeId,
	            "description": description
            },
            format='json', 
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def memoryLineByType(self, typeId, page=1):
        return self.client.get(
            "/api/v1/memory-lines/?type=" + typeId + "&page=" + str(page),
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def updateMemoryLineName(self, memoryLineId, name):
        return self.client.put(
            "/api/v1/memory-lines/" + memoryLineId + "/",
            format='json',
            data={
                "title": name
            },
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def deleteMemoryLine(self, memoryLineId):
        return self.client.delete(
            "/api/v1/memory-lines/" + memoryLineId + "/",
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def detailMemoryLine(self, memoryLineId):
        return self.client.get(
            "/api/v1/memory-lines/" + memoryLineId + "/",
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def ownerMemoryLine(self, memoryLineId):
        return self.client.get(
            "/api/v1/memory-lines/" + memoryLineId + "/owner/",
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
        self.createAccount("typeuser", "type@hotmail.com")
        self.configAuthentication("typeuser")

    def test_create_memory_line(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")

        memoryLine = MemoryLine.objects.first()

        self.assertEqual(str(memoryLine.type.id), typeId)
        self.assertEqual(memoryLine.title, "Era 1")
        self.assertEqual(memoryLine.description, "Primeira era de mistborn")

    def test_memory_line_by_tag(self):
        
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Segunda era de mistborn")
        self.createMemoryLine(typeId, "Era 3", "Terceira era de mistborn")

        bodyMemoryLineByType = json.loads(self.memoryLineByType(typeId).content)

        self.assertEqual(bodyMemoryLineByType["next"], None)
        self.assertEqual(bodyMemoryLineByType["previous"], None)
        self.assertEqual(bodyMemoryLineByType["count"], 3)

        self.assertEqual(bodyMemoryLineByType["results"][0]["title"], "Era 3")
        self.assertEqual(bodyMemoryLineByType["results"][1]["title"], "Era 2")
        self.assertEqual(bodyMemoryLineByType["results"][2]["title"], "Era 1")

    def test_memory_line_by_tag_has_second_page(self):
        
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Segunda era de mistborn")
        self.createMemoryLine(typeId, "Era 3", "Terceira era de mistborn")
        self.createMemoryLine(typeId, "Era 4", "Terceira1 era de mistborn")
        self.createMemoryLine(typeId, "Era 5", "Terceira2 era de mistborn")
        self.createMemoryLine(typeId, "Era 6", "Terceira3 era de mistborn")
        self.createMemoryLine(typeId, "Era 7", "Terceira4 era de mistborn")

        bodyMemoryLineByType = json.loads(self.memoryLineByType(typeId).content)

        self.assertTrue(bodyMemoryLineByType["next"] != None)
        self.assertEqual(bodyMemoryLineByType["previous"], None)
        self.assertEqual(bodyMemoryLineByType["count"], 7)

        self.assertEqual(bodyMemoryLineByType["results"][0]["title"], "Era 7")
        self.assertEqual(bodyMemoryLineByType["results"][1]["title"], "Era 6")
        self.assertEqual(bodyMemoryLineByType["results"][2]["title"], "Era 5")
        self.assertEqual(bodyMemoryLineByType["results"][3]["title"], "Era 4")
        self.assertEqual(bodyMemoryLineByType["results"][4]["title"], "Era 3")
        self.assertEqual(bodyMemoryLineByType["results"][5]["title"], "Era 2")

    def test_memory_line_by_tag_second_page(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Segunda era de mistborn")
        self.createMemoryLine(typeId, "Era 3", "Terceira era de mistborn")
        self.createMemoryLine(typeId, "Era 4", "Terceira1 era de mistborn")
        self.createMemoryLine(typeId, "Era 5", "Terceira2 era de mistborn")
        self.createMemoryLine(typeId, "Era 6", "Terceira3 era de mistborn")
        self.createMemoryLine(typeId, "Era 7", "Terceira4 era de mistborn")

        bodyMemoryLineByType = json.loads(self.memoryLineByType(typeId, page=2).content)

        self.assertEqual(bodyMemoryLineByType["next"], None)
        self.assertTrue(bodyMemoryLineByType["previous"] != None)
        self.assertEqual(bodyMemoryLineByType["count"], 7)

        self.assertEqual(bodyMemoryLineByType["results"][0]["title"], "Era 1")

    def test_memory_line_by_tag_second_page_when_dont_have_more_than_six(self):
        self.createType("Mistborn")
        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Segunda era de mistborn")
        self.createMemoryLine(typeId, "Era 3", "Terceira era de mistborn")
        self.createMemoryLine(typeId, "Era 4", "Terceira1 era de mistborn")
        self.createMemoryLine(typeId, "Era 5", "Terceira2 era de mistborn")

        response = self.memoryLineByType(typeId, page=2)
        self.assertEqual(response.status_code, 404)

    def test_update_name_memory_line(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]
        self.updateMemoryLineName(memoryLine["id"], "Stormlight Archive")

        memoryLineUpdated = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        self.assertEqual(memoryLine["title"], memoryLineUpdated["title"])

    def test_delete_memory_line(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        self.deleteMemoryLine(memoryLine["id"])

        response = json.loads(self.memoryLineByType(typeId).content)
        self.assertEqual(response["next"], None)
        self.assertEqual(response["previous"], None)
        self.assertEqual(response["count"], 1)
        self.assertEqual(response["results"][0]["title"], "Era 1")

    def test_detail_memory_line(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        detail = json.loads(self.detailMemoryLine(memoryLine["id"]).content)

        self.assertEqual(detail["title"], "Era 1")
        self.assertEqual(detail["description"], "Primeira era de mistborn")
        self.assertEqual(detail["type"], typeId)
        self.assertEqual(detail["owner"]["username"], "typeuser")
        self.assertEqual(len(detail["some_participants"]), 0)

    def test_i_am_owner_of_memory_line(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]
        owner = json.loads(self.ownerMemoryLine(memoryLine["id"]).content)
        
        self.assertEqual(owner["owner"]["username"], "typeuser")

    def test_update_memory_line_name_from_another_account_should_not_work(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        self.createAccount("hoid", "hoid@hotmail.com")
        self.configAuthentication("hoid")
        
        request = self.updateMemoryLineName(memoryLine["id"], "Stormlight Archive")
        self.assertEqual(request.status_code, 403)

    def test_detail_memory_line_from_another_account_should_not_work(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(typeId, "Era 2", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        self.createAccount("hoid", "hoid@hotmail.com")
        self.configAuthentication("hoid")

        request = self.deleteMemoryLine(memoryLine["id"])
        self.assertEqual(request.status_code, 403)

    def test_delete_memory_line_from_another_account_should_not_work(self):
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(typeId, "Era 1", "Primeira era de mistborn")

        memoryLine = json.loads(self.memoryLineByType(typeId).content)["results"][0]

        self.createAccount("hoid", "hoid@hotmail.com")
        self.configAuthentication("hoid")

        request = self.detailMemoryLine(memoryLine["id"])
        self.assertEqual(request.status_code, 403)
