
def main(args):
    import json
    import os
    import sys
    import nltk
    from watson_developer_cloud import NaturalLanguageUnderstandingV1
    from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, MetadataOptions

    natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=args.get("username"),
    password=args.get("password"),
    #username='de40afab-f410-4012-bb00-2d878ffc18f2',
    #password='oclD356nMDxV',
    version='2018-03-16')

    #text='I am travelling to Chennai from Bangalore. Book me flight.'
    #text='I am travelling from from Bangalore to Chennai. Book me flight.'
    text=args.get("input")
    nltk.download('punkt')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            entities=EntitiesOptions(
            #emotion=True,
            #sentiment=True,
            limit=5)
            #,metadata=MetadataOptions() # Metadata is only available for url and html not for text input
        )
        ,return_analyzed_text=True
    )
    words = nltk.word_tokenize(text)

    #print(json.dumps(response["entities"]))
    for entities in response["entities"]:
        print('entities*****\n',entities)
        print('entities.type',entities["type"])
        if(entities["type"] == "Location"):
            #print('inside loop***',entities["text"])
            index = words.index(entities["text"])
            #print(index)
            if(words[index-1]  == 'from'):
                #print('Source Location is',entities["text"])
                source = entities["text"]
            if(words[index-1]  == 'to'):
                    #print('Destination Location is',entities["text"])
                    destination = entities["text"]
        #else:
            #print('not a location')
    response.update({'Source':source})
    response.update({'Destination':destination})
    #print('response*****\n',json.dumps(response, indent=2))
    #return {'source ': source, 'destination': destination}
    return {'response': response}
