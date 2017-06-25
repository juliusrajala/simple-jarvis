import speech_recognition as sr
import logging

logger = logging.Logger("AssistantLogger", level=logging.INFO)
recognizer = sr.Recognizer()
catch_words = "hey listen"

def record_audio():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

def listen_initial():
    audio = record_audio()
    try:
        return recognizer.recognize_sphinx(audio)
    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
    except sr.RequestError as e:
        logger.warning("Recog error: {0}".format(e))

def external_recognition():
    '''
    In the future, this function will also call an indicator
    function to show current recording status.
    '''
    logger.warning('Recognizing intent using wit.ai')
    audio = record_audio()
    recognizer.recognize_wit('''TODO: API_KEY etc.''')

def main():
    listening = True
    while listening:
        logger.warning('Assistant is listening...')
        message = listen_initial()
        logger.warning('Assistant heard: {0}'.format(message))
        if catch_words in message:
            listening = False
            external_recognition()

if __name__ == "__main__":
    logger.warning("Calling main thread")
    main()
