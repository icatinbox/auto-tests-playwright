import requests

class ClientApi:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        url = f'{self.base_url}/{path.lstrip('/')}'
        return self.session.request(method, url, **kwargs)
