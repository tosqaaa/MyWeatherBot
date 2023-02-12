from googletrans import Translator


def trans_to_be(text):
    translator = Translator()
    translation = translator.translate(text=text, src='ru', dest='be')
    return translation.text

