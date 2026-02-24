import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    response = requests.post(URL, json = myobj, headers=HEADERS)
    parsed = json.loads(response.text)
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant = ("none", 0)

    scores = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if response.status_code == 200:
        for emotion in emotions:
            scores[emotion] = parsed["emotionPredictions"][0]["emotion"][emotion]

            if scores[emotion] > dominant[1]:
                dominant = (emotion, scores[emotion])

    scores["dominant_emotion"] = dominant[0]
    
    return scores

#print("result -> {}".format(emotion_detector("text to analyse")))