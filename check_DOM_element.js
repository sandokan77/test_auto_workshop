function getElementByXpath(path) {
  return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

console.log( getElementByXpath("/html/body/div[3]/div[1]/div[5]/div/div[3]/button/span") );
