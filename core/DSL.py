# Developed by André Paris - Software Engineer
# https://www.linkedin.com/in/andre-paris-02626153/
#
# You can find this framework at: https://github.com/andreparis/python-test-framework-with-zabbix

from ..core.driverfactory import DriverFactory
from ..log.logtests import LogTest
from Framework.core.property import Property
from Framework.core.zabbix import Zabbix
import win32com.client
import datetime
import time
import pyautogui

class DSL:
	
	### Inicia e Finaliza driver ###
	def __init__(self, url, className, browser):
		self.logname = className
		LogTest.write("Init", "Inicia", "browser", self.logname)						
		self.method = ""
		self.sentZabbixError = False
		try:
			self.driver = DriverFactory.driver(browser)
			self.driver.get(url)
			self.driver.maximize_window()
		except Exception as err:
			print(err)
			msg = "Não foi possível localizar o driver Chrome"
			self.errorHandling(err, msg)

	def quit(self):	
		try:	
			DriverFactory.exitTest()
		except Exception as err:
			print(err)

	def printScreen(self):
		try:
			LogTest.write("Quit", "Finaliza", "browser", self.logname)
			currTime = str(datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
			imageName = Property.PATH_SCREENSHOTS+self.logname+"\\" + currTime + "_"  + self.logname + ".png"
			print("starting screenshot")
			self.driver.save_screenshot(imageName)
			print("finishing screenshot")			
		except Exception as err:
			print(err)
			msg = "Erro ao capturar imagem da tela"
			LogTest.write(self.method, "Exception", msg, self.logname, "ERROR")
			#self.errorHandling(err, msg)		

	### Setters - TextField and TextArea ###

	def setText(self, by, attr,text):
		try:
			LogTest.write(self.method, "Escrve"+text, attr, self.logname)
			self.driver.find_element(by, attr).send_keys(text)
		except Exception as err:
			print(err)
			msg = "Não encontrou " + attr + " para escrever" + text
			self.errorHandling(err, msg)

	def setTextById(self, id, text):
		try:
			LogTest.write(self.method, "Escrve "+text, id, self.logname)
			self.driver.find_element_by_id(id).send_keys(text)				
		except Exception as err:
			print(err)
			msg = "Não encontrou " + id + " para escrever" + text
			self.errorHandling(err, msg)

	def setTextByXpath(self, xpath, text):
		try:
			LogTest.write(self.method, "Escrve "+text, xpath, self.logname)
			self.driver.find_element_by_xpath(xpath).send_keys(text)
		except Exception as err:
			print(err)
			msg = "Não encontrou " + xpath + " para escrever" + text
			self.errorHandling(err, msg)

	### Getters - TextField and TextArea ###

	def getText(self, by, attr):
		try:
			LogTest.write(self.method, "Obtem texto", attr, self.logname)
			self.driver.find_element(by, attr).text
		except Exception as err:
			print(err)
			msg = "Não encontrou " + attr
			self.errorHandling(err, msg)

	def getTextById(self, id):
		try:
			LogTest.write(self.method, "Obtem texto", id, self.logname)
			self.driver.find_element_by_id(id).text
		except Exception as err:
			print(err)
			msg = "Não encontrou " + id
			self.errorHandling(err, msg)

	def getTextByXpath(self, xpath):
		try:
			LogTest.write(self.method, "Obtem texto", xpath, self.logname)
			self.driver.find_element_by_xpath(xpath).text
		except Exception as err:
			print(err)
			msg = "Não encontrou " + xpath
			self.errorHandling(err, msg)

	### Buttons ###

	def click(self, by, attr):
		try:
			LogTest.write(self.method, "Clica", attr, self.logname)
			self.driver.find_element(by, attr).click()
		except Exception as err:
			print(err)
			msg = "Não foi possível clicar em " + attr
			self.errorHandling(err, msg)

	def clickById(self, id):
		try:
			LogTest.write(self.method, "Clica", id, self.logname)
			self.driver.find_element_by_id(id).click()
		except Exception as err:
			print(err)
			msg = "Não foi possível clicar em " + id
			self.errorHandling(err, msg)

	def clickByXpath(self, xpath):
		try:
			LogTest.write(self.method, "Clica", xpath, self.logname)
			self.driver.find_element_by_xpath(xpath).click()
		except Exception as err:
			print(err)
			msg = "Não foi possível clicar em " + id
			self.errorHandling(err, msg)

	def attachFile(self, filepath, xpath):
		try:
			LogTest.write(self.method, "Anexar", filepath, self.logname)
			self.driver.find_element_by_xpath(xpath).send_keys(filepath)
		except Exception as err:
			print(err)
			msg = "Não foi anexar o arquivo " + filepath
			self.errorHandling(err, msg)


	### Link ###

	def getLinkById(self, id):
		try:
			LogTest.write(self.method, "Obtem link", id, self.logname)
			self.driver.find_element_by_id(id).get_attribute('href')
		except Exception as err:
			print(err)
			msg = "Não encontrou o link " + id
			self.errorHandling(err, msg)

	def getLinkByXpath(self, xpath):
		try:
			LogTest.write(self.method, "Obtem link", xpath, self.logname)
			self.driver.find_element_by_xpath(xpath).get_attribute('href')
		except Exception as err:
			print(err)
			msg = "Não encontrou o link " + xpath
			self.errorHandling(err, msg)

	### Waiters ###

	def waitByXpath(self, xpath, timeout):
		try:
			LogTest.write(self.method, "Espera elemento", xpath, self.logname)
			DriverFactory.webDriverWait("xpath", xpath, timeout)
		except Exception as err:
			print(err)
			msg = "Tempo de espera de "+str(timeout)+" esgotado ao esperar por " + xpath
			self.errorHandling(err, msg)

	def waitByXpathFix(self, timeout):
		try:			
			LogTest.write(self.method, "Espera Fixa", "thread", self.logname)
			time.sleep(timeout)
		except Exception as err:
			print(err)
			msg = "Tempo de espera de "+str(timeout)+" esgotado!"
			self.errorHandling(err, msg)

	def waitByXpathImplicit(self, timeout):
		try:
			LogTest.write(self.method, "Espera Implicita", "thread", self.logname)
			self.driver.implicitly_wait(timeout)
		except Exception as err:
			print(err)
			msg = "Tempo de espera de "+str(timeout)+" esgotado!"
			self.errorHandling(err, msg)

	### Windows Handle ###

	def getWindow(self, index):
		try:
			LogTest.write(self.method, "Obtem nova janela aberta", str(index), self.logname)
			return self.driver.window_handles[index]
		except Exception as err:
			print(err)
			msg = "Não existe a janela " + str(index)
			self.errorHandling(err, msg)


	def switchWindow(self, window):
		try:
			LogTest.write(self.method, "Mudar Janela", str(window), self.logname)
			self.driver.switch_to.window(window)
		except Exception as err:
			print(err)
			msg = "Não existe a janela " + str(window)
			self.errorHandling(err, msg)

	def closeCurrentWindow(self):
		try:
			LogTest.write(self.method, "Fechar Janela Atual", "", self.logname)
			self.driver.close()
		except Exception as err:
			print(err)
			msg = "Não foi possível fechar a janela!"
			self.errorHandling(err, msg)

	### Frame ###

	def switchFrame(self, xpath):
		try:
			LogTest.write(self.method, "Mudar para frame", xpath, self.logname)
			iframe = self.driver.find_element_by_xpath(xpath)
			self.driver.switch_to.frame(iframe)
		except Exception as err:
			print(err)
			msg = "Frame " + str(window) + " não encontrado"
			self.errorHandling(err, msg)

	def switchDefaultContent(self):
		try:
			LogTest.write(self.method, "Mudar para frame principal", "", self.logname)
			self.driver.switch_to.default_content()
		except Exception as err:
			print(err)
			msg = "Não foi possível retorna a pagina principal"
			self.errorHandling(err, msg)


	### Alerts ###

	def switchToAlert(self):
		try:
			LogTest.write(self.method, "Mudar para alerta", "", self.logname)
			#DriverFactory.webDriverWaitAlert(30)
			return self.driver.switch_to_alert()
		except Exception as err:
			print(err)
			msg = "Não foi possível mudar para alerta"
			self.errorHandling(err, msg)

	def setTextAlert(self, text, alert):
		try:
			LogTest.write(self.method, "Escreve em alerta", text, self.logname)
			alert.send_keys(text)
		except Exception as err:
			print(err)
			msg = "Não foi possível escrever "+text+" no alerta"
			self.errorHandling(err, msg)

	def acceptAlert(self, alert):
		try:
			LogTest.write(self.method, "Confirma Alerta", "", self.logname)
			alert.accep()
		except Exception as err:
			print(err)
			msg = "Não foi possível confirmar alerta"
			self.errorHandling(err, msg)

	### Win32com handler

	def switchToPopupWin32com(self):
		try:
			return win32com.client.Dispatch("WScript.Shell")
		except Exception as err:
			print(err)

	def setTextPopupWin32com(self, shell, text):
		try:
			shell.Sendkeys(text)
		except Exception as err:
			print(err)


	### Mouse Handler ###

	def mouseClick(self, x, y):
		try:
			LogTest.write(self.method, "Mouse Clica", "", self.logname)
			pyautogui.click(x, y, button='left')
		except Exception as err:
			msg = "Incapaz de usar o mouse para clicar"
			self.errorHandling(err, msg)

	### Zabbix Event Handle ###

	def zabbixSend(self, code):
		LogTest.write(self.method, "Enviar para Zabbix", str(code), self.logname)
		zabbix = Zabbix()
		zabbix.send(self.logname, code)
		

	### Errors Handling ###

	def errorHandling(self, err, msg):
		errClass = DriverFactory.errorType(err)
		LogTest.write(self.method, errClass, msg, self.logname, "ERROR")
		self.sentZabbixError = True
		self.zabbixSend(Property.ZABBIX_CODE_ERROR)
		self.printScreen()
		raise Exception(errClass + " " + msg)


