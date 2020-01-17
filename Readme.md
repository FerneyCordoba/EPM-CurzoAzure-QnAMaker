# Create

crea una base de conocimiento, cuyo origen puede ser de manera manua, una URL o archivo world, excel, .

    req = {
        "name": "QnA Maker FAQ",
        "qnaList": [
            {
                "id": 0,
                "answer": "You can use our REST APIs to manage your Knowledge Base. See here for details: https://westus.dev.cognitive.microsoft.com/docs/services/58994a073d9e04097c7ba6fe/operations/58994a073d9e041ad42d9baa",
                "source": "Custom Editorial",
                "questions": [
                    "How do I programmatically update my Knowledge Base?"
                ],
                "metadata": [
                    {
                        "name": "category",
                        "value": "api"
                    }
                ]
            }
        ],
    }

Ejemplo de url

        "urls": [
            "https://docs.microsoft.com/en-in/azure/cognitive-services/qnamaker/faqs"
        ],

Ejemplo de files

    "files": [
            {"fileName": "Preguntas%20Okibot%202020.docx",
            "FileUri": "https://github.com/FerneyCordoba/EPM-CurzoAzure-QnAMaker/raw/develop/Preguntas%20Okibot%202020.docx"
            }
        ]


# Update

    req = {
        'add': {
            'qnaList': [
                {
                    'id': 1,
                    'answer': 'You can change the default message if you use the QnAMakerDialog. '
                    + 'See this for details:  https://docs.botframework.com/en-us'
                    + '/azure-bot-service/templates/qnamaker/#navtitle',
                    'source': 'Custom Editorial',
                    'questions': [
                    'How can I change the default message from QnA Maker?'
                    ],
                    'metadata': []
                }
            ],
            'urls': []
        },
    }

# Publish

al publicar, se reponde con un json.

    {
        "result": "Success."
    }

podemos hacer un Postman, de la siguiente manera:

Hacemos Post a:

    https://curso-azure.azurewebsites.net/qnamaker/knowledgebases/d58ed0fe-c81e-4266-a9a2-3d495ede5af0/generateAnswer

en Header seleccionamos Bulk Edit y escribimos

    Content-Type:application/json
    Authorization: EndpointKey b0527ffb-4075-4b4e-910b-d1485c8fa67d

y en Body enviamos un raw en formato JSON así:

    {
        "question":"How do I programmatically update my Knowledge Base?"
        }
