import pyttsx3
from PyPDF2 import PdfReader

# Add your input file
pdfreader = PdfReader('contents.pdf') 

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

full_text = ""
for page in pdfreader.pages:
    text = page.extract_text()
    if text:  # Ensure text is not None
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + " "
        print(clean_text)

speaker.save_to_file(full_text, 'audio.mp3')

speaker.runAndWait()
speaker.stop()