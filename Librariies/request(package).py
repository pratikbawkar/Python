# making a program to get itunes page with specific song and band  

""" import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

respone = request.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(respone.json()) """

# we will import json so that we can undestand json document better 

# making a program to get itunes page with specific song and band  
import json  # comes manually with python and dont need to pip install 
import requests
import sys

if len(sys.argv) != 2:
    sys.exit() # we use this instead of break because we need to exit from whole program

respone = request.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# above we made a http request using python to the server 

""" print(json.dumps(respone.json(), indent == 2)) """  # we dont need to need to print out the contents of that respone cause thats not intresting or pretty for anyone 

# instead lets do this 
# creating a new variable  
o = respone.json() # just giving o as in object  # on thiss grabbing from the variable which contains the server's respone the Json object that we care about.
for result in o["results"]: # by reading documentation and by poking around we got to know that object has a key called results and this result key is a list
# the list contains only one song cause we have limited it to only one song 
# everytime it iterate a loop its gonna print the current results track name 
# we can change the limit from one to many numbers to get more song 
    print(result["trackName"])


