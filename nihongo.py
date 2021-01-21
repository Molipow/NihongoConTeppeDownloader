import requests

month = 7
year = 2019
current = 1
last = 354

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True
    

while current <last:
    url = f'http://nihongoconteppei.com/wp-content/uploads/{year}/{str(month).zfill(2)}/Beginners-con-Teppei{current}.mp3'
    if(is_downloadable(url)):
        print(url, True)
        r = requests.get(url, allow_redirects=True)
        open(f'Beginners-con-Teppei{current}.mp3', 'wb').write(r.content)
        current+=1
    else:
        print(url, False)
        month += 1
        if(month == 13):
            month = 1
            year += 1
            current -= 1
