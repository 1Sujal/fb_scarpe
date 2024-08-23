from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # Optional, but may be useful for performance
chrome_options.add_argument("--no-sandbox")  # Required if running as root in some cases
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems

# Initialize WebDriver with options
driver = webdriver.Chrome('/home/sujal/Downloads/chromedriver-linux64/chromedriver', options=chrome_options)

# Open the Facebook login page
driver.get('https://mbasic.facebook.com/login')
time.sleep(3)

# Refresh the page (optional)
driver.refresh()

# Log in to Facebook
email = driver.find_element(By.NAME, 'email')
email.send_keys('email')  # Replace with your actual email

password = driver.find_element(By.NAME, 'pass')
password.send_keys('password')  # Replace with your actual password

login = driver.find_element(By.NAME, 'login')
login.click()

# Wait for login to process
time.sleep(4)

# Perform actions after login
test = driver.find_element(By.CLASS_NAME, 'bn')
test.click()

# Navigate to the desired page
driver.get('https://mbasic.facebook.com/officialroutineofnepalbanda?v=timeline&lst=100029424570188%3A100064557167145%3A1723769754&eav=Afa01KybogSCA4wXvwwBo8nVZnk8Tqds9xfD1Lj-Td3JjwNVVuwNHSOyrpZNVbTjsL4&paipv=0&refsrc=deprecated&_rdr#_=_')

# Find and print text from the first paragraph tag
texttt = driver.find_element(By.TAG_NAME, 'p')
textt = texttt.text
print(textt)

# Find image elements and print the URL of the second one if available
images = driver.find_elements(By.CLASS_NAME, 'img')
if len(images) >= 5:
    img_url = images[4].get_attribute('src')
    print("Sixth Image URL:", img_url)

driver.quit()
