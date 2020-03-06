'''
How to use:
- Before deactivating your account on twitter, go to https://twitter.com/settings/your_twitter_data and click 'Download Data'. This script works on active accounts too.
- Extract the zip file that twitter gives you, then copy this script into the folder
- Your twitter follower / following file (choose which) must be placed in the same directory as this script or it won't run!
- You can deactivate your account now, since you've just pulled the data from it (which has your saved followers, those who followed you, etc)
'''
#WARNING!
'''
This script opens up all the links to every account you follow at once - I only had ~150 people I followed, but if you have hundreds or thousands this will probably crash your browser and make your PC hang.
Use at your own peril! Or modifiy it yourself for a high volume of followers/followed accounts.
'''

import sys, os
import webbrowser

LINKS = []
bites = str()

with open(os.path.join(sys.path[0], "following.js"), "r") as f:
    data = f.readlines()
    for i in str(data).split(','):
        bites = i.split("\"")
        for url in bites:
            if url[:5] == 'https' and url not in LINKS:
                LINKS.append(url)

charStrip = ['[', ']', '\'']
strippedLink = repr(LINKS)
for chars in charStrip:
    strippedLink = strippedLink.replace(chars, '')
    strippedLink = strippedLink.replace(', ', '\n')

with open(os.path.join(sys.path[0], "Following-these-accounts.text"), "w") as newFile:
    newFile.write(strippedLink)

#Disable this if you don't want it to open up a tab for every followed account in your browser
with open(os.path.join(sys.path[0], "Following-these-accounts.text"), "r") as savedLinks:
    for user in savedLinks:
    webbrowser.open(user)
