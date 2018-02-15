def debug_xpath(xpath): #https://stackoverflow.com/questions/5585343/getting-the-return-value-of-javascript-code-in-selenium
    script1 = "function getElementByXpath(path) {"
    script2 = "return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}"
    #script3 = "result = getElementByXpath(\""+xpath+"\")); return result;"
    script3 = "return getElementByXpath(\""+xpath+"\")" #returns a WebElement 
    
    script = script1 + script2 + script3
    print(script)
    result = driver.execute_script(script)
    print(result)

    element_text = result.text
    element_attribute_value = result.get_attribute('value')

    print ('element.text: {0}'.format(element_text))
    print ('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))