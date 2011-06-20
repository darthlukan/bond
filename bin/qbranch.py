import urllib
import json

def google(user, target, message):
    query = message
    headers = defualt_headers
    opts = {'q': query, 'v': '1.0'}
    url = urllib.request.Request(google_search_url + "?" + urlencode(opts), headers=headers)
    print(url)
    page = urllib.request.urlopen(url)
    print(type(page))
    results = json.load(page.decode())
    page.close()
    print("Results")
    print(results)
    

