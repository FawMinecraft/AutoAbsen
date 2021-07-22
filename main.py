import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import schedule

i = 1

browser = webdriver.Chrome()

usernameStr = '0078904560'
passwordStr = 'R8F27M'

browser.get('https://elearning.mtsn2ponorogo.sch.id/')

username = browser.find_element_by_name('username')
username.send_keys(usernameStr)

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_class_name('fa-sign-in')
signInButton.click()

lewatitmbl = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "introjs-skipbutton")))

lewatitmbl.click()

#VAR VAR VAR VAR VAR VAR VAR VAR VAR VAR VAR


def mnbk():
	bk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP BIMBINGAN DAN KONSELING')))
	bk.click()
	
	bkba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	bkba.click()
	
	bkab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	bkab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnipa():
	ipa = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K IPA BU MUNTIK')))
	ipa.click()

	ipaba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	ipaba.click()

	ipaab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	ipaab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnmtk():
	mtk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP - MATHEMATICS')))
	mtk.click()

	mtkba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	mtkba.click()

	mtkab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	mtkab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnips():
	ips = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP - IPS')))
	ips.click()

	ipsba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	ipsba.click()

	ipsab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	ipsab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnpkn():
	pkn = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP PPKn')))
	pkn.click()

	pknba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	pknba.click()

	pknab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	pknab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnakd():
	akidah = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K AKIDAH AKHLAK')))
	akidah.click()

	akidahba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	akidahba.click()

	akidahab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	akidahab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnski():
	ski = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-SKI')))
	ski.click()

	skiba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	skiba.click()

	skiab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	skiab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnind():
	ind = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP BAHASA INDONESIA')))
	ind.click()

	indba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	indba.click()

	indab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	indab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnpjok():
	pjok = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K-PJOK')))
	pjok.click()

	pjokba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	pjokba.click()

	pjokab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	pjokab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnqdt():
	qdt = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'VIII K(ICP) - QURDITS Badar Basuki')))
	qdt.click()

	qdtba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	qdtba.click()

	qdtab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	qdtab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnpka():
	pka = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'VIIIK ICP Prakarya')))
	pka.click()

	pkaba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	pkaba.click()

	pkaab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	pkaab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnbtq():
	btq = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP- BTQ')))
	btq.click()

	btqba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	btqba.click()

	btqab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	btqab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnarb():
	arb = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP BAHASA ARAB')))
	arb.click()

	arbba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	arbba.click()

	arbab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	arbab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnjwa():
	jwa = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K BHS JAWA')))
	jwa.click()

	jwaba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	jwaba.click()

	jwaab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	jwaab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnsbk():
	sbk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-SBK')))
	sbk.click()

	sbkba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	sbkba.click()

	sbkab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	sbkab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mnfkh():
	fkh = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP FIKIH')))
	fkh.click()

	fkhba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	fkhba.click()

	fkhab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	fkhab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


def mning():
	ing = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-SBK')))
	ing.click()

	ingba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	ingba.click()

	ingab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	ingab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()


#JADWAL JADWAL JADWAL JADWAL JADWAL JADWAL JADWAL


def senin():
	mnbk()
	mnind()
	mnipa()
	mnqdt()
	mnsbk()
	mnmtk()

def selasa():
	mnbk()
	mnmtk()
	mning()
	mnakd()
	mnpka()
	mnbtq()

def rabu():
	mnbk()
	mnind()
	mnarb()
	mnfkh()
	mnipa()

def kamis():
	mnbk()
	mnipa()
	mning()
	mnski()
	mnjwa()

def jumat():
	mnbk()
	mnpkn()
	mnarb()
	mnips()
	mnsbk()

def sabtu():
	mnbk()
	mnind()
	mnips()
	mnmtk()
	mnpjok()


schedule.every().monday.at("07:00").do(senin)
schedule.every().tuesday.at("07:00").do(selasa)
schedule.every().wednesday.at("07:00").do(rabu)
schedule.every().thursday.at("07:00").do(kamis)
schedule.every().friday.at("07:00").do(jumat)
schedule.every().saturday.at("07:00").do(sabtu)

while i == 1:
	schedule.run_pending()
	sleep(1)
