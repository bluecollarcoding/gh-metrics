import requests
public = requests.get('https://api.github.com/orgs/tendermint/repos?type=public').json()

print "Main public repos:"

for p in public:
    print p['full_name']
