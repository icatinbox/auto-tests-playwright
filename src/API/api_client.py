import requests

class ClientApi:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        url = f'{self.base_url}/{path.lstrip('/')}'
        print(url, self.base_url)
        return self.session.request(method, url, **kwargs)
