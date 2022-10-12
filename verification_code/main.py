from PIL import Image
import pytesseract

# 指定tesseract.exe路径
pytesseract.pytesseract.tesseract_cmd = r'D:\softwareinstall\Tesseract-OCR\tesseract.exe'

image = Image.open('ocr_test.png')
text = pytesseract.image_to_string(image=image)
print(text)


