from ZabbixSender import ZabbixSender, ZabbixPacket
from Monitoria.core.property import Property
from ..log.logtests import LogTest
import time
import datetime

class Zabbix:
	def __init__(self):
		try:
			self.server =  ZabbixSender(Property.ZABBIX_IP, Property.ZABBIX_PORT)
			print(self.server)
		except Exception as err:
			print(err)
			LogTest.write("Zabbix", "Conectar", "", "zabbix", "ERROR")

	def send(self, sensor, code):
		try:
			packet = ZabbixPacket()
			ts = time.time()
			packet.add(Property.ZABBIX_HOST, sensor, code, ts)
			print(datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))
			print(packet)
			self.server.send(packet)
		except Exception as err:
			print(err)
			LogTest.write("Zabbix", "Enviar Pacote", "", "zabbix", "ERROR")

