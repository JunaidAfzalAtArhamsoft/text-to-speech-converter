from gtts import gTTS #google text to speech library, to convert text into speech
import webbrowser #To play saved .mp3 files

def speech_to_text(content):
    """
    This Function takes input text and convert it in speech and save to disk.
    Parameters:
        content (str): text to read
    Returns:
        str
    """
    print('Text is being converted into speech. please wait...')
    speech = gTTS(text=content, slow=False)
    speech.save('temp.mp3')
    print('Text is successfully converted into mp3: '
          '\nPress 1 to listen it or else to ignore.')
    if input() == '1':
        webbrowser.open('temp.mp3')
    else:
        print('Ok, file is save in mp3 format tou can listen it later.')


if __name__ == '__main__':

    choice = input('1-input text\n2-input file\nselect: ')
    if choice == '1':
        text = input('input text to listen:')
    if choice == '2':
        text_file = input('input file address to listen its content:')
        with open(text, 'r') as txt_file:
            text = txt_file.read()

    speech_to_text(text)

