from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Options = Options()
Options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=(ChromeDriverManager().install()), options=Options)

driver.get("www.google.com")
