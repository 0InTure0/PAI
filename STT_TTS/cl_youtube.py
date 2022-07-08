#https://dejavuqa.tistory.com/109
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def youtube_play(strmsg):
  youtube_find = strmsg.find("유튜브")
  play_find = strmsg.find("틀어줘")
  search_word  = "".join(list(strmsg)[youtube_find+3:play_find])
  email = "minchul90172@gmail.com\n"
  password = "hyunsu0223\n"
  driver = uc.Chrome(use_subprocess=True)
  wait = WebDriverWait(driver, 20)
  url = 'https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
  driver.get(url)
  wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
  wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-searchbox"))).send_keys(search_word)
  wait.until(EC.visibility_of_element_located((By.ID, "search-icon-legacy"))).click()
  wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img"))).click()
  wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ytp-fullscreen-button"))).click()
  global str2
  while True:
    str2 = input("값을 임력해주세요: ")  #음성인식 함수 집어넣고 꺼줘라는 말이 인식 될 때까지 반복
    pass
    if("꺼줘" in str2):
      break


str1 = "유튜브 잔잔한  틀어줘"
youtube_play(str1)
