# pip install pytesseract
# pip install pdf2image

# Convert each page from a pdf file into an image and then extract the text from this image and save in a txt file. 

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# Convert PDF in image
from pdf2image import convert_from_path

pages = convert_from_path('file.pdf', 500, poppler_path = r'C:\Program Files\poppler-22.01.0\Library\bin')
for page in pages:
    page.save('out.jpg', 'JPEG')

#images = convert_from_path('file.pdf')
#images = convert_from_bytes(open('file.pdf', 'rb').read())
#print(images)


    img = Image.open("out.jpg")
    text = pytesseract.image_to_string(img)
    print(text)

    # Open text file in append mode 'a'
    text_file = open("data.txt", "a", encoding="utf-8")

    # Write String to File
    text_file.write(text)

    # Close file
    text_file.close()