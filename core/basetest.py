# Developed by André Paris - Software Engineer
# https://www.linkedin.com/in/andre-paris-02626153/
#
# You can find this framework at: https://github.com/andreparis/python-test-framework-with-zabbix

from ..core.DSL import DSL
from Framework.core.driverfactory import DriverFactory
from Framework.core.property import Property

class BaseTest:	

	def __init__(self, url, className, browser = 1):
		try:
			self.dsl = DSL(url, className, browser)
		except Exception as err:
			print(err)
			

	def finish(self):
		try:
			self.dsl.method = "Fim"
			if self.dsl.sentZabbixError is False:
				self.dsl.zabbixSend(Property.ZABBIX_CODE_SUCCESS)	
			self.dsl.quit()
			self.dsl = None		
		except Exception as err:
			print(err)		