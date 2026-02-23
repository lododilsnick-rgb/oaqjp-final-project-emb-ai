import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

def emotion_detector(text_to_analyse):
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    response = requests.post(URL, json = myobj, headers=HEADERS)
    print("response-> {}".format(response.text))
    parsed = json.loads(response.text)
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant = ("none", 0)

    scores = {
        'anger': 0,
        'disgust':0,
        'fear': 0,
        'joy': 0,
        'sadness': 0,
        'dominant_emotion': dominant[0]
    }

    if response.status_code == 200:
        for emotion in emotions:
            scores[emotion] = parsed["emotionPredictions"][0]["emotion"][emotion]

            if scores[emotion] > dominant[1]:
                dominant = (emotion, scores[emotion])

    scores["dominant_emotion"] = dominant[0]
    
    return scores

print("result -> {}".format(emotion_detector("text to analyse")))