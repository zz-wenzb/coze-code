import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# 初始化WebDriver
# driver = webdriver.Chrome(service=Service(executable_path='D:\chrome\chromedriver-win64'))
driver = webdriver.Edge()

# 打开页面
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#task')

# # 查找元素，这里以按钮为例
# button = driver.find_element(By.CSS_SELECTOR, 'userhead_img_empty')
#
# # 模拟点击按钮
# button.click()

# 或者使用WebDriverWait等待元素可点击再点击
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'userhead_img_empty'))).click()
time.sleep(1)

# 输入电话号
input_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ttLogin__TTLogin_phone_input__H3tw7')))
input_box.clear()
input_box.send_keys('18525509251')
time.sleep(1)

# 发送验证码
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ttLogin__TTLogin_btn_getCaptcha__B8sx0'))).click()
time.sleep(1)

# 点击登录
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ttLogin__TTLogin_btn_login__RN3oy'))).click()
time.sleep(1)

# 获取所有 Cookie
all_cookies = driver.get_cookies()
# 筛选特定接口的 Cookie
target_domain = "100bt.com"  # 替换为目标接口的域名
target_path = "/"  # 替换为目标接口的路径

target_cookies = [cookie for cookie in all_cookies if
                  cookie['domain'] == target_domain and cookie['path'] == target_path]

# 打印特定接口的 Cookie
print("\nTarget Cookies:")
for cookie in target_cookies:
    print(cookie)

# 关闭浏览器
driver.quit()
