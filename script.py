import webbrowser as wb
import config


'''
    A python script which, after execution, opens up the links from the config file in the browser.
    You can change or add new links in the config file
'''

for key in config.links:
    wb.open(config.links[key])
