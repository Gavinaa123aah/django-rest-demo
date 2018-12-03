import urllib2
import json
contents = urllib2.urlopen("http://127.0.0.1:8000/users").read()
print (json.loads(contents))
