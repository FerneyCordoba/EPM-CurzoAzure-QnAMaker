# -*- coding: utf-8 -*-

import http.client
import urllib.parse
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace this with a valid subscription key.
subscriptionKey = os.getenv("KEY")  # YOUR SUBSCRIPTION KEY HERE'

# Represents the various elements used to create HTTP request path
# for QnA Maker operations.
host = 'westus.api.cognitive.microsoft.com'
service = '/qnamaker/v4.0'
method = '/knowledgebases/create'

'''
Formats and indents JSON for display.
:param content: The JSON to format and indent.
:type: string
:return: A string containing formatted and indented JSON.
:rtype: string
'''


def pretty_print(content):
    # Note: We convert content to and from an object so we can pretty-print it.
    return json.dumps(json.loads(content), indent=4)


'''
Sends the POST request to create the knowledge base.
:param path: The URL path being called.
:type: string
:param content: The contents of your POST.
:type: string
:return: A header that creates the knowledge base, the JSON response
:rtype: string, string
'''


def create_kb(path, content):
    print('Calling ' + host + path + '.')
    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
        'Content-Type': 'application/json',
        'Content-Length': len(content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request("POST", path, content, headers)
    response = conn.getresponse()
    # /knowledgebases/create returns an HTTP header named Location that contains a URL
    # to check the status of the operation in creating the knowledge base.
    return response.getheader('Location'), response.read()


'''
Checks the status of the request to create the knowledge base.
:param path: The URL path being checked
:type: string
:return: The header Retry-After if request is not finished, the JSON response
:rtype: string, string
'''


def check_status(path):
    print('Calling ' + host + path + '.')
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path, None, headers)
    response = conn.getresponse()
    # If the operation is not finished, /operations returns an HTTP header named Retry-After
    # that contains the number of seconds to wait before we query the operation again.
    return response.getheader('Retry-After'), response.read()


'''
Dictionary that holds the knowledge base.
The data source includes a QnA pair with metadata, the URL for the
QnA Maker FAQ article, and the URL for the Azure Bot Service FAQ article.
'''
req = {
    "name": "QnA Reditos Estructurada",

    # "urls": [
    #     "https://www.gruporeditos.com/prensa/noticias/"
    # ],
    "files": [
        {"fileName": "Preguntas%20Okibot%202020.docx",
         "FileUri": "https://github.com/FerneyCordoba/EPM-CurzoAzure-QnAMaker/raw/develop/Preguntas%20Okibot%202020.docx"
         }
    ]
}

# Builds the path URL.
path = service + method
# Convert the request to a string.
content = json.dumps(req)
# Retrieve the operation ID to check status, and JSON result
operation, result = create_kb(path, content)
# Print request response in JSON with presentable formatting
print(pretty_print(result))

'''
Iteratively gets the operation state, creating the knowledge base.
Once state is no longer "Running" or "NotStarted", the loop ends.
'''
done = False
while False == done:
    path = service + operation
# Gets the status of the operation.
    wait, status = check_status(path)
    # Print status checks in JSON with presentable formatting
    print(pretty_print(status))

    # Convert the JSON response into an object and get the value of the operationState field.
    state = json.loads(status)['operationState']

    # If the operation isn't finished, wait and query again.
    if state == 'Running' or state == 'NotStarted':
        print('Waiting ' + wait + ' seconds...')
        time.sleep(int(wait))
    else:
        done = True  # request has been processed, if successful, knowledge base is created

    # ver los resultados en https://www.qnamaker.ai/Home/MyServices
