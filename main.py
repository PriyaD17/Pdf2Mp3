import pyttsx3
from PyPDF2 import PdfReader

# Open the PDF file
pdfreader = PdfReader('contents.pdf')

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Extract and concatenate text from all pages
full_text = ""
for page in pdfreader.pages:
    text = page.extract_text()
    if text:  # Ensure text is not None
        clean_text = text.strip().replace('\n', ' ')
        full_text += clean_text + " "
        print(clean_text)

# Save the concatenated text to an audio file
speaker.save_to_file(full_text, 'audio.mp3')

# Run the text-to-speech engine
speaker.runAndWait()
speaker.stop()
print("Extracted text length:", len(full_text))
print("First 100 characters of text:", full_text[:100])