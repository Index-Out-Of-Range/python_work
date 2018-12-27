from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re


def jump_page_to_get_email(driver, page_url, teacher_dict):
	driver.get(page_url)
	elememts = driver.find_elements_by_class_name("span9")
	# teacher_dict = {}
	for element in elememts[1:]:
		info_list = element.text.split()
		for info in info_list:
			if re.match(r"^(\w|.)*@(\w|.)*$", info):
				teacher_dict[info_list[0]] = info
				continue
	# print(teacher_dict)

	button = driver.find_element_by_xpath('//*[@id="techerinformationList"]/tfoot/tr/td/div/ul/li[5]/a')
	# print(button.get_attribute('href'))
	next_page_url = button.get_attribute('href')
	if next_page_url:
		ActionChains(driver).click(button).perform()
		jump_page_to_get_email(driver, next_page_url, teacher_dict)
	driver.quit()


if __name__ == "__main__":
	teacher_dict = {}
	driver = webdriver.Chrome()
	first_page_url = "http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52?limitstart=0"
	jump_page_to_get_email(driver, first_page_url, teacher_dict)
	print(teacher_dict)