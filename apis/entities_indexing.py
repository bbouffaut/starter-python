import requests
import config
import os

url = 'https://api.recast.ai/v2/users/' + os.environ['USER_SLUG'] + '/bots/' + os.environ['BOT_SLUG'] + '/entities'
print(url)
response = requests.get(url,
  headers={'Authorization': os.environ['DEVELOPER_TOKEN']}
)

print(response.text)
