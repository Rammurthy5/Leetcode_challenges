class Codec:
    def __init__(self):
        self.urldb = {}
        self.codedb = {}
        self.chars = string.ascii_letters + string.digits
        
    def getCode(self):
        return ''.join([random.choice(self.chars) for q in range(6)])
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urldb:
            return self.urldb[longUrl]
        code = self.getCode()
        tiny = "http://tinyurl.com/"+code
        self.urldb[longUrl] = code
        self.codedb[code] = longUrl
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codedb.get(shortUrl, None)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
