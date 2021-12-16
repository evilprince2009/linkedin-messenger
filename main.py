import random
import time
from selenium import webdriver

# Tell the bot from which page to start and where to end
start_page_index = 1  # Can't be less than 1
last_page_index = 100  # Can't be less than 1 , upper value depends on your connection

# Credentials and Message
username = ""
password = ""
message = "Write some message!"

# Don't touch if you are not proficient with Python , Selenium & DOM Elements
url = "https://www.linkedin.com"
browser = webdriver.Edge("msedgedriver.exe")
browser.maximize_window()
browser.get(url)
time.sleep(1)

username_field = browser.find_element_by_xpath(
    "//input[@name='session_key']")
password_field = browser.find_element_by_xpath(
    "//input[@name='session_password']")

username_field.send_keys(username)
password_field.send_keys(password)
submit = browser.find_element_by_xpath("//button[@type='submit']")
browser.execute_script("arguments[0].click();", submit)
time.sleep(1)

for i in range(start_page_index, last_page_index):
    network_url = url + "/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=" + \
        str(i) + "&sid=OEz"

    browser.get(network_url)
    time.sleep(2)

    all_buttons = browser.find_elements_by_tag_name("button")
    message_button = [btn for btn in all_buttons if btn.text == "Message"]

    name_tracker = 0
    for counter in range(0, len(message_button)):
        browser.execute_script(
            "arguments[0].click();", message_button[counter])
        time.sleep(2)

        main_div = browser.find_element_by_xpath(
            "//div[starts-with(@class, 'msg-form__msg-content-container')]")

        paragaraphs = browser.find_elements_by_tag_name("p")
        time.sleep(2)
        all_span = browser.find_elements_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute(
            "aria-hidden") == "true"]

        # Due to dynamic markup changes, this range keeps changing everyday which is disgusting
        # I will find a better way to fix it
        index_range = [*range(16, 53, 4)]

        greetings_prefix = ["Hello", "Hi", "Hey", "Greetings"]
        recipent_names = []

        for id in index_range:
            name = all_span[id].text.split(" ")[0]
            recipent_names.append(name)

        greetings_idx = random.randint(0, len(greetings_prefix) - 1)
        formatted_text_buffer = greetings_prefix[greetings_idx] + \
            " " + recipent_names[name_tracker] + "\n" + message
        name_tracker += 1
        time.sleep(2)

        paragaraphs[-5].send_keys(formatted_text_buffer)
        submit = browser.find_element_by_xpath("//button[@type='submit']")
        time.sleep(2)
        browser.execute_script("arguments[0].click();", submit)
        time.sleep(2)

        close_button = browser.find_element_by_xpath(
            "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        browser.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
