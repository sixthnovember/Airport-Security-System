from flask import Flask, request

import requests 
import json

app = Flask(__name__)

api_key = "?key=AIzaSyCAPbMOfLX4QUeAqXGjVlAdlX2-TnHchyc" 
url = "https://vision.googleapis.com/v1/images:annotate" + api_key

bind_to = { 'hostname': "0.0.0.0", 'port': 8080 }

@app.route('/frame', methods=['POST'])
def post_request():
    if request.method == 'POST':
        if (request.is_json == True):
            
            # send request
            request_to_sent = json.loads(json.dumps(request.json))
            vision_response = send_to_vision(request_to_sent)
            
            # check for person in response
            if "responses" in vision_response:
                detected_entities = vision_response['responses'][0]['localizedObjectAnnotations']
                number_of_persons = 0
                for e in detected_entities:
                    if e['name'] == "Person":
                        number_of_persons += 1
                request_to_sent.update({'person-count': number_of_persons})
                if number_of_persons > 0:
                    # send to image analysis and face recogniton - which sends an response to collector
                    return send_to_other_services(request_to_sent)
                else:
                    return {"success": {"code": 200, "message": "No person detected!", "status": "OK"} }
            else:
                return {"error": {"code": 403, "message": "No response in received response!", "status": "DENIED"}}
            
        else:
            return {"error": {"code": 400, "message": "Not json!", "status": "DENIED"} }
    return {"error": {"code": 403, "message": "Request method was not POST", "status": "DENIED"} }
           
def send_to_vision(request):
    json_vision = {
        "requests": [
            {
                "image": {
                    "content": ""
                },
                "features": [
                    {
                        "maxResults": 10,
                        "type": "OBJECT_LOCALIZATION"
                    },
                ]
            }]
    }
    json_vision['requests'][0]['image']['content'] = request['image']
    response_vision = requests.post(url, json=json_vision)
    ret = json.loads(response_vision.text)
    return ret

def send_to_other_services(request): 
    request_ia = request
    request_fr = request
    request_ia['destination'] = "http://collector:8080/persons"
    request_fr['destination'] = "http://collector:8080/known-persons"
    try:
        requests.post("http://image-analysis:80/frame", json=request_ia)
        requests.post("http://face-recognition:80/frame", json=request_fr)
        return {"success": {"code": 200, "message": "At least one person detected! And successfully sent to image analysis and face recognition", "status": "OK"} }
    except:
        return {"error": {"code": 403, "message": "Could not send request to other services", "status": "DENIED"}}


@app.route('/', methods=['GET'])
def test():
    return {"success": {"code": 200, "message": "Welcome to the human detection service!", "status": "OK"} }

if __name__ == "__main__":
    app.run(host=bind_to['hostname'], port=int(bind_to['port']), debug=True)