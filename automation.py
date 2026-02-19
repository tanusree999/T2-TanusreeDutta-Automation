import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://dev.octopussaas.com/auth")
time.sleep(5)
#login
driver.find_element(By.XPATH, "//input[@id='login-email']").send_keys("henry@test.com")
driver.find_element(By.XPATH, "//input[@id='login-password']").send_keys("Nayan123!@")
driver.find_element(By.XPATH, "//button[text()='Log In']").click()
time.sleep(5)
#click on Add new button
driver.find_element(By.XPATH, "//h6[text()='Add New']").click()
time.sleep(2)
#create generator
driver.find_element(By.XPATH, "//li[text()='Generator']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Enter generator name']").send_keys("Tanusree Dutta")
driver.find_element(By.XPATH, "//input[@placeholder='Enter internal account number']").send_keys("12345678912345")
driver.find_element(By.XPATH, "//button[@type='submit']").submit()
time.sleep(10)
#filling billing information
driver.find_element(By.XPATH, "//input[@placeholder='Select Industry Type']").click()
driver.find_element(By.XPATH, "//span[text()='Dental Clinics']").click()

driver.find_element(By.ID, "serviceAddress-street").send_keys("271,vivekananda pally,taki road,barasat")
driver.find_element(By.ID, "serviceAddress-city").send_keys("Kolkata")

driver.find_element(By.XPATH, "//input[@placeholder='Select State']").click()
driver.find_element(By.XPATH, "//span[text()='IN']").click()

driver.find_element(By.XPATH, "//input[@placeholder='ZIP Code']").send_keys("700124")
driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("td92929@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='(123) 456-7890']").send_keys("7439760040")
#latitude & longitutde
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Edit Position On Map']").click()

lati = driver.find_element(By.XPATH, "(//input[@type='number' and @step='1'])[1]")
lati.send_keys("22.57")

longi = driver.find_element(By.XPATH, "(//input[@type='number' and @step='1'])[2]")
longi.send_keys("88.43")

driver.find_element(By.XPATH, "//button[text()='Update Address']").click()
#verify lati & longi-
if lati.is_displayed():
    print("Latitude verified")

if longi.is_displayed():
    print("Longitude verified")

time.sleep(4)
driver.find_element(By.XPATH, "//button[contains(@class,'enabled:hover:text-primary')]").click()
time.sleep(3)
#Add sevice hours
driver.find_element(By.XPATH, "//input[@placeholder='Monday Opening Time']").click()
driver.find_element(By.XPATH, "//span[text()='9:00 AM']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Monday Lunch Start Time']").click()
driver.find_element(By.XPATH, "//span[text()='1:00 PM']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Monday Lunch End Time']").click()
driver.find_element(By.XPATH, "//span[text()='2:00 PM']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Monday Closing Time']").click()
driver.find_element(By.XPATH, "//span[text()='5:00 PM']").click()

driver.find_element(By.XPATH, "(//span[@class='w-1/4 flex items-center justify-center'])[1]").click()
driver.find_element(By.XPATH, "(//span[@class='w-1/4 flex items-center justify-center'])[4]").click()
driver.find_element(By.XPATH, "(//span[@class='w-1/4 flex items-center justify-center'])[6]").click()
driver.find_element(By.XPATH, "(//span[@class='w-1/4 flex items-center justify-center'])[8]").click()
driver.find_element(By.XPATH, "(//span[@class='w-1/4 flex items-center justify-center'])[10]").click()

#  Sat & Sun close
driver.find_element(By.XPATH, "(//div[contains(@class,'cursor-pointer min-w-[26px]')])[6]").click()

driver.find_element(By.XPATH,"(//div[contains(@class,'cursor-pointer min-w-[26px]')])[7]").click()
time.sleep(5)

#  Click on 3 dots
driver.find_element(By.XPATH,"//button[text()='...']").click()
time.sleep(5)
#click on route assignment
driver.find_element(By.XPATH, "//button[text()='Route Assignment']").click()
ele=driver.find_element(By.XPATH, "//button[contains(text(),'Go Back to Generator Profile')]")
ActionChains(driver).click(ele).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@role='checkbox']//div[contains(@class,'cursor-pointer')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Yes']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[text()='...']").click()
driver.find_element(By.XPATH, "//button[text()='Route Assignment']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Add a Service']").click()
time.sleep(3)

 #click route dropdown
