from selenium import webdriver
import time

driver = driver = webdriver.Chrome('C:/Users/Lokesh/Desktop/chromedriver.exe')

driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
driver.execute_script("window.open('','_blank');")
driver.switch_to_window(driver.window_handles[1])
driver.get('https://web.whatsapp.com/')
time.sleep(60)

flag = 0
message =''
oldLength = 0
newLength = 1

message = driver.find_elements_by_class_name("msg")

while True:
    if newLength > oldLength:
        msgg = message[len(message) -1 ].text
        msgg = msgg.split('\n')
        msgg = msgg[0]
        print(msgg)
    # msgg is MESSAGE of the USER
    
        driver.switch_to_window(driver.window_handles[0])
        driver.switch_to.frame('input')
        textField = driver.find_elements_by_tag_name("input")[1]
        textField.send_keys(msgg + Keys.ENTER)
        time.sleep(1)
        fontTags = driver.find_elements_by_tag_name("font")
        
        for tag in fontTags:
            if tag.get_attribute("face") == "Trebuchet MS,Arial" and tag.get_attribute("color") == "#000000":
                responseBody = tag
                break
        
        x = responseBody.text
        x = x.split('\n')
        x = x[1]
        x = x[10:]
        
        # x is response of mitsuku
        
        driver.switch_to_window(driver.window_handles[1])
        inputMessage = driver.find_elements_by_class_name('input-container')
        inputMessage[0].send_keys(x,Keys.ENTER)
        message = driver.find_elements_by_class_name("msg")
        while True:
            oldLength = len(message)
            message = driver.find_elements_by_class_name("msg")
            newLength = len(message)
            if newLength > oldLength:
                break
            print("Waiting For New Message...")
    print("Waiting to get message")
        

        
        
        

    
