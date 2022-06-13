from unittest.loader import VALID_MODULE_NAME
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib import request
import requests
import sqlite3
from bs4 import BeautifulSoup
import time
import sqlite3

count = 1
summary_detail=[]
summary_tag = []
info_title=[]
info_details=[]
urls=[]
date_t = []
date_d = []
doc_title = []
doc_detail = []
conn = sqlite3.connect('test.db')
# if conn:
#     conn.execute('''CREATE TABLE Contact
#        (Cont_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         Name        TEXT,
#         Constraint_Type		  TEXT,
#         Status	  TEXT,
#         ID            INTEGER,
#         FOREIGN KEY(ID) REFERENCES Header(ID));''')


PATH = "/Users/yudiz/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://portal.calderdale.gov.uk/online-applications/")

nav = driver.find_element(by=By.LINK_TEXT ,value="Weekly/Monthly Lists").click()
time.sleep(2)
driver.find_element(by=By.XPATH ,value='//*[@id="week"]/option[2]').click()
time.sleep(2)
driver.find_element(by=By.XPATH ,value='//*[@id="weeklyListForm"]/fieldset/div[5]/input[2]').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="resultsPerPage"]/option[5]').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="searchResults"]/input[4]').click()
print("page 100....")
time.sleep(2)
# link=driver.find_elements(by=By.XPATH,value="//li[@class = 'searchresult']/a")
# for l in link:
#     urls.append(l.text)
# for i in range(len(urls)):
#     print(urls[i])
#     conn.execute('INSERT INTO Header(LINKS) VALUES(?)',(urls[i],))
#     conn.commit()