driver.find_element(By.ID, "route").click()
time.sleep(2)

# type in search textbox inside dropdown
search_box = driver.find_element(By.XPATH, "//input[@type='text']")
search_box.clear()
search_box.send_keys("Nayan Route")
time.sleep(2)

# click route from list
driver.find_elements(By.XPATH, "//div[text()='Nayan Route']")[0].click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='service-input-0']").click()
driver.find_element(By.XPATH, "//div[text()='Medical Waste']").click()
driver.find_element(By.XPATH, "//div[@class='react-datepicker__input-container']").click()
driver.find_element(By.XPATH, "//div[text()='28']").click()
driver.find_element(By.XPATH, "//span[text()='Service Frequency']").click()
driver.find_element(By.XPATH, "//div[text()='Multiple Times Weekly (MTW)']").click()
driver.find_element(By.XPATH, "//span[text()='Select Weekdays']").click()
time.sleep(2)
driver.execute_script("arguments[0].click();",
    driver.find_element(By.XPATH, "//*[contains(text(),'Thursday')]"))

driver.execute_script("arguments[0].click();",
    driver.find_element(By.XPATH, "//*[contains(text(),'Friday')]"))

driver.execute_script("arguments[0].click();",
    driver.find_element(By.XPATH, "//*[contains(text(),'Saturday')]"))

driver.execute_script("arguments[0].click();",
    driver.find_element(By.XPATH, "//*[contains(text(),'Sunday')]"))

# Open Anchor Date calendar
driver.find_element(By.XPATH, "//label[contains(text(),'Anchor Date')]/following::input[1]").click()

# Get all enabled dates
dates = driver.find_elements(
    By.XPATH,
    "//*[not(contains(@class,'disabled')) and normalize-space(text())!='']"
)

# Click first numeric available date
for d in dates:
    if d.text.isdigit():
        driver.execute_script("arguments[0].scrollIntoView(true);", d)
        d.click()
        print("Selected date:", d.text)
        break
else:
    print("No date found")

## Set Scope of Work (SOW)
driver.find_element(By.XPATH, "(//span[text()='Scope Of Work (SOW)'])[2]").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox' and @class='mr-2'])[4]").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox' and @class='mr-2'])[5]").click()

# Remove extra items if needed
# Close any open dropdown first
driver.find_element(By.TAG_NAME, "body").click()
time.sleep(1)

for i in range(4):
    try:
        remove_btn = driver.find_element(
            By.XPATH,
            "(//button[contains(@class,'absolute right-2 top-1')])[1]"
        )

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", remove_btn)
        time.sleep(1)

        # Use JavaScript click (prevents intercept error)
        driver.execute_script("arguments[0].click();", remove_btn)
        time.sleep(1)

    except:
        break

# Add service to route
driver.find_element(By.XPATH, "//button[text()='Add to Route']").click()
time.sleep(2)
#price book
driver.find_element(By.XPATH, "//a[text()='Price Book']").click()
time.sleep(2)

# Toggle button
toggle = driver.find_element(
    By.XPATH,
    "//button[contains(@class,'rounded-full') and contains(@class,'cursor-pointer')]"
)
driver.execute_script("arguments[0].click();", toggle)

# Click Yes
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(text(),'Yes')]").click()
time.sleep(3)

price_inputs = driver.find_elements(
    By.XPATH, "//input[contains(@class,'bg-transparent') and contains(@class,'outline-none')]"
)

print("Total price inputs:", len(price_inputs))

if len(price_inputs) >= 2:
    # First selected container price
    p1 = price_inputs[0]
    p1.click()
    p1.send_keys(Keys.CONTROL + "a")
    p1.send_keys(Keys.DELETE)
    p1.send_keys("19.42")

    # Second selected container price
    p2 = price_inputs[1]
    p2.click()
    p2.send_keys(Keys.CONTROL + "a")
    p2.send_keys(Keys.DELETE)
    p2.send_keys("15.67")

    print("Price updated for 2 containers")
else:
    print("Price boxes not found")

time.sleep(2)
#logout
driver.find_element(By.XPATH, "//img[contains(@class,'rounded-full')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Logout']").click()
print("Logout successfully")

driver.quit()
