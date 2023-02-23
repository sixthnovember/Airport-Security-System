from flask import Flask, request

import requests 
import json

app = Flask(__name__)

bind_to = { 'hostname': "0.0.0.0", 'port': 8080 }

@app.route('/frame', methods=['POST'])
def post_request():
    if request.method == 'POST':
        if (request.is_json == True):
            try:
                return send_to_human_detection(request.json) 
            except: 
                return {"error": {"code": 403, "message": "Request could not been sent to humand detection", "status": "DENIED"} }
        else:
            return {"error": {"code": 400, "message": "Not json!", "status": "DENIED"} }
    else:
        return {"error": {"code": 403, "message": "Request method was not POST", "status": "DENIED"} }

def send_to_human_detection(request):
    try: 
        requests.post("http://human-detection:8080/frame", json=request)
        return {"success": {"code": 200, "message": "Received a response from human detection", "status": "OK"} }
    except:
        return {"error": {"code": 403, "message": "POST to humand detection did not work", "status": "DENIED"} }


@app.route('/persons', methods=['POST'])
def persons():
    if request.method == 'POST':
        if (request.is_json == True):
            if "persons" in request.json:
                if request.json["persons"] != "":
                    return send_to_section(request.json)
                else:
                    return {"error": {"code": 403, "message": "Request could not been sent to section", "status": "DENIED"} }
            else:
                return {"error": {"code": 403, "message": "No persons in request", "status": "DENIED"} }
        else:
            return {"error": {"code": 400, "message": "Not json!", "status": "DENIED"} }
    else:
        return {"error": {"code": 403, "message": "Request method was not POST", "status": "DENIED"} }

def send_to_section(request):
    try: 
        requests.post("http://section:80/persons", json=request)
        return {"success": {"code": 200, "message": "Received a response from section", "status": "OK"} }
    except:
        return {"error": {"code": 403, "message": "POST to section did not work", "status": "DENIED"} }


@app.route('/known-persons', methods=['POST'])
def known_persons():
    if request.method == 'POST':
        if (request.is_json == True):
            if "known-persons" in request.json:
                if request.json["known-persons"] != "":
                    return send_to_alert(request.json)
                else:
                    return {"error": {"code": 403, "message": "No known person found", "status": "DENIED"} }
            else:
                return {"error": {"code": 403, "message": "No known persons in request", "status": "DENIED"} }
        else:
            return {"error": {"code": 400, "message": "Not json!", "status": "DENIED"} }
    else:
        return {"error": {"code": 403, "message": "Request method was not POST", "status": "DENIED"} }

def send_to_alert(request):
    try: 
        requests.post("http://alert:80/alerts", json=request)
        return {"success": {"code": 200, "message": "Received a response from alert", "status": "OK"} }
    except:
        return {"error": {"code": 403, "message": "POST to alert did not work", "status": "DENIED"} }

           
@app.route('/', methods=['GET'])
def test():
    return {"success": {"code": 200, "message": "Welcome to the collector service!", "status": "OK"} }

if __name__ == "__main__":
    app.run(host=bind_to['hostname'], port=int(bind_to['port']), debug=True)