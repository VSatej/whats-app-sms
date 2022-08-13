import requests
import json

def whatsApp(messageParams, TO_PHONE_NUMBER, templateId):
    templateMapping = {
        1 : 'welcome',
        2 : 'otp'
    }
    url = "https://graph.facebook.com/v13.0/FROM_PHONE_NUMBER_ID/messages"

    payload = json.dumps({
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": TO_PHONE_NUMBER,
    "type": "template",
    "template": {
        "name": templateMapping[templateId],
        "language": {
        "code": "en_US"
        },
        "components": [
        {
            "type": "body",
            "parameters": messageParams
        }
        ]
    }
    })
    headers = {
    'Authorization': 'Bearer ACCESS_TOKEN',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)
    return
