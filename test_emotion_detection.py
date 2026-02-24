import unittest
from 

class TestEmotionDetection(unittest.TestCase): 
    def test_emotion_detection(self): 
        # Test case for positive sentiment 
        result_1 = emotion_detection('I love working with Python') 
        self.assertEqual(result_1['label'], 'SENT_POSITIVE') 
        # Test case for negative sentiment 
        result_2 = emotion_detection('I hate working with Python') 
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE') 
        # Test case for neutral sentiment 
        result_3 = emotion_detection('I am neutral on Python') 
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()