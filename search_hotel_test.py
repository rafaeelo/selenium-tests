from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()

driver.find_element_by_name("checkin").send_keys("05/11/2019")
driver.find_element_by_name("checkout").send_keys("08/11/2019")
driver.find_element_by_name("checkin").click()

driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys(4)
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys(5)
driver.find_element_by_xpath("//button[text()=' Search']").click()

hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
print(hotels)
hotel_name = [hotel.get_attribute("textContent") for hotel in hotels]
print(hotel_name)

for name in hotel_name:
    print("hotel name: " + name)

prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
prices_values = [price.get_attribute("textContent") for price in prices]
for price in prices_values:
    print("cena to : " + price)

assert hotel_name[0] == "Jumeirah Beach Hotel"
assert hotel_name[1] == "Oasis Beach Tower"
assert hotel_name[2] == "Rose Rayhaan Rotana"
assert hotel_name[3] == "Hyatt Regency Perth"

assert prices_values[0] == "$22"
assert prices_values[1] == "$50"
assert prices_values[2] == "$80"
assert prices_values[3] == "$150"

driver.close();