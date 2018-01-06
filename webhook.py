from flask import Flask, request, jsonify 
import json 

app = Flask(__name__) 
port = '5000' 

@app.route('/', methods=['POST']) 
def index(): 
    request_content = json.loads(request.get_data().decode('utf-8'))
    print(request_content)

    if (len(request_content['nlp']['entities']) > 0):
        room = request_content['nlp']['entities']['room'][0]['raw']
        content = 'Désolé, je ne connais pas la température dans ' + room
    else:
        content = "Désolé je n'ai rien compris"

    return jsonify( 
        status=200, 
        replies=[{ 
            'type': 'text', 
            'content': content, 
        }],
        conversation={ 
            'memory': {
                'room': {
                    'value': room,
                    'raw': room
                } 
            }
        } 
    ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
    print(json.loads(request.get_data())) 
    return jsonify(status=200) 
 
app.run(port=port)