while True:
    print(count,"Count")
    link2=driver.find_element(by=By.XPATH,value="//*[@id='searchresults']/li["+str(count)+"]/a").text
    links = driver.find_element(by=By.XPATH,value="//*[@id='searchresults']/li["+str(count)+"]/a").send_keys(Keys.COMMAND,Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])
    ref=driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[1]/td').text
    alt_ref=driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[2]/td').text
    app_rec=driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[3]/td').text
    app_vali = driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[4]/td').text
    address = driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[5]/td').text
    propasal =  driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[6]/td').text
    status = driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[7]/td').text
    Appeal_status = driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[7]/td').text
    Appeal_Decision = driver.find_element(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr[9]/td').text
    # conn.execute('INSERT INTO Summary(Reference,Alternative_Reference,Application_Received,Application_Validated,Address,Proposal,Status, Appeal_Status,Appeal_Decision,ID ) VALUES(?,?,?,?,?,?,?,?,?,?)',(ref,alt_ref,app_rec,app_vali,address,propasal,status,Appeal_status,Appeal_Decision,link2))
    # conn.commit()
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT,value='Further Information').click()
    title = driver.find_elements(by=By.XPATH,value='//*[@id="applicationDetails"]/tbody/tr/th')
    details = driver.find_elements(by=By.XPATH,value='//*[@id="applicationDetails"]/tbody/tr/td')
    for t in range(len(title)):
        print(title[t].text)
        info_title.append(title[t].text)
    for d in range(len(details)):
        print(details[d].text)
        info_details.append(details[d].text)
    info = dict(zip(info_title,info_details))
    # conn.execute('''INSERT INTO Further_info(Application_Type,EDL,CASH_OFFICER,PARISH,WARD,APPLICANT_NAME, AGENT_NAME,AGENT_COMPANY,AGENT_ADDR,EAR,ID ) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(info.get('Application Type'),info.get('Expected Decision Level'),info.get('Case Officer'),info.get('Parish'),info.get('Ward'),info.get('Applicant Name'),info.get('Agent Name'),info.get('Agent Company Name'),info.get('Agent Address'),info.get('Environmental Assessment Requested'),link2))
    # conn.commit()
    info_title.clear()
    info_details.clear()
    driver.find_element(by=By.LINK_TEXT,value='Important Dates').click()
    date_title = driver.find_elements(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr/th')
    date_details = driver.find_elements(by=By.XPATH,value='//*[@id="simpleDetailsTable"]/tbody/tr/td')
    for t in range(len(date_title)):    
        date_t.append(date_title[t].text)
    for d in range(len(date_details)):    
        date_d.append(date_details[d].text)
    date = dict(zip(date_t,date_d))
    # conn.execute('''INSERT INTO Imp_dates(Application_Received_Date,Application_Validated_Date,Expiry_Date,Actual_Committee_Date
    # ,Latest_Neighbour_Consultation_Date,Neighbour_Consultation_Expiry_Date,Standard_Consultation_Date,Standard_Consultation_Expiry_Date,Last_Advertised_In_Press_Date
    # ,Latest_Advertisement_Expiry_Date,Last_Site_Notice_Posted_Date,Latest_Site_Notice_Expiry_Date,Internal_Target_Date,Agreed_Expiry_Date,Decision_Made_Date,Permission_Expiry_Date
    # ,Decision_Printed_Date,Environmental_Impact_Assessment_Received,Determination_Deadline,Temporary_Permission_Expiry_Date,ID) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
    # (date.get('Application Received Date'),date.get('Application Validated Date'),date.get('Expiry Date'),date.get('Actual Committee Date'),date.get('Latest Neighbour Consultation Date')
    # ,date.get('Neighbour Consultation Expiry Date'),date.get('Standard Consultation Date'),date.get('Standard Consultation Expiry Date')
    # ,date.get('Last Advertised In Press Date'),date.get('Latest Advertisement Expiry Date'),date.get('Last Site Notice Posted Date')
    # ,date.get('Latest Site Notice Expiry Date'),date.get('Internal Target Date'),date.get('Agreed Expiry Date'),date.get('Decision Made Date')
    # ,date.get('Permission Expiry Date'),date.get('Decision Printed Date'),date.get('Environmental Impact Assessment Received'),date.get('Determination Deadline'),date.get('Temporary Permission Expiry Date'),link2))
    # conn.commit()
    date_t.clear()
    date_d.clear()
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//*[@id="tab_constraints"]').click()
    url = driver.find_element(by=By.XPATH,value='//*[@id="tab_constraints"]').get_attribute('href')
    print('url',url)
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # for tr in soup.find_all('tr')[1:]:
    #     tds = tr.find_all('td')
    #     print([tds[0].text, tds[1].text, tds[2].text])
        # conn.execute('''INSERT INTO Contact(Name,Constraint_Type,Status,ID) VALUES(?,?,?,?)''',(tds[0].text, tds[1].text,tds[2].text,link2))
        # conn.commit()
    # q = conn.execute('SELECT ID FROM Header WHERE LINKS=(?)',(link2,))
    driver.find_element(by=By.XPATH,value='//*[@id="tab_documents"]').click()
    docs_url =  driver.find_element(by=By.XPATH,value='//*[@id="tab_documents"]').get_attribute('href')
    temp = requests.get(docs_url)
    print("temp url ",temp)
    soup2 = BeautifulSoup(temp.content,'html.parser')
    for doc_tr in soup2.find_all('tr')[1:]:     
        doc_tds = doc_tr.find_all('td')
        anchor = driver.find_element(by=By.XPATH,value='//*[@id="Documents"]/tbody/tr/td/a').get_attribute('href')
        print(anchor)
        print("kjdaksldkjdkjdaksdjasjkl",[doc_tds[1].text, doc_tds[2].text, doc_tds[3].text])
        conn.execute('''INSERT INTO Document(Date_Published,Document_Type,Description,view,ID) VALUES(?,?,?,?,?)''',(doc_tds[1].text,doc_tds[2].text,doc_tds[4].text,anchor,link2))
        conn.commit()
    time.sleep(12)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    count+=1
   
    
























# for z in range(len(contact)):
#     conn.execute('INSERT INTO Employees(ADDRESS,INFO) VALUES(?,?)',(Address[z],contact[z]))
#     conn.commit()
