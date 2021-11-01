from text_converter import TextToSpeech


if __name__ == '__main__':

    converter = TextToSpeech()
    converter.language_selection()
    text = input('Enter text: ')
    converter.content = text
    converter.text_to_speech()
    file_name = input('With what file name you want to save it? ')
    converter.file_name_to_save = file_name
    converter.save()
    converter.listen_speech()
