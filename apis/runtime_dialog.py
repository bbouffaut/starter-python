import recastai
import config
import os
from utils import print_json

build = recastai.Build(os.environ['REQUEST_TOKEN'], 'en')
response = build.dialog({'type': 'text', 'content': 'Hello Recast'}, '123eb')

print('NLP Part:')
print_json(response.nlp.raw)
print('Conversation Part:')
print_json(response.conversation.raw)
print_json(response.messages.raw)
