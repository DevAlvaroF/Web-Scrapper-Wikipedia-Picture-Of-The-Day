import time
import urllib
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


# Main Spider Function
def main():

    driver = webdriver.Chrome(r"C:\ChromeDriver\chromedriver.exe")
    driver.get("https://www.wikipedia.org/")
    time.sleep(5) # To visualize results

    # Click on [Wikimedia commons] Action button
    driver.find_element(By.XPATH,"/html/body/div[7]/div[3]/div[1]/a[@class='other-project-link']").click()
    time.sleep(5) # To visualize results

    # Get website screenshot to verify
    driver.get_screenshot_as_file("screenshot_wikipedia.png")

    # Get Picture of the Day
    img = driver.find_element(By.XPATH,"//*[@id='mainpage-potd']/*[1]/a[@class='image']/img[1]")
    src = img.get_attribute('src')

    # Add BS Parser
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    # Get scrap info
    soup.find
    description = [i.text for i in soup.find_all('a',class_='extiw')]

    # download the image with proper name
    fileName = description[0].replace(' ','_')+".png"
    urlretrieve(src, fileName)
    print(f"\nSaved File:  {fileName}\n")

    # Close Chrome Driver
    driver.close()

if __name__ == "__main__":
    main()
