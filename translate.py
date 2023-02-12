from googletrans import Translator

def trans(text, src, dest):
   translator = Translator()
   translation = translator.translate(text=text, src=src, dest=dest)
   return translation.text
    

if __name__ == "__main__":
    print(trans(input(), "ru", "be"))