from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display  # Установите pyvirtualdisplay через pip

# Запускаем виртуальный дисплей
display = Display(visible=0, size=(1024, 768))
display.start()

options = Options()
options.set_headless()
options.set_preference('browser.cache.disk.enable', False)
options.set_preference('browser.cache.memory.enable', False)

# Укажите путь к вашему geckodriver, если он не в PATH
service = Service('/usr/local/bin/geckodriver', log_path='/tmp/geckodriver.log')

# Настроим драйвер Firefox
driver = webdriver.Firefox(service=service, options=options)

# Откроем страницу
driver.get("https://www.google.com")

# Выполним поиск
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Подождем немного
driver.implicitly_wait(10)

# Закроем браузер
driver.quit()

# Остановим виртуальный дисплей
display.stop()
