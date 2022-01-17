import time
from PIL import Image
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException





year = input()
CompName = input()
probNum = input()

ser = Service('C:/Users/ronit/PyCharmProjects/AMC-AIME BOT/chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://artofproblemsolving.com/wiki/index.php/'+year+'_'+CompName+'_Problems/Problem_'+probNum)
driver.fullscreen_window()
try:
    driver.find_element(By.CLASS_NAME, "togglelink").click()
except NoSuchElementException:
    pass
time.sleep(2)
problemPage = driver.get_screenshot_as_png()





#Find Dimensions of Problem by exploiting formating of AOPS Site
probWithNum = True
solWithNum = True
solWithoutNum = True

try:
    driver.find_element(By.ID,'Problem_' + probNum)
except NoSuchElementException:
    probWithNum = False
try:
    element2 = driver.find_element(By.ID,'Solution_1')
except NoSuchElementException:
    solWithNum = False
try:
    driver.find_element(By.XPATH,"//*[contains(@id, 'Solution')]")
except NoSuchElementException:
    solWithoutNum = False

if probWithNum:
    element1 = driver.find_element(By.ID,'Problem_' + probNum)
else:
    element1 = driver.find_element(By.ID,'Problem')

location1 = element1.location

if solWithNum:
    element2 = driver.find_element_by_xpath("//*[contains(@id, 'Solution')]")
    location2 = element2.location
elif solWithoutNum:
    element2 = driver.find_element(By.XPATH,"//*[contains(@id, 'Solution')]")
    location2 = element2.location
else:
    location2 = {'x' : location1['x'],'y' : location1['y']+3500}






#Getting Answer for Question (Could be Optimized in the sense that it gets all the answers from the test the problem is from)
driver.get('https://artofproblemsolving.com/wiki/index.php/'+year+'_'+CompName+'_Answer_Key')
element3 = driver.find_element(By.ID,'mw-content-text').text
answers = str(element3)
answerList = answers.splitlines()
print(answerList[int(probNum)-1])


#Creating Picture for Problem
im = Image.open(BytesIO(problemPage)) # uses PIL library to open image in memory

left = location1['x']
top = location1['y']
right = location2['x']+1800
bottom = location2['y']

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image

screenshot = Image.open('screenshot.png')

screenshot.show()
