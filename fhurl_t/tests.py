"""
>>> from django.test.client import Client
>>> import json
>>> c = Client()
>>>

>>> r = c.get("/login/with/")
>>> r.status_code
200
>>> r.templates[0].name
'login.html'
>>> 'This field is required.' in r.content
False

>>> r = c.post("/login/with/")
>>> r.status_code
200
>>> r.templates[0].name
'login.html'
>>> len(r.content.split("This field is required."))
3

>>> r = c.post("/login/with/", {"username": "john"})
>>> r.status_code
200
>>> len(r.content.split("This field is required."))
2

>>> r = c.post("/login/with/", {"username": "john", "password": "asd"})
>>> r.status_code
302
>>> r.content
''
>>> r["Location"]
'http://testserver/'

>>> r = c.get("/login/without/")
>>> r.status_code
200
>>> r.templates[0].name
'login.html'
>>> 'This field is required.' in r.content
False

>>> r = c.post("/login/without/")
>>> r.status_code
200
>>> r.templates[0].name
'login.html'
>>> len(r.content.split("This field is required."))
3

>>> r = c.post("/login/without/", {"username": "john"})
>>> r.status_code
200
>>> len(r.content.split("This field is required."))
2

>>> r = c.post("/login/without/", {"username": "john", "password": "asd"})
>>> r.status_code
302
>>> r.content
''
>>> r["Location"]
'http://testserver/'


>>> r = c.get("/with/http/")
>>> r.status_code
200
>>> r.templates[0].name
'login.html'

>>> r = c.post("/with/http/", {"username": "john", "password": "asd"})
>>> r.status_code
200
>>> r.content
'hi john'


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()