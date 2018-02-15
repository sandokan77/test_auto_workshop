from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys

import time


#----------------------------configuration--------------------------------------------------
CONFIG_URL = "https://jira.smss.org.nz/secure/Dashboard.jspa";

def wait_until_element_visible(xpath):
    visible = None;

    while (visible == None):
        try:
            element = driver.find_element_by_xpath(xpath);
            visible = element.is_displayed();
        except NoSuchElementException:
            print (xpath + "is not visible");
            time.sleep(0.2);

    print (xpath + "is visible");            
    return element;

#not working (yet) needs investigation: returns always result
def debug_xpath():
    result =  driver.execute_script("function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}" + "result = getElementByXpath(\"//input[@id=\'login-form-username\' and @name=\'os_username\']\");");
    print (result);                            
    

#----------------------------application elements API---------------------
def getUsernameTextfield():
    return wait_until_element_visible("//*[@id='login-form-username' and @name='os_username']");

def getPasswordTextField():
    return wait_until_element_visible("//*[@id='login-form-password' and @name='os_password']");

def getLoginButton():
    return wait_until_element_visible("//input[@id='login' and @name='login']");

def getCreateButton():
    return wait_until_element_visible("//a[@id='create_link']");

def getAssignee():
    return wait_until_element_visible("//input[@id='assignee-field']");

def getSite():
    return wait_until_element_visible("//select[@id='customfield_10013']");

def getSummaryTextField():
    return wait_until_element_visible("//input[@id='summary']");

def getDescriptionTextArea():
    return wait_until_element_visible("//textarea[@id='description']");

def getComponentTextArea():
    return wait_until_element_visible("//textarea[@id='components-textarea']");

def getTestEnvironmentRadio():
    return wait_until_element_visible("//input[@id='customfield_10024-1']");

def getPriority():
    return wait_until_element_visible("//input[@id='priority-field']");

def getLabels():
    return wait_until_element_visible("//textarea[@id='labels-textarea']");

def getFixVersion():
    return wait_until_element_visible("//textarea[@id='fixVersions-textarea']");

#----test script----
USERNAME = 'chris';
PASSWORD = 'Pwd123';
ASSIGNEE = USERNAME;
PASSWORD = PASSWORD;
SITE = 'SMSS';
SUMMARY = 'Discounts: USE_NEWDISCOUNTS is Y but Create Misc Invoice >> Discounts button triggers the old discounts popup';
DESCRIPTION = '*[http://chris-iis/700/914/]\n*chrisserver\mssqlserver2014\CMdiscountsPHP7 build 002\n';
COMPONENT = 'ART-Finance';
PRIORITY = "Medium";
#LABEL1 = 'efxphp7';
FIX_VERSION = 'ART-09.14.00';

driver = webdriver.Chrome()
driver.get(CONFIG_URL);
# needs to switch to the IFrame that includes the login form 
driver.switch_to.frame("gadget-0");

getUsernameTextfield().send_keys(USERNAME);
getPasswordTextField().send_keys(PASSWORD);
getLoginButton().click();

getCreateButton().click();
getAssignee().send_keys(USERNAME);
getAssignee().send_keys(keys.Keys.RETURN);


getSite().send_keys(SITE);
getSite().send_keys(keys.Keys.RETURN);

getSummaryTextField().send_keys(SUMMARY);
getDescriptionTextArea().send_keys(DESCRIPTION);
getComponentTextArea().send_keys(COMPONENT);
getComponentTextArea().send_keys(keys.Keys.TAB);

getTestEnvironmentRadio().click();
getPriority().send_keys(PRIORITY);
getPriority().send_keys(keys.Keys.RETURN);
#getLabels().send_keys(LABEL1);
#getLabels().send_keys(keys.Keys.RETURN);

getFixVersion().send_keys(FIX_VERSION);
getFixVersion().send_keys(keys.Keys.RETURN);
getFixVersion().send_keys(keys.Keys.TAB);


