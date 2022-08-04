from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

username = input('Enter Username: ')
password = input('Enter Password: ')
message_to_send = input('Message to send: ')

browser = webdriver.Chrome('drivers/chromedriver')

# Instagram username list for DM:
with open('usernames.txt','r') as file:
	usernames=[]
	for line in file:
		strip_lines=line.strip()
		listli=strip_lines.split()
		print(listli)
		usernames.append(listli)


# Delay time between messages in sec:
between_messages = 2000

def auth(username, password):
	try:
		browser.get('https://www.instagram.com/')
		time.sleep(2)
		try:
			cookies = browser.find_element_by_xpath('/html/body/div[4]/div/div/button[2]')
		except:
			pass
		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,3))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,3))
		input_password.send_keys(Keys.ENTER)
	except:
		browser.quit()

# Sending messages:
def send_message(users, message):
	try:
		browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
		time.sleep(random.randrange(3,5))
		browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
		time.sleep(random.randrange(1,2))
		browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
		for user in users:
			time.sleep(random.randrange(1,2))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
			time.sleep(random.randrange(2,3))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').find_element_by_tag_name('button').click()
			time.sleep(random.randrange(3,4))
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
			time.sleep(random.randrange(3,4))
			text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			text_area.send_keys(message)
			time.sleep(random.randrange(2,4))
			text_area.send_keys(Keys.ENTER)
			print(f'Message successfully sent to {user}')
			time.sleep(between_messages)
			browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

	except Exception as err:
		print(err)
		browser.quit()


auth(username, password)
time.sleep(random.randrange(2,4))
send_message(usernames, message_to_send)
