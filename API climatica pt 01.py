import requests

r = requests.get('https://api.github.com/users/mateusyamaguti/repos')

# print(r.status_code)

# print(r.headers['content-type'])

# print(r.encoding)

# print(r.text)
# print(r.json())
# print(len(r.json()))
# print(r.json()[0]['name'])


# for item in range(len(r.json())):
#     print(r.json()[item]['name'])

