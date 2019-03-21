import webbrowser as wb
import config


'''
    A python script which, after execution, opens up the links I have saved in the browser.
    You can change or add new links in the config file
'''

for key in config.backing_tracks:
    wb.open(config.backing_tracks[key])
