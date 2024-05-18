from selenium import webdriver

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars") # disables the infobars
  options.add_argument("start-maximized") # open Browser in maximized mode
  options.add_argument("disable-dev-shm-usage") # disables the use of /dev/shm
  options.add_argument("no-sandbox") # disables the sandbox
  options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disables the automation
  options.add_argument("disable-blink-features=AutomationControlled") # disables the automation
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())