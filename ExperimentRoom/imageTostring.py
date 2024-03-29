import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
from datetime import datetime
# Step 6: Refresh the URL with the new URL "https://www.enesttechnologies.com/workPanel/preLiveWork/forms-2.php"
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.jpgtotext.com/")
#dismiss-button > div > svg
folder_path = os.getcwd()+"\\text_SNI.jpg"+"\n"+os.getcwd()+"\\Caption.jpg"+"\n"+os.getcwd()+"\\text_Dict.jpg"
#+"\n"+os.getcwd()+"\\Dictionary.jpg"
# Find the browse button and click it
#browse_button = WebDriverWait(chrome_driver, 10).until(EC.element_to_be_clickable((By.ID, "//*[@id="file"]")))
Element = chrome_driver.find_element(By.XPATH,'//*[@id="file"]')
Element.send_keys(folder_path)

# Find the button with data-v attribute and click it


try:
    # Find the button by its XPath
    button_xpath = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div[2]/div/div[4]/button'
    button = WebDriverWait(chrome_driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    )
    
    # Click the button using JavaScript
    chrome_driver.execute_script("arguments[0].click();", button)
    
    
    
    #print("Button clicked and page reloaded successfully!")
    # Wait for the textarea to become clickable
    textarea_css_selector = 'textarea[data-v-5e38c1d8]'
    textarea = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, textarea_css_selector)))

    textarea_css_selector_ = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/textarea'
    textarea_ = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.XPATH, textarea_css_selector_)))

    textarea_css_selector__ = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/textarea'
    textarea__ = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.XPATH, textarea_css_selector__)))

    #maincontent > div.min-h-48.flex.w-full.flex-col.justify-between.items-center.px-4.pb-4.lg\:pb-20 > div.w-full.max-w-7xl.pt-0.md\:pt-4.flex.flex-wrap > div > div > div.px-4.w-full > div > div > div:nth-child(4) > div > div.relative.flex-wrap.flex-grow > div > div > textarea
    #maincontent > div.min-h-48.flex.w-full.flex-col.justify-between.items-center.px-4.pb-4.lg\:pb-20 > div.w-full.max-w-7xl.pt-0.md\:pt-4.flex.flex-wrap > div > div > div.px-4.w-full > div > div > div:nth-child(4) > div > div.relative.flex-wrap.flex-grow > div > div > textarea
    # Interact with the textarea (for example, get its text)
    text_SNI = textarea.text.replace("\n","").replace(" ","").replace("==","=")
    text_Caption = textarea_.text
    text_Dict = textarea__.text
    #text_Dict="0 = %, 1 = ), 2 = $, 3 = @, 4 = (, 5 = !, 6 = #, 7 = &, 8 = ^, 9 = *"
    #print("Textarea text:", text_SNI)
    #text = textarea.text
    
    #print("Textarea text:", text_Caption)

    #print("Textarea is enabled after clicking the button!")

except Exception as e:
    chrome_driver.close()
    
    
chrome_driver.close()
chrome_driver.switch_to.window(chrome_driver.window_handles[0])

print("text_SNI,text_Caption,text_Dict,",text_SNI,text_Caption,text_Dict)