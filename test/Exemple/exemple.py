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