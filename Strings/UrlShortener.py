import random
class Codec:
    def __init__(self):
        self.refs = set()
        self.urls = {}
    def get_ref(self):
        s = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7))
        if s in self.refs:
            return self.get_ref()
        self.refs.add(s)
        return s
    
    def encode(self,longUrl) -> str:
        """Encodes a URL to a shortened URL.
        """
        print (longUrl)
        url, part = longUrl.rsplit('/', 1)
        new_url = f'{url}/{self.get_ref()}'
        self.urls[new_url] = longUrl
        return new_url

    def decode(self,shortUrl) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]