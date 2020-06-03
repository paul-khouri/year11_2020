import urllib.request
url = 'http://catalogue.data.govt.nz/api/3/action/datastore_search?resource_id=daffe531-0e0e-4d69-b8c6-ebaaa532c966&limit=5&q=title:jones'  
x = urllib.request.urlopen(url)
print(x.read())
