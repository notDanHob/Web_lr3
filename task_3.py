import requests

url = 'https://httpbin.org/get'
url_y = 'https://www.youtube.com/results'
params = {'search_query':'funny cats'}
response = requests.get(url)
response_y = requests.get(url_y, params= params)

print(response_y.url)