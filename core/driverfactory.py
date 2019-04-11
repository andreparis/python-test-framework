from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.common.exceptions import ScreenshotException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InsecureCertificateException
from selenium.common.exceptions import UnknownMethodException
from selenium.common.exceptions import NoSuchWindowException
from Framework.core.property import Property

class DriverFactory:	

	_driver = None

	def __init__(self):
		pass

	@property
	def driver(self):
		return self._driver

	@staticmethod
	def driver(browser):
		if DriverFactory._driver != None:
			DriverFactory.exitTest()
			return DriverFactory.driver(browser)
		if browser == 1:
			DriverFactory._driver = webdriver.Chrome(executable_path=Property.PATH_CHROMEDRIVER)
		elif browser == 2:
			firefoxProfile = FirefoxProfile()
			firefoxProfile.set_preference("plugin.state.flash", 2)
			DriverFactory._driver = webdriver.Firefox(firefoxProfile, executable_path=Property.PATH_FIREFOXDRIVER)				
		return DriverFactory._driver

	@staticmethod
	def webDriverWait(by, origin, timeout):
		if by == "xpath":
			by = By.XPATH
		elif by == "id":
			by = By.ID
		WebDriverWait(DriverFactory._driver, timeout).until(EC.presence_of_element_located((by, origin)))

	@staticmethod
	def webDriverWaitAlert(timeout):
		WebDriverWait(DriverFactory._driver, timeout).until(EC.alert_is_present)

	@staticmethod
	def exitTest():
		try:
			if DriverFactory._driver != None:
				DriverFactory._driver.close()
				DriverFactory._driver.quit()
		except Exception as err:
			print(err)
		DriverFactory._driver = None
			
	@staticmethod
	def errorType(err):
		if type(err) == TimeoutException:
			return "TimeoutException"
		elif type(err) == WebDriverException:
			return "WebDriverException"
		elif type(err) == InvalidElementStateException:
			return "InvalidElementStateException"
		elif type(err) == NoSuchElementException:
			return "NoSuchElementException"
		elif type(err) == InvalidSwitchToTargetException:
			return "InvalidSwitchToTargetException"
		elif type(err) == ScreenshotException:
			return "ScreenshotException"
		elif type(err) == ElementNotVisibleException:
			return "ElementNotVisibleException"
		elif type(err) == ElementNotInteractableException:
			return "ElementNotInteractableException"
		elif type(err) == ElementNotSelectableException:
			return "ElementNotSelectableException"
		elif type(err) == ElementClickInterceptedException:
			return "ElementClickInterceptedException"
		elif type(err) == InsecureCertificateException:
			return "InsecureCertificateException"
		elif type(err) == UnknownMethodException:
			return "UnknownMethodException"
		elif type(err) == NoSuchWindowException:
			return "NoSuchWindowException"
		else:
			return "Exception"
