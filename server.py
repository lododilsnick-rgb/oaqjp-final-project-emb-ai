"""Emotion detection web app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Handle web app request"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """Handle emotion detector request"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    formatted = "Invalid input text"

    if(text_to_analyze is not None and text_to_analyze.strip()):
        # Pass the text to the emotion detector function and store the response
        response = emotion_detector(text_to_analyze)
        formatted = f"""
For the given statement, the system response is 'anger': {response['anger']}, 
'disgust': {response['disgust']}, 'fear': {response['fear']}, 
'joy': {response['joy']} and 'sadness': {response['sadness']}. 
The dominant emotion is {response['dominant_emotion']}"""

    return formatted

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
