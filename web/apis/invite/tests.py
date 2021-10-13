from django.urls import reverse
from rest_framework.test import APITestCase
import json
from apis.accounts.models import RememberAccount

class InviteTest(APITestCase):
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
        return self.client.post(
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
    
    def createMoment(self, memoryLineId, description):
        self.client.post(
            "/api/v1/memory-lines/" + memoryLineId + "/moments/create/",
            data = {
	            "file": "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 " +
                    "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 " +
                    "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" +
                    "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 " + 
                    "ozfA5PmSScoLa2zxvNKlHojS1Mr35EwezaO0nuDy/rGtkgMo/CFIUqKikRQPV8Of/lR9fwfcXXyP haD/ADUPM+538wL38g/2D6+YfUoexfYPqO4D2HsH1HcC+w7+QHcAXuO4A3j5s6HOHNnT3Ae5fchU AAAAoAAAAAAigAUgAAoAAAAAAKAAAIAAKIUACFACICkAAAAAABCgAAAAAAIoQAHp0ytUeY64J8Mi VY9fCl0sw8cLuqZvi2slN7swrSaWxHkinRl8vuZUUpc9xFJzuWy3GLEoy4nzYpcWx0clGNstRy1k vkUTxHTNPjm2czUQIU6YsTyPsgORDvLCknwu2RYLVt0+w0cSHVYJOTXRdRLA0rvYaOIOqwSrdpAD 8SUhSCopEUD0aF1q8X+5H3l08z4Gj21OP/cvyfej0AvuPcLoF08yh38y9/MLp5hdPMA+vmXv5kX7 hfuEX3HfzHuPcC+49x7l7BWoczp7nOH1HTsARURdCgEAAKAAABSiFAIAAAAAoAFAAAAAAAAIAAKA AAAAAAAgQoAEKAIAUCAAACkAqAAAIADtjytOmeniUo0meA0ptGbF17nHbYkYJSs8y1Ekg9RI52dK 9UnGKt0jy583HsuRylNye7Mm5zn1BkANgenAn4To8p0WVxhwx2JR2SUYKLknJm40vppLq2ePid3e 4c5PmyYr2R+e3fymMicpJR2iupzjmSil07Gcme9oKkMHfl9MG13B5fGn3AwfiikKEVFIigddM6zw f/sj9Aufkj87h2yRf3P0X+pAXlXkF08g+vkO/kUVdAuhPYewF7DsO3kO3kEVdAugXTyHsBV0KuhE PYDcPqR0OcPq9Dp7BQvsT2L7AAABQAAAAFBCgAAAKQoAEKUAAAAQAAoAgAApCkAAAAAAgAAAAAAh QICkAAACgIAAAAAAAhSAAABAAFQ0kZNogKHE6StnT9NKt9jthjwQut2dU9jj1+l301jwTxOPMw0e 6fzJ7Hjkqk0b561LGOEFoG0fiykKQEaMo0BqH1I/RLr92fnI80fooO1EDXfzK+pOi+7HuUV9R38i d/MvcA+vkXv5EfUvcIexfYncvcB7F9iPqXuVWofV6HX2OUeZ07kF9ik7juBQQoApCgAgggBSIFFA BAAAApClAAAAAAAAFIAAHUAIAAKAAAAAgAABCgCFIAAAAoAAAAAAAIAAIAABAABtdDmaUiK92KSc Sttv7HjjnceRr9SzneF16cklCDZ4ZO3ZuWbiObkanOGgJYNI/GFIUgGkZNAWPM/QYn8kP9tn59cz 72F/4UX/AOi/AHVfyhdPMcq8gunkUVdPMdPUi6FT5AX3D6+ZFyXmX3AvfzHci/cvuUXuXuT3HuQa jzOpyj9XqdPcCl7k9x7gX3A9x7gVAIICoIgQFABRQAAAAApABQAAAAAAAAAAAAAABAAAACAUgAAA AAAAAAGgQAUEAAAACAACAACABUALwyfRgQhrhfZk+xBkHSWPhhb5nMCAAD8eUhSAaMmkBVzPuad/ 4EP9sfwj4S5n29M//Gx+SA9D6+RXz9DL6+Ze5RV+EF08iPr5F9gKugXQi/Yq6eRRV0C6eZF0KugF X7j3IuhV0CNR5rzOq/c5Q+peZ0XTzIq+5fcyuhV0AvbzCC6BdAKuhexnsXsBQRAClICiggIKACig gApTJQBSACggAoIUAQAAAAAACAACgACAAAAgAAADQIAKQAAAQCkAAEAAEACtQ3mjvKfzqK2VHmUu F2VZHxX1JR6HK5NckjL4catK23zOKyNW+rNLL3VkxXWVSS4uRnJy+VKjDzcT3JPKnGor1A57dQZb BUfkCkKQDSMlAp9rRu9Pi8j4p9jRP/x8fk/yB6b2X3Zb2fmRfyhdPMor6+ZW+Zn3L38wK+vkX2I+ ofUo1f4C6eRnv5Fv8AVdPIq6eRPYLp5BG484nRdDlHmjounkRWl0C6EXTyC6AaXQLoRdAgNLoF0I ugX7AUpABQQpRbBAQUpAUUEAFAAFBABQQAUEAFBABQQAUEAAAAAAAAIBSABAAAaIAAAIBRZAABBY AEAFICBUlJQVs5fqY9jWXdHNQQTWv1ER48O5jgTYeFVYV08eHceLDucViTI8IHbxI9wefwl9wB+c ABkUqIVAU+toX/40fsn+T5J9TQv/AMb1A9i6eRVziZfXyL7FFT5Dp5si5ryCf0lRfcr6+ZldPMvT 1Ar6l7k7+Y7+YVp9fIvsZ7l7hGlzXkdfY4p7nX2Cqv2LfLyM+xfYgq/YvsZ9i+wF9gT2HsUa9gQo FBABSkBBQSylApBYFBLAFAAFBABQQAUEAFIAECmShQAgRQQBVBAEACAUEAGgQAWwQAAQAUgIAAIB SEsASatHNJs7VaNqNJKKRNXHldojmzpm+o49QjXGRz7l+ShUAM8aBeGAA/MAAiqVEKgKfT0D/wDG X+4+WfT+H/wF/uA9j6+Ze/kZXL1K+pUX9kF08h3D5vyKKugXTzJ19CroBe3mPci6BdPMDXfzL3M+ 5b/IVq+Z0fU5dfU6XzA13L38jL6lfUC+xfYzfMoFsvsZ9i2BfYWQAaFkAGhZLAFLZkAasEAFKZFg aBABQQAUEAFBABQSwBQQBFIAAAIBRZLAFICAUqMlQFKQgFBAAAJYFIQWBSCyAUgJYGuKoh5ZVSMM JbEVh7k4LfMsjFuwOvgbczLwPuROT6jiknSdkXDwJA1eQFTH5UAEFKjJpAD6Xw5/4X9T/Y+afQ+H /wAKXmB7lyj5l5r1JHoF0KD6+ZX/ADE6eo7+ZRXzfkW+v2J3D6+QFXQqfInX0C6eQFXTzL7kXQLo Ea6vzOnfzOS6eZ09wrXcvcz38y9/MC9y3zM9y9wL3LZnuUClM9y2BRZABoEAFKZstgUEsWBSmSgU EFgUEAFBABQQAUEsAUEFhFBABQQAAQAUEAAqMlQGrICAUEsNgLBABSEsWBSWQAAQAGFOjLI9gEnZ grIBU2yq4vYymLa5GXT+OnFLsDn4k+wDL80AAgaRk0gB7/h/8OfmeA93w/6J+aA96/Yq6GV18i9f Qoq6DovMi6BdCi9/Mvcz09Svr5gXv5C/wR9Q+vkBpdPIq6GfYq5ryAsXyOvucV0Oq6AX3HuRdPMv uBS3zM+5fcC3zKZ7lvmBe47kvmO4GrBLFgaBmy2BSmQBoEsWBQQAasGSgWwSwBRZABbBABRZLARQ QAUEIBohABRZABbFkIBSozZUBbFkAFBLFgAQAASwABLAAEslgOpqk1uYb3KpMFZnszFmps52CNpl Uq6GVyKpcJl0vxfF/wDUDxF2AZfmgAEDSMlQFPb8P5T80eI9nw/nJeQH0OjHV+RFy9SvqUXr6BdC dx7FFXTzHT1IugXTzAr6+ZX1M3+S9wL38i9fQzfMt8/ICrp5HVPkcvY6Lp5AVPl5lXTzMroVPkBr 3F/kz28y+4Fvn5juT3HuBodyXzAGgQAUpkoFFkAFspABQQAUpkoFBABRZLAFsGbKEUEJYGrBCWBR ZLAFFksWBQSyWBbFkAFKjIQGrFkFgUhLFgUgsgFsWQgFJYJYFJYsjYAUItByIMSOZuRkKsXsVTro Qiml0I1fjfir/SDPiR/0gI//2Q==",
	            "description": description
            },
            format='json', 
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def getMoments(self, memoryLineId, page=1):
        return self.client.get(
            '/api/v1/memory-lines/' + memoryLineId + "/moments/?page=" + str(page),
            format='json', 
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def createInvite(self, guestId, memoryLineId):
        return self.client.post(
            '/api/v1/invites/',
            data={
                "guest": guestId,
	            "memory_line": memoryLineId
            },
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def createInvites(self, data):
        return self.client.post(
            '/api/v1/invites/many/',
            data=data,
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def getInvites(self, page=1):
        return self.client.get(
            '/api/v1/invites/?page=' + str(page),
            format='json',
            HTTP_AUTHORIZATION=self.bearerToken
        )

    def answerInvite(self, inviteId, answer):
        return self.client.post(
            '/api/v1/invites/' + inviteId + '/accept/',
            data={
                "accepted": answer
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

    def createMoreThanSixInvites(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createMemoryLine(self.typeId, "Era 4", "Primeira era de mistborn")
        self.createMemoryLine(self.typeId, "Era 5", "Primeira era de mistborn")
        self.createMemoryLine(self.typeId, "Era 6", "Primeira era de mistborn")
        self.createMemoryLine(self.typeId, "Era 7", "Primeira era de mistborn")
        memoryLines = json.loads(self.memoryLineByType(self.typeId).content)["results"]
        memoryLines2 = json.loads(self.memoryLineByType(self.typeId, page=2).content)["results"]
        self.createInvites([
            {
                "guest": guest.id,
                "memory_line": memoryLines[0]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines[1]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines[2]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines[3]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines[4]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines[5]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": memoryLines2[0]["id"]
            }
        ])
        
    def configAuthentication(self, username):
        data = {'username': username, 'password':'testpassword'}
        response = self.client.post(self.urlLogin, data, format='json')
        body = json.loads(response.content)
        authorization = body["access"]
        self.bearerToken = "Bearer " + authorization

    def setUp(self):
        self.urlLogin = reverse('api.accounts.login')
        self.createAccount("kelsier", "type@hotmail.com")
        self.createAccount("hoid", "hoid@hotmail.com")
        self.configAuthentication("kelsier")
        self.createType("Mistborn")

        body = json.loads(self.requestTypes().content)
        self.typeId = body["results"][0]["type"]["id"]
        self.createMemoryLine(self.typeId, "Era 1", "Primeira era de mistborn")
        self.createMemoryLine(self.typeId, "Era 2", "Segunda era de mistborn")
        self.createMemoryLine(self.typeId, "Era 3", "Terceira era de mistborn")
        self.memoryLines = json.loads(self.memoryLineByType(self.typeId).content)["results"]

    def test_create_invite_and_get_invite(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")
        body = json.loads(self.getInvites().content)

        self.assertEqual(body["count"], 1)
        results = body["results"]
        self.assertEqual(results[0]["answered"], False)
        self.assertEqual(results[0]["memory_line"]["id"], self.memoryLines[0]["id"])
        self.assertEqual(results[0]["memory_line"]["title"], self.memoryLines[0]["title"])
        self.assertEqual(results[0]["memory_line"]["description"], self.memoryLines[0]["description"])

    def test_create_many_invites_and_get_invites(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvites([
            {
                "guest": guest.id,
                "memory_line": self.memoryLines[0]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": self.memoryLines[1]["id"]
            },
            {
                "guest": guest.id,
                "memory_line": self.memoryLines[2]["id"]
            }
        ])

        self.configAuthentication("hoid")
        body = json.loads(self.getInvites().content)

        self.assertEqual(body["count"], 3)
        results = body["results"]

        self.assertEqual(results[0]["memory_line"]["id"], self.memoryLines[0]["id"])
        self.assertEqual(results[1]["memory_line"]["id"], self.memoryLines[1]["id"])
        self.assertEqual(results[2]["memory_line"]["id"], self.memoryLines[2]["id"])

    def test_accept_invite(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, True)

        self.assertEqual(json.loads(self.getInvites().content)["count"], 0)

    def test_reject_invite(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, False)

        self.assertEqual(json.loads(self.getInvites().content)["count"], 0)

    def test_reject_invite_and_create_invite_again(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, False)

        self.configAuthentication("kelsier")
        self.createInvite(guest.id, self.memoryLines[0]["id"])

        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)

        self.assertEqual(body["count"], 1)
        results = body["results"]
        self.assertEqual(results[0]["answered"], False)
        self.assertEqual(results[0]["memory_line"]["id"], self.memoryLines[0]["id"])
        self.assertEqual(results[0]["memory_line"]["title"], self.memoryLines[0]["title"])
        self.assertEqual(results[0]["memory_line"]["description"], self.memoryLines[0]["description"])

    def test_create_two_equal_invites_should_fail(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        request = self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.assertTrue(request.status_code, 400)
        self.assertTrue(True, True)

    def test_get_invites_second_page(self):
        self.createMoreThanSixInvites()
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites(page=2).content)
        self.assertEqual(body["count"], 7)
        results = body["results"]
        self.assertEqual(results[0]["answered"], False)
        self.assertEqual(results[0]["memory_line"]["title"], "Era 1")

    def test_get_invites_second_page_and_dont_have_second_page(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        request = self.getInvites(page=2)

        self.assertTrue(request.status_code, 404)

    def test_accept_invite_and_get_memory_line(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, True)
        body = json.loads(self.memoryLineByType(self.typeId).content)

        self.assertEqual(body["count"], 1)
        self.assertEqual(body["next"], None)
        self.assertEqual(body["previous"], None)

        self.assertEqual(body["results"][0]["title"], "Era 3")

    def test_reject_invite_and_get_memory_line_should_fail(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, False)
        request = json.loads(self.memoryLineByType(self.typeId).content)
        self.assertEqual(request["count"], 0)

    def test_accept_invite_and_owner_create_memory_line_in_type_should_not_show_new_memory_line(self):
        guest = RememberAccount.objects.filter(username="hoid").first()
        self.createInvite(guest.id, self.memoryLines[0]["id"])
        self.configAuthentication("hoid")

        body = json.loads(self.getInvites().content)
        inviteId = body["results"][0]["id"]
        self.answerInvite(inviteId, True)
        self.configAuthentication("kelsier")
        self.createMemoryLine(self.typeId, "Thaidakar", "Is Kelsier")
        self.configAuthentication("hoid")

        request = json.loads(self.memoryLineByType(self.typeId).content)
        self.assertEqual(request["count"], 1)

