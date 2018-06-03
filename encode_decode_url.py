class Codec:
    base_url = 'http://tinyurl.com/'
    #### static member
    d = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.base_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """


d = Codec()
d2 = Codec()

d.d['1'] = 2

print(d2.d)


def minus(i):
    i -= 1


i = 10
minus(i)
print(i)  ######## <<<<<<<<<<<print 10

z = []


def minus_list(z):
    z.append(10)


minus_list(z)
print(z)

import random


class Codec:
    base_url = 'http://tinyurl.com/'
    d = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = "".join(random.sample(string.letters + string.digits, 6)).capitalize()
        self.d[key] = longUrl
        print(self.d)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.d.get(shortUrl.split("/")[-1], None)


p = Codec()
p.encode("https://leetcode.com/problems/design-tinyurl")
p, d
