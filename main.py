# 샘플 Python 스크립트입니다.
import time
# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 2-1. 구글 검색창 검색어 입력 및 검색 실행
driver.get("https://google.com")
element = driver.find_element(By.NAME, 'q')
element.send_keys('맥도날드')
element.submit()

# 2-2. 네이버 검색창 검색어 입력 및 검색 실행
driver.get("https://www.naver.com/")
element = driver.find_element(By.ID, 'query')
element.send_keys('맥도날드')
element.submit()

time.sleep(10)