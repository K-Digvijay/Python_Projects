import requests
import urllib.parse

class Request:
    def __init__(self,method,args):
        self.args = args
        self.method = method

request  = Request('GET',{'Search':'Galvin'})


if request.method == 'GET':
    search = urllib.parse.quote(request.args.get('search',''))
    url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
    response = requests.get(url)
    #print(response.json())

    if response.status_code==200: # 200 means the request was successful, 404 unauthorised
        data = response.json()
        print(data)