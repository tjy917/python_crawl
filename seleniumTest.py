# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/
from selenium import webdriver

# the path of chromedriver where it is located has been added to the system enviroment.
driver = webdriver.Chrome()
driver.get("https://m-wise.eu/")
driver.find_element_by_link_text("Solutions").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()
print(html[:200])