from selenium import webdriver

MAIN_URL = 'https://go.sfu.ca/psp/paprd/EMPLOYEE/h/?tab=PAPP_GUEST'

OPEN_IMG_SRC = 'https://sims-prd.sfu.ca/cs/csprd/cache/PS_CS_STATUS_OPEN_ICN_1.gif'

def go_to(course, coursenum, section):
	# switch to frame containing the elements we're looking for
	browser.switch_to_frame("TargetContent")
	# Go to course's alphanumeric category
	browser.find_element_by_id("DERIVED_SSS_BCC_SSR_ALPHANUM_" + course[0]).click()
	# Expand Course View
	browser.find_element_by_partial_link_text(course).click()
	# Click on course requested
	browser.find_element_by_link_text(coursenum).click()
	# View all class sections
	browser_find_element_by_id("DERIVED_SAA_CRS_SSR_PB_GO").click()
	print element.get_attribute("innerHTML")
	
browser = webdriver.PhantomJS()
browser.set_window_size(1400, 1000)

#Go to main page
browser.get(MAIN_URL)
print "got onto main page: " + browser.current_url

#Go to course catalog page
browser.find_element_by_link_text("Browse Course Catalog").click()
print "clicked on " + browser.current_url
go_to("ACMA", "210")
browser.quit()


