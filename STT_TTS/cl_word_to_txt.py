from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

el_list2 = []

def youtube_play():
  driver = uc.Chrome(use_subprocess=True)
  wait = WebDriverWait(driver, 20)
  url = 'https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%AA%85%EC%82%AC'
  driver.get(url)
  
  for j in range(128):
    xpath = "//*[@id='mw-pages']/div/div/div/ul/li"
    el_list = driver.find_elements(By.XPATH, xpath)
    for i in el_list:
      el = i.text
      el_list2.append(el)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[2]/div[2]/a[2]'))).click()

youtube_play()

with open('Word_list.txt', 'w', encoding='utf8') as f:
    for line in el_list2:
        f.write(line+'\n')
