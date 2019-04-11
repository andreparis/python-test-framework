# python-test-framework-with-zabbix

This frameworke developed in Python 3 uses selenium for acceptance tests, sending the results for Zabbix. 
You also can use it for building robots.

#Run:

As a good practice, you should call all your classes in TestSuit file, then, you will compile this code as a package:
py -m Framework.suites.TestSuit

#You must install, with pip, the followings libs:

selenium
win32com
pyautogui
