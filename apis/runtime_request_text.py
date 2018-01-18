import recastai
import config
import os
from utils import print_json

request = recastai.Request(os.environ['REQUEST_TOKEN'], 'en')
response = request.analyse_text('Hello Recast')

print_json(response.raw)
