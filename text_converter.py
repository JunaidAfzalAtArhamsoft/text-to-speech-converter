from playsound import playsound
from gtts import gTTS
import os.path


class TextToSpeech:

    def __init__(self, file_name_to_save='', content='I am text to speech converter.'):
        self.content = content
        self.language = 'en'
        self.speech = None
        self._file_name_to_save = file_name_to_save

    # ################################################################################# #

    @property
    def file_name_to_save(self):
        return self._file_name_to_save

    @file_name_to_save.setter
    def file_name_to_save(self, file_name):
        if os.path.isfile('{}.mp3'.format(file_name)):
            print(f'File with name "{file_name}" already exist.\nSelect operation:\n')
            operation = input('1- Override the file\n2- Save with other name\nSelect: ')
            if operation == '1':
                self._file_name_to_save = '{}.mp3'.format(file_name)
                print('\nFile is override.')
            elif operation == '2':
                file_name = input('Enter different file name: ')
                self.file_name_to_save = file_name
        else:
            self._file_name_to_save = '{}.mp3'.format(file_name)

    def text_to_speech(self):
        """
        Message: Covert the content in speech
        Parameters:
        Returns:
            None
        """
        print('Text is being converted into speech. please wait...')
        yes_no = False
        accent = 'co.uk'
        if self.language == 'ur':
            yes_no = True
            accent = 'co.in'
        speech = gTTS(text=self.content, slow=yes_no, lang=self.language, tld=accent)
        self.speech = speech
        print('Conversion is Done. Now you can listen it.')

    # ################################################################################# #

    def save(self):
        self.speech.save(self.file_name_to_save)

    # ################################################################################# #

    def listen_speech(self):
        """
        Message: Play the converted content
        Parameters:
            self:
        Returns:
            None
        """
        if os.path.isfile(self.file_name_to_save):
            playsound(self.file_name_to_save)
        else:
            print('No Such file.')

    # ################################################################################# #

    def language_selection(self):
        """
        Message: Take input and set language accordingly
        Parameters:
            self:
        Returns:
            None:
        """
        while True:
            print('Select language:\n1-English\n2-Urdu\nSelect: ')
            playsound('my_input.mp3')
            language = input()
            if language == '1':
                language = 'en'
                break
            elif language == '2':
                language = 'ur'
                break
            else:
                print('Invalid choice.')
        self.language = language
