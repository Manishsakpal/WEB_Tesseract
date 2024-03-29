# import requests
# from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
from datetime import datetime
# Step 1: Open URL in Chrome and wait until element with ID "username" is visible
 
# iii=input("Enter the OTP u get")
# # # Step 5: Wait for the page to load and click the button with class ID "btn btn-success btn-block btn-flat"
# success_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-success.btn-block.btn-flat")))
# success_button.click()
#time.sleep(10)
# Step 6: Refresh the URL with the new URL "https://www.enesttechnologies.com/workPanel/preLiveWork/forms-2.php"
chrome_driver = webdriver.Chrome()
ErrorFound=0
 
 
 
chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
wait = WebDriverWait(chrome_driver, 10)
username_element = wait.until(EC.visibility_of_element_located((By.ID, "username")))
 
# Step 2: Enter text "8108543251" into element with ID "username"
username_element.send_keys("8108543251")
 
# Step 3: Enter text "bmdt0273" into element with ID "password"
password_element = chrome_driver.find_element(By.ID, "password")
password_element.send_keys("stmp0290")
 
# Step 4: Click the button with class ID "btn btn-primary btn-block btn-flat"
login_button = chrome_driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block.btn-flat")
login_button.click()
time.sleep(3)
chrome_driver.get("https://www.enesttechnologies.com/workPanel/custommobilenoediting/forms-1.php")
 
