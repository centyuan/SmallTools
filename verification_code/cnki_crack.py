import time
from PIL import Image
from selenium import webdriver
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\softwareinstall\Tesseract-OCR\tesseract.exe'

def get_captcha(driver):
    print('截屏幕')
    driver.save_screenshot('screen_shot.png')  # 截屏
    check_code = driver.find_element_by_id('phoneCheckCode')  #
    loc = check_code.location  # 验证码左上角的坐标 x，y
    size = check_code.size  # 验证码大小,宽，高
    image = Image.open('screen_shot.png')
    print('截取对应图片')
    print('图片坐标',loc,size)
    # 856 682
    # 965 734
    rec = (loc['x'], loc['y'], size['width'] + loc['x'], size['height'] + loc['y'])  # 4个坐标。左上角、右下角
    rec = (856,682,965,734)  # 4个坐标。左上角、右下角
    print('截取對於',rec)
    captcha = image.crop(rec)  # 截取对应坐标图片
    captcha.save('captcha.png')


def recognize_captcha(file):
    gray = Image.open(file).convert('L')  # 灰度化
    w, h = gray.size
    data = gray.load()  # 数值化,内存加载二维点阵数据
    for i in range(w):
        for j in range(h):
            # 点阵里面的值，以128为界，置成0或者255.非黑即白
            if data[i,j] <128:
                data[i,j] = 0
            else:
                data[i,j] = 255
    return pytesseract.image_to_string(gray)

if __name__ == '__main__':
    url = 'https://my.cnki.net/Register/CommonRegister.aspx'
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=r'D:\all_project\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()  # 窗口最大化
    driver.implicitly_wait(5)  # 隐式等待5s
    time.sleep(3)
    check_code = driver.find_element_by_id('phoneCheckCode')  #
    src = check_code.get_attribute('src')
    print(src)

    get_captcha(driver)
    captcha = recognize_captcha('captcha.png')
    print(captcha)
    time.sleep(10)
    # driver.quit()

# https://www.lanqiao.cn/courses/364/learning/?id=1165
# https://www.lanqiao.cn/courses/1133/learning/?id=7186
# https://blog.csdn.net/qq_41937821/article/details/124037025