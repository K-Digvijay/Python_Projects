import requests
import urllib.parse

class Request:
    def __init__(self,method,args):
        self.args = args
        self.method = method

request  = Request('GET',{'search':'java'})


if request.method == 'GET':
    search = urllib.parse.quote(request.args.get('search',''))
    url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
    response = requests.get(url)
    #print(response.json())

    if response.status_code==200: # 200 means the request was successful, 404 unauthorised
        data = response.json()
        for item in data.get('items',[]):
            volume_info = item.get('volumeInfo',{})
            title = volume_info.get('title','N/A')
            publisher = volume_info.get('publisher','N/A')
            published_data = volume_info.get('publishedDate','N/A')
            author= volume_info.get('authors',['N/A'])
            rating = volume_info.get('averageRating',['N/A'])
            image_link = volume_info.get('imageLink',{})
            image = image_link.get('thumbnail','N/A')



            print(title)
            print(publisher)
            print(published_data)
            print(author)
            print(rating)
            print(image)
    else:
        print(f"Error: {response.status_code}")