print("sucess ful refress")
time.sleep(10)
login_button = chrome_driver.find_element(By.ID, "info11")
login_button.click()
 
 
while True and ErrorFound<10:
    try:
        #chrome_driver = webdriver.Chrome()
        # chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
        # wait = WebDriverWait(chrome_driver, 10)
        # username_element = wait.until(EC.visibility_of_element_located((By.ID, "username")))
 
        # # Step 2: Enter text "8108543251" into element with ID "username"
        # username_element.send_keys("8108543251")
 
        # # Step 3: Enter text "bmdt0273" into element with ID "password"
        # password_element = chrome_driver.find_element(By.ID, "password")
        # password_element.send_keys("stmp0290")
 
        # # Step 4: Click the button with class ID "btn btn-primary btn-block btn-flat"
        # login_button = chrome_driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block.btn-flat")
        # login_button.click()
        # time.sleep(3)
        # chrome_driver.get("https://www.enesttechnologies.com/workPanel/custommobilenoediting/forms-1.php")
 
        # print("sucess ful refress")
        # time.sleep(10)
        # login_button = chrome_driver.find_element(By.ID, "info11")
        # login_button.click()
       
       
       
       
        # try:
        #     # Wait for the close buttons to become present
        #     close_buttons = WebDriverWait(chrome_driver, 10).until(
        #         EC.presence_of_all_elements_located((By.XPATH, '//*[@id="closeJobPay12"] | //*[@id="closeJobPay1212"]'))
        #     )  
        #     for close_button in close_buttons:
        #         close_button.click()
        #     #print("Pressed second button")
        # except:
        #     print("Excepting to clocse the unwanted window")
 
        #Element=chrome_driver.find_element(By.CLASS_NAME,"col-sm-9")
        # DicNumSym=[Each.split("=") for Each in str(Element.text).replace(" ","").split(",")]
        # # #print(DicNumSym)
 
        # Dic={}
        # for i in DicNumSym:
        #     Dic[i[1]]=i[0]
        ##print(Dic)
 
       
 
        image_url = chrome_driver.current_url[::-1].split("/",1)[1][::-1]+"/mobileno-img.php"
 
        # DriverChrome.get(image_url)
 
 
        # # Open a new tab
        # DriverChrome.execute_script("window.open('');")
 
        # # Switch to the new tab
        # DriverChrome.switch_to.window(DriverChrome.window_handles[-1])
        # #print("Working")
        # i=input("")
               
        try:
            # Find the doodle image element
            ####time.sleep(2)
            for i,v in enumerate(['#xcods']):
                doodle_element = chrome_driver.find_element(By.CSS_SELECTOR,v)
                # Get the URL of the doodle image
                doodle_url = doodle_element.get_attribute("src")
                # Check if the doodle URL is relative, and make it absolute
                if doodle_url.startswith("/"):
                    doodle_url = image_url
                if i==0:
                    Web_Image="\\Caption.jpg"
                if i==2:
                    Web_Image="\\Dictionary.jpg"
                # Create a folder to save the image if it doesn't exist
                folder_path = os.getcwd()+Web_Image
                # Save the image
                with open(folder_path, "wb") as f:
                    # Download the image using Selenium
                    time.sleep(1)
                    f.write(doodle_element.screenshot_as_png)
            #print("Doodle image saved successfully!")
        except Exception as e:
            print("An error occurred:", e)
 
 
 
        text_Dict = chrome_driver.current_url[::-1].split("/",1)[1][::-1]+"/mobilesym3-img.php"
 
        text_SNI = chrome_driver.current_url[::-1].split("/",1)[1][::-1]+"/mobileno3-img.php"
 
        for i,v in enumerate([text_Dict,text_SNI]):
            chrome_driver.execute_script("window.open('about:blank', '_blank');")
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            chrome_driver.get(v)
            #for i,v in enumerate(['body > img','body > img']):
            time.sleep(2)
            doodle_element = chrome_driver.find_element(By.CSS_SELECTOR,"body > img")
            # Get the URL of the doodle image
            doodle_url = doodle_element.get_attribute("src")
           
            # Check if the doodle URL is relative, and make it absolute
            if doodle_url.startswith("/"):
                doodle_url = image_url
            if i==0:
                Web_Image="\\text_SNI.jpg"
            if i==1:
                Web_Image="\\text_Dict.jpg"
            print("Better3")
            # Create a folder to save the image if it doesn't exist
            folder_path = os.getcwd()+Web_Image
            # Save the image
            with open(folder_path, "wb") as f:
                # Download the image using Selenium
                time.sleep(1)
                f.write(doodle_element.screenshot_as_png)
            print("Better4")
            chrome_driver.close()
            chrome_driver.switch_to.window(chrome_driver.window_handles[0])
            print("Better5")
           
           
            #file_path = os.path.join(os.getcwd(), "text_SNI.jpg")
 
           
        print("Screen shot "*10)
        #time.sleep(60)
 
 
 
 
 
 
 
       
        # # Open a new tab in the existing Chrome window and switch to it
        # chrome_driver.execute_script("window.open('about:blank', '_blank');")
        # chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
 
 
        # chrome_driver.get("https://www.jpgtotext.com/")
        # #dismiss-button > div > svg
        # folder_path = os.getcwd()+"\\text_SNI.jpg"+"\n"+os.getcwd()+"\\Caption.jpg"+"\n"+os.getcwd()+"\\text_Dict.jpg"
        # #+"\n"+os.getcwd()+"\\Dictionary.jpg"
        # # Find the browse button and click it
        # #browse_button = WebDriverWait(chrome_driver, 10).until(EC.element_to_be_clickable((By.ID, "//*[@id="file"]")))
        # Element = chrome_driver.find_element(By.XPATH,'//*[@id="file"]')
        # Element.send_keys(folder_path)
 
        # # Find the button with data-v attribute and click it
 
 
        # try:
        #     # Find the button by its XPath
        #     button_xpath = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div[2]/div/div[4]/button'
        #     button = WebDriverWait(chrome_driver, 20).until(
        #         EC.element_to_be_clickable((By.XPATH, button_xpath))
        #     )
           
        #     # Click the button using JavaScript
        #     chrome_driver.execute_script("arguments[0].click();", button)
           
           
           
        #     #print("Button clicked and page reloaded successfully!")
        #     # Wait for the textarea to become clickable
        #     textarea_css_selector = 'textarea[data-v-5e38c1d8]'
        #     textarea = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, textarea_css_selector)))
 
        #     textarea_css_selector_ = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/textarea'
        #     textarea_ = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.XPATH, textarea_css_selector_)))
 
        #     textarea_css_selector__ = '//*[@id="maincontent"]/div[2]/div[3]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/textarea'
        #     textarea__ = WebDriverWait(chrome_driver, 120).until(EC.element_to_be_clickable((By.XPATH, textarea_css_selector__)))
 
        #     #maincontent > div.min-h-48.flex.w-full.flex-col.justify-between.items-center.px-4.pb-4.lg\:pb-20 > div.w-full.max-w-7xl.pt-0.md\:pt-4.flex.flex-wrap > div > div > div.px-4.w-full > div > div > div:nth-child(4) > div > div.relative.flex-wrap.flex-grow > div > div > textarea
        #     #maincontent > div.min-h-48.flex.w-full.flex-col.justify-between.items-center.px-4.pb-4.lg\:pb-20 > div.w-full.max-w-7xl.pt-0.md\:pt-4.flex.flex-wrap > div > div > div.px-4.w-full > div > div > div:nth-child(4) > div > div.relative.flex-wrap.flex-grow > div > div > textarea
        #     # Interact with the textarea (for example, get its text)
        #     text_SNI = textarea.text.replace("\n","").replace(" ","").replace("==","=")
        #     text_Caption = textarea_.text
        #     text_Dict = str(textarea__.text).strip()
        #     #text_Dict="0 = %, 1 = ), 2 = $, 3 = @, 4 = (, 5 = !, 6 = #, 7 = &, 8 = ^, 9 = *"
        #     #print("Textarea text:", text_SNI)
        #     #text = textarea.text
           
        #     #print("Textarea text:", text_Caption)
 
        #     #print("Textarea is enabled after clicking the button!")
 
        # except Exception as e:
        #     chrome_driver.close()
           
           
        # chrome_driver.close()
        # chrome_driver.switch_to.window(chrome_driver.window_handles[0])
       
        # # print("text_SNI,text_Caption,text_Dict,",text_SNI,text_Caption,text_Dict)
        # # #text_SNI,text_Caption,text_Dict, 0 = ^, 1 = &, 2 = (, 3 = #, 4 = *, 5 = %, 6 = $, 7 = !, 8 = @,9 =) 2 + 3 80(2#5*&99
        # # print([True if i in text_SNI.replace(" ","") else False for i in "0 = %, 1 = ), 2 = $, 3 = @, 4 = (, 5 = !, 6 = #, 7 = &, 8 = ^, 9 = *".replace(" ","")])
       
       
        # # if not(all([True if i in text_SNI.replace(" ","") else False for i in "0 = %, 1 = ), 2 = $, 3 = @, 4 = (, 5 = !, 6 = #, 7 = &, 8 = ^, 9 = *".replace(" ","")])):
        # #     print(text_SNI)
        # #     Exception_noProperConvrsion
        # # if len(str(text_Dict))!=10:
        # #     print(text_Dict)
        # #     phoneNumberPhotoNoProper
           
           
           
        #os.getcwd()+"\\text_SNI.jpg"+"\n"+os.getcwd()+"\\Caption.jpg"+"\n"+os.getcwd()+"\\text_Dict.jpg"4
        text_SNI = "".join([ x for x in os.popen(r'tesseract "text_SNI.jpg" - -l eng').read() if x not in ["\n"," "]])
        text_Caption = "".join([ x for x in os.popen(r'tesseract "Caption.jpg" - -l eng').read() if x not in ["\n"," "]])
        text_Dict = "".join([ x for x in os.popen(r'tesseract "text_Dict.jpg" - -l eng').read() if x not in ["\n"," "]])
        print("Working Fine...")
        print("Value for dictionary is ",text_SNI)

 
 
 
        # DicNumSym=[Each.split("=") if "=" in Each else (Each+"=").split("=") for Each in str(text_SNI).strip().replace(" ","").split(",")]
       
       
        # # if all([True if i in DicNumSym.keys() else False for i in "1234567890"]) and all([True if i in DicNumSym.values() else False for i in "!@#$%^&*()"]):
        # #     for i in "1234567890":
        # #         if i not in DicNumSym.keys():
        # #             DicNumSym[i]=""
               
        # #     for i,v in enumerate("!@#$%^&*()"):
        # #         if v not in DicNumSym.values():
        # #             DicNumSym[list(DicNumSym.keys())[i]]=v
                   
           
        # # #print(DicNumSym)
 
        # Dic={}
        # for i in DicNumSym:
        #     Dic[str(i[1])[0]]=str(i[0])[-1]
           
           
           
        # if not(all([True if i in Dic.keys() else False for i in "1234567890"])):
        #     for i in "1234567890":
        #         if i not in Dic.keys():
        #             Dic[i]=""
        # if not(all([True if i in Dic.values() else False for i in "!@#$%^&*()"])):                
        #     for i,v in enumerate("!@#$%^&*()"):
        #         if v not in Dic.values():
        #             Dic[list(Dic.keys())[i]]=v
                   
                   
                   
        # ##print(Dic)
        # # Switch back to the original tab
       
        # chrome_driver.switch_to.window(chrome_driver.window_handles[0])
        # #print("TextEntering.....",text)
 
 
        # print("No problem 1",Dic)
 
 
 
 
 
               
        DicNumSym=[Each.split("=") if "=" in Each else (Each+"=").split("=") for Each in str(text_SNI).strip().replace(" ","").split(",")]
 
        print(DicNumSym)
        # if all([True if i in DicNumSym.keys() else False for i in "1234567890"]) and all([True if i in DicNumSym.values() else False for i in "!@#$%^&*()"]):
        #     for i in "1234567890":
        #         if i not in DicNumSym.keys():
        #             DicNumSym[i]=""
               
        #     for i,v in enumerate("!@#$%^&*()"):
        #         if v not in DicNumSym.values():
        #             DicNumSym[list(DicNumSym.keys())[i]]=v
                   
           
        # #print(DicNumSym)
        print([v for i,v in enumerate("!@#$%^&*()") if v not in [z[1] if z[1]!="" else "Dum" for z in DicNumSym]])
        Dic={}
        dum=0
        for i,v in enumerate(DicNumSym):
            print("value",v)
            if v[1]=="":
                Dic[[v for i,v in enumerate("!@#$%^&*()") if v not in [z[1] if z[1]!="" else "Dum" for z in DicNumSym]][dum]]=str(v[0])[-1]
                dum+=1
            else:
                Dic[str(v[1])]=str(v[0])[-1]
            # except:
                # Dic[str(i[1])]=    
                   
            print("Dic",Dic)
        IndexI=0
        print([True if i in Dic.keys() else False for i in "!@#$%^&*()"])
        if not(all([True if i in Dic.keys() else False for i in "!@#$%^&*()"])):                
            for i,v in enumerate("!@#$%^&*()"):
                if v not in Dic.keys():
                    Dic[v]=[i for i,v in enumerate(Dic.keys()) if v not in "!@#$%^&*()"][IndexI]
                    IndexI+=1
 
        IndexI=0
        print([True if i in Dic.values() else False for i in "1234567890"])
        if not(all([True if i in Dic.values() else False for i in "1234567890"])):
            for i in "1234567890":
                if i not in Dic.values():
                    Dic[list(Dic.values())[i]]=[i for i,v in enumerate(Dic.values()) if v not in "1234567890"][IndexI]
                    IndexI+=1
 
                   
 
        print("No problem 1",len(Dic),"<=Length Value=>",Dic)
        if len(Dic)!=10:
            DumData
 
 
 
 
 
        NumDic={"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four","5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
        OutputNumStr=[]
        OutputNum=[]
        for EachNumber in str(text_Dict):
            if EachNumber in Dic.keys():
                EachNumber=Dic[EachNumber]
            OutputNumStr.append(NumDic[EachNumber])
            OutputNum.append(EachNumber)
 
        ##print(EachNumber,OutputNum)
        print("No problem 1")
       
        try:
            #print("REaching the enter button")
            Element = chrome_driver.find_element(By.ID,"enty")
            Element.click()
            time.sleep(0.5)
            Element.send_keys("India : "+" ".join(OutputNumStr).strip()+" (+91 "+"".join(OutputNum).strip()+")")  # Enter the phone number
        except:
            #print("Inner exception")
            Element_ = chrome_driver.find_element(By.ID,"closeJobPay1")
            Element_.click()
            Element = chrome_driver.find_element(By.ID,"enty")
            Element.click()
            time.sleep(0.5)
            Element.send_keys("India : "+" ".join(OutputNumStr).strip()+" (+91 "+"".join(OutputNum).strip()+")")  # Enter the phone number
        print("India : "+" ".join(OutputNumStr)+" (+91 "+"".join(OutputNum)+")")
        ##print("India : "+" ".join(OutputNumStr)+" (+91 "+"".join(OutputNum)+")"+text)
        #ii=input("Waiting for ur caption in the web and submit")
       
       
 
 
 
        Element = chrome_driver.find_element(By.ID,"code")
        Element.click()
        Element.send_keys(eval(text_Caption))
        #ii=input("PLease just Enter for submit")
 
 
        # Find the button by its XPath
        button_xpath = '//*[@id="ffields"]/div/div[2]/div/div[6]/div/center/button'
        button = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
       
        # Click the button using JavaScript
        chrome_driver.execute_script("arguments[0].click();", button)
       
       
       
        time.sleep(15)
        button_xpath = '//*[@id="matched"]/div/div/div[3]/center/button'
        try:
            button = WebDriverWait(chrome_driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, button_xpath))
            )
            button.click()
        except:
            button_xpath = 'refrs'
            try:
                button = WebDriverWait(chrome_driver, 30).until(
                    EC.element_to_be_clickable((By.ID, button_xpath))
                )
                button.click()
            except:
                hhhh
           
           
           
            print("IMage and text not matching")
            os.popen("ren String_Number.jpg "+str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f').replace('.','-').replace(':','-'))+".jpg")
        #ii=input("Done execution")
       
       
        print("Runned no problem")
        ErrorFound=0
    except Exception as Expp:
        try:
            #chrome_driver.quit()
            print("Exception",Expp)
            chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
            wait = WebDriverWait(chrome_driver, 10)
            username_element = wait.until(EC.visibility_of_element_located((By.ID, "username")))
 
            # Step 2: Enter text "8108543251" into element with ID "username"
            username_element.send_keys("8108543251")
 
            # Step 3: Enter text "bmdt0273" into element with ID "password"
            password_element = chrome_driver.find_element(By.ID, "password")
            password_element.send_keys("stmp0290")
 
            # Step 4: Click the button with class ID "btn btn-primary btn-block btn-flat"
            login_button = chrome_driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block.btn-flat")
            login_button.click()
            time.sleep(3)
            chrome_driver.get("https://www.enesttechnologies.com/workPanel/custommobilenoediting/forms-1.php")
 
            print("sucess ful refress")
            time.sleep(10)
            login_button = chrome_driver.find_element(By.ID, "info11")
            login_button.click()
           
            ErrorFound+=1
            # time.sleep(30)
            # chrome_driver = webdriver.Chrome()
            #chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
            print("Hope refresh")
            #time.sleep(30)
        except:
            #chrome_driver.quit()
            print("Exception",Expp)
            chrome_driver = webdriver.Chrome()
            ErrorFound=0
            chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
            wait = WebDriverWait(chrome_driver, 10)
            username_element = wait.until(EC.visibility_of_element_located((By.ID, "username")))
 
            # Step 2: Enter text "8108543251" into element with ID "username"
            username_element.send_keys("8108543251")
 
            # Step 3: Enter text "bmdt0273" into element with ID "password"
            password_element = chrome_driver.find_element(By.ID, "password")
            password_element.send_keys("stmp0290")
 
            # Step 4: Click the button with class ID "btn btn-primary btn-block btn-flat"
            login_button = chrome_driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block.btn-flat")
            login_button.click()
            time.sleep(3)
            chrome_driver.get("https://www.enesttechnologies.com/workPanel/custommobilenoediting/forms-1.php")
 
            print("sucess ful refress")
            time.sleep(10)
            login_button = chrome_driver.find_element(By.ID, "info11")
            login_button.click()
           
            ErrorFound+=1
            # time.sleep(30)
            # chrome_driver = webdriver.Chrome()
            #chrome_driver.get("https://www.enesttechnologies.com/workPanel/")
            print("Hope refresh")
            #time.sleep(30)
           
    # Close the WebDriver
    #chrome_driver = webdriver.Chrome()
chrome_driver.quit()
 
 
 
#new updated++