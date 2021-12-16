# LinkedIn Messenger
A simple bot to automate LinkedIn messages

## Made using
- Python
- Selenium
- Edge Browser
- VSCode

## How to make it work

Follow these steps below to run this

- Download Edge Driver or Chrome Driver for your operating system.

- Put it into the root directory.

- Open ```main.py``` file in your favorite code editor.

- Go to _line 16_, change it to:
  - ```browser = webdriver.Edge("msedgedriver.exe")``` if you want use Microsoft Edge.
  - ```browser = webdriver.Chrome("chromedriver.exe")``` if you want use Google Chrome.

- Fill these fields with proper credentials and parameters inside ```main.py``` file.

```
# Tell the bot from which page to start and where to end
start_page_index = 50
last_page_index = 60

# Credentials and Message
username = ""
password = ""
message = "Write some message!"
```

- Having Python installed on your machine, run ```pip install selenium``` on terminal.

- Now run ```python bot.py``` on terminal.

### What may go wrong

Inside the source code there is a place where I had to go through a list of ```<span></span>``` and look for recipents name on a regular interval. This range looks like ```index_range = [*range(16, 53, 4)]``` on _line 59_ which keeps changing due to dynamic markup change. If you can figure out how to handle this dynamic change or you have a better solution , let me know. Else don't worry, this won't stop you from sending automated messages.

### [Iben Nahian](https://www.linkedin.com/in/evilprince2009/)
