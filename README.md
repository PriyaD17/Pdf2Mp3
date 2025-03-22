# PDF to MP3 Converter

This project converts PDF documents into MP3 audio files using text-to-speech (TTS) technology. It is designed to make reading accessible and convenient by turning text into audio.

## Features

- Extracts text from PDF files.
- Converts extracted text to speech.
- Outputs MP3 audio files.
- Simple and user-friendly interface.

## Requirements

- Python 3.7 or higher
- Required Python libraries:
    - `PyPDF2`
    - `pyttsx3`

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/yourusername/pdf2mp3.git
     cd pdf2mp3
     ```

2. Set up a virtual environment:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Install dependencies:
     ```bash
     pip install pyttsx3 pypdf2
     ```

4. If you encounter issues with `pyttsx3` installation, ensure you have the necessary system dependencies. For example, on Linux, you may need to install `espeak`, `libespeak1`, or other TTS-related libraries:
     ```bash
     sudo apt-get install espeak
     ```

## Usage

1. Place your PDF file in the project directory.
2. Run the script:
     ```bash
     python pdf2mp3.py input.pdf output.mp3
     ```
    Replace `input.pdf` with the name of your PDF file and `output.mp3` with the desired name for the audio file.

3. The MP3 file will be generated in the same directory.

## Acknowledgments

- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech conversion.
- Inspired by the need for accessible reading solutions.