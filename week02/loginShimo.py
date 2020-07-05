from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('18307985226')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('jiangbin524946')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(text(),"立即登录")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()