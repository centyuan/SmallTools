from selenium import webdriver
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'D:\softwareinstall\Tesseract-OCR\tesseract.exe'


def get_captcha(url, captcha_ele_id):
    # 截取验证码图片
    path = r'D:\all_project\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=path)
    browser.get(url)
    check_code = browser.find_element_by_id(captcha_ele_id)
    left, top = check_code.location.get('x'), check_code.location.get('y')  # 获取验证码左上角坐标
    # 验证码宽高
    width = check_code.size.get('width')
    height = check_code.size.get('height')
    right, bottom = width + left, height + top  # 获取验证码左下角坐标
    # 截屏,裁剪验证码并保持
    browser.get_screenshot_as_file('screen_pic.png')
    image = Image.open('resource/screen_pic.png')
    captcha = image.crop((left, top, right, bottom))
    captcha.save('resource/captcha.png')
    return True


def recognize_text(image):
    # 图像预处理
    # 1. 放大
    h, w = image.shape[:2]
    h, w = h * 2, 2 * 2  # 比例放大2倍
    img_g = cv2.resize(image, (w, h))
    # 2.图像去噪，边缘保留滤波
    blur = cv2.pyrMeanShiftFiltering(img_g, sp=8, sr=60)
    # 3.图像灰度化
    gray = cv2.cv2tColor(blur, cv2.COLOR_BGR2GRAY)
    # 4.图像二值化
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 5.形态学操作  获取结构元素  开操作
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 2))
    bin1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow('bin1', bin1)
    kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (2, 3))
    bin2 = cv2.morphologyEx(bin1, cv2.MORPH_OPEN, kernel)
    cv2.imshow('bin2', bin2)
    # 6.逻辑运算  让背景为白色  字体为黑  便于识别
    cv2.bitwise_not(bin2, bin2)
    cv2.imshow('binary-image', bin2)
    # tesseract 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')

if __name__ == '__main__':
    url = 'https://my.cnki.net/Register/CommonRegister.aspx'
    captcha_ele_id = 'phoneCheckCode'
    get_captcha(url, captcha_ele_id)
    captcha_pic = cv2.imread('resource/captcha.png')
    recognize_text(captcha_pic)