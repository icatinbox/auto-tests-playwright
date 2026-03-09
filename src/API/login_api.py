import base64

class LoginApi:
    def __init__(self, client):
        self.client = client

    def login(self, login, password):
        payload = {
            "username": login, "password": base64.b64encode(password.encode("utf-8")).decode("utf-8")
        }
        return self.client.request('POST', '/login', json=payload)

    def get_token_from_response(self, response):
        token = response.text.replace('"', '').split(':')[1].strip()
        return token