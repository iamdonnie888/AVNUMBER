
from urllib.parse import urlencode

params = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

encoded_params = urlencode(params)
print(encoded_params)

base_url = 'https://20.climaxfun.pw/forum-68-'
tail_url = '.html'

def get_url(page):
    page = str(page)
    return base_url + page + tail_url

url = get_url(200)
print(url)
