from id_validator import validator

# 350821199202093329
# 350481199609013524
# 371526199311076026
# 362502199803207238
# 15093325400
# 支持大陆18,15位,港澳18位,台18位
print(validator.is_valid('362502199803207238'))  # 验证合法性
print(validator.get_info('362502199803207238'))  # 获取身份证d息(地区，出生日期,星座,生肖,性别)
# {'address_code': '362502', 'abandoned': 1, 'address': '江西省抚州地区临川市', 'address_tree': ['江西省', '抚州地区', '临川市'], 'age': 24, 'birthday_code': '1998-03-20', 'constellation': '双鱼座', 'chinese_zodiac': '寅虎', 'sex': 1, 'length': 18, 'check_bit': '8'}