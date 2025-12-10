from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,30)

# Visiting website
driver.get("https://www.flipkart.com")
time.sleep(2)
driver.maximize_window()

# Searching the product
search = wait.until(EC.presence_of_element_located((By.NAME,"q")))
search.send_keys("pixel 10 pro")
search.submit()
time.sleep(2)

# Selecting the desired product
product = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href,'jade-256')]")))
product.click()

# Jumping to the new opened window
driver.switch_to.window(driver.window_handles[1])

# Entering the pincode and checking for availability
pincode = wait.until(EC.element_to_be_clickable((By.ID, "pincodeInputId")))
pincode.clear()
pincode.send_keys("531113")
pincode.submit()

# Selecting the exchange option and adding the product to be exchanged
driver.execute_script("window.scrollBy(0,200);")
time.sleep(2)

exchange = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Buy with Exchange']")))
driver.execute_script("arguments[0].click();", exchange)

wait.until(EC.element_to_be_clickable((By.XPATH,"//*[normalize-space()='Search']"))).click()

# Searching the device to be exchanged
ph_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
ph_search.click()
ph_search.send_keys("Motorola Edge 50 fusion")
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[normalize-space()='MOTOROLA Edge 50 Fusion']"))).click()

# Selecting the Condition of the mobile
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Flawless (with Brand Box)']"))).click()
time.sleep(2)

# Going to the next and confirming the exchange
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Next']"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Confirm Exchange']"))).click()
time.sleep(2)

# Adding item to the cart
addtocart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Add to cart']")))
addtocart.click()

time.sleep(4)
driver.close()

print("Item Successfully added to cart")
