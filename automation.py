from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = './chromedriver'

# service = Service(chrome_driver_path)
driver = webdriver.Chrome()

url='http://75.119.137.6:8069/web#action=298&cids=1&menu_id=170&model=product.template&view_type=kanban'
# driver = webdriver.Remote(command_executor=url,options=webdriver.DesiredCapabilities)
driver.session_id = 'e69fe1a7e407dda26a74cfce844475b3eefa4306'
# url = "http://75.119.137.6:8069/web#action=298&model=product.template&view_type=kanban&cids=1&menu_id=170"
# driver.get(url)

# article_count = driver.find_element(By.NAME, "#articlecount a")
# print(article_count.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("hashem", Keys.ENTER)

while(True):
    pass
