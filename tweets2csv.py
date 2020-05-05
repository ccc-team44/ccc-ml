import os
import time

from cloudant.client import CouchDB

user = "admin"
password = "1111"
# db_host = "172.26.130.31:5984"
db_host = "http://127.0.0.1:5984"

tweetMap= None
with open('map.js', 'r') as file:
    tweetMap = file.read().replace('\n', '')
	
print(tweetMap)
	
client = CouchDB(user, password, url=db_host, connect=True)
session = client.session()
print('Databases: {0}'.format(client.all_dbs()))
db = client['tweets']

new_view = {
	'_id': '_design/'+ str(time.time()),
	'_rev': 'rev-code',
	'views': {
		'ml': {
			'map': f'''{tweetMap}'''
		}
	},
	'language': 'javascript'
}

# create new view like a doc
db.create_document(new_view)

results = db.get_view_result(new_view['_id'], 'ml')

for result in results:
	try:
		print(result)
	except Exception:
		pass
