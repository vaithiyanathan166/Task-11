from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the target URL
    driver.get("https://jqueryui.com/droppable/")
    time.sleep(2)  # Wait for the page to load

    # Switch to the iframe that contains the draggable and droppable elements
    iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe)

    # Identify the draggable (white box) and droppable (yellow box) elements
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")

    # Perform drag and drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()
    time.sleep(2)  # Pause to observe the result

finally:
    # Close the browser
    driver.quit()
