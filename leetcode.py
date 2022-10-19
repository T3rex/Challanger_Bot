from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

PROBLEM = "/problems/letter-combinations-of-a-phone-number/"
LANGUAGE = "Python3"

driver.get(f"https://leetcode.com{PROBLEM}")
driver.implicitly_wait(30)

ques_title = driver.find_element(By.CLASS_NAME,"css-v3d350")
problem =driver.find_element(By.CSS_SELECTOR,'div[class="content__u3I1 question-content__JfgR"')

selection=driver.find_element(By.CSS_SELECTOR,'div[class="select__2iyW select-container__29U9"]')
selection.click()

selected_lang = driver.find_element(By.CSS_SELECTOR,f'li[data-cy="lang-select-{LANGUAGE}"]')
selected_lang.click()

print(ques_title.text)
print(problem.text)

