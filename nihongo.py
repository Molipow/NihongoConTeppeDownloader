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
    

while current < last:
    if current == 214:
        ext = '.m4a'
    elif current == 244:
        print('http://nihongoconteppei.com/wp-content/uploads/2020/07/%E3%82%88%E3%82%93%E3%81%98%E3%82%85%E3%82%93%E3%81%95%E3%82%93%E3%81%A8%E3%81%86%E3%81%AE%E3%83%9E%E3%83%B3%E3%83%A2%E3%82%B9%EF%BC%81.mp3', True)
        r = requests.get('http://nihongoconteppei.com/wp-content/uploads/2020/07/%E3%82%88%E3%82%93%E3%81%98%E3%82%85%E3%82%93%E3%81%95%E3%82%93%E3%81%A8%E3%81%86%E3%81%AE%E3%83%9E%E3%83%B3%E3%83%A2%E3%82%B9%EF%BC%81.mp3', allow_redirects=True)
        open(f'Beginners-con-Teppei{current}.mp3', 'wb').write(r.content)
        current += 1
        continue
    else:
        ext = '.mp3'
    url = f'http://nihongoconteppei.com/wp-content/uploads/{year}/{str(month).zfill(2)}/Beginners-con-Teppei{current}{ext}'
    if(is_downloadable(url)):
        print(url, True)
        r = requests.get(url, allow_redirects=True)
        open(f'Beginners-con-Teppei{current}{ext}', 'wb').write(r.content)
        current+=1
    else:
        print(url, False)
        month += 1
        if(month == 13):
            month = 1
            year += 1
 
