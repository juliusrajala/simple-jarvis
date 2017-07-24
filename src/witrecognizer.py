'''
Simple wrapper around the speech_recognition modules
recognize functions.

Julius 2017
'''
import speech_recognition as sr

class WitRecognizer:
    '''
    Class initialized with api-key for wit.
    '''
    def __init__(self, api_key):
        self.api_key = api_key
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio):
        '''
        The actual beef of the class.
        '''
        try:
            return self.recognizer.recognize_wit(audio,
                                                 key=self.api_key,
                                                 show_all=True)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError:
            print("Could not request results from Wit.ai service.")
