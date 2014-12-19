from selenium import webdriver

MAIN_URL = 'https://go.sfu.ca/psp/paprd/EMPLOYEE/h/?tab=PAPP_GUEST'

OPEN_IMG_SRC = 'https://sims-prd.sfu.ca/cs/csprd/cache/PS_CS_STATUS_OPEN_ICN_1.gif'

def check_course(course, coursenum, section):
	browser = webdriver.PhantomJS()
	browser.set_window_size(1400, 1000)

	# Go to main page
	browser.get(MAIN_URL)
	# Go to course catalog page
	browser.implicitly_wait(10)
	browser.find_element_by_link_text("Browse Course Catalog").click()
	# switch to frame containing the elements we're looking for
	browser.switch_to_frame("TargetContent")
	# Go to course's alphanumeric category
	browser.find_element_by_id("DERIVED_SSS_BCC_SSR_ALPHANUM_" + course[0]).click()
	# Expand Course View
	browser.implicitly_wait(10)
	browser.find_element_by_partial_link_text(course).click()
	# Click on course requested
	browser.implicitly_wait(10)
	browser.find_element_by_link_text(coursenum).click()
	# View all class sections
	browser.implicitly_wait(10)
	browser.find_element_by_id("DERIVED_SAA_CRS_SSR_PB_GO").click()
	# Get the table row for the section that we're looking for
	browser.implicitly_wait(10)
	browser.find_element_by_partial_link_text(section).click()

	browser.implicitly_wait(10)
	div_element = browser.find_element_by_id("win0divSSR_CLS_DTL_WRK_SSR_STATUS_LONG")
	img_element = div_element.find_element_by_class_name("SSSIMAGECENTER")
	element_src = img_element.get_attribute('src')
	if (element_src == OPEN_IMG_SRC):
		print "course has seats\n"
		browser.quit()
		return True
	else:
		print "course is full\n"
		browser.quit()
		return False


#Browser goes on course page with all class sections open
print "should print has seats \n"
check_course("HIST", "101", "D100-LEC")

print "should print is full \n"
check_course("HIST", "101", "D101-TUT")

