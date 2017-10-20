import requests
import sys

response = requests.get('https://www.google.pl')

if response.status_code != 200:
    print("cos poszlo nie tak!")
    sys.exit(-1)

with open('google.html', 'w') as f:
    f.write(response.text)

print("plik zapisany! :)")