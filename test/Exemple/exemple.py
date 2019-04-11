# Developed by André Paris - Software Engineer
# https://www.linkedin.com/in/andre-paris-02626153/
#
# You can find this framework at: https://github.com/andreparis/python-test-framework-with-zabbix

from Framework.core.basetest import *
from Framework.core.property import Property

class Exemple(BaseTest):
	def __init__(self):
		try:
			super().__init__("WEBSITE", Property.ZABBIX_FLAG_EXAMPLE)
			self.checkInstitucionalLoaded()
		except Exception as err:
			print(err)
		self.finish()

	def checkInstitucionalLoaded(self):
		self.dsl.method = "NameOfMethodForLog"
		xpath = 'xpath'
		self.dsl.waitByXpath(xpath, 30)	