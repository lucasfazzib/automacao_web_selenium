from selenium import webdriver

navegador = webdriver.Chrome()


navegador.get("https://ri.magazineluiza.com.br/")

#navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img').click()
#navegador.find_element_by_xpath('//*[@id="4zS989en0CKjhpbeCLPGMw=="]').click()


element = navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img')
navegador.execute_script("arguments[0].click();", element)
element2 = navegador.find_element_by_xpath('//*[@id="4zS989en0CKjhpbeCLPGMw=="]')
navegador.execute_script("arguments[0].click();", element2)