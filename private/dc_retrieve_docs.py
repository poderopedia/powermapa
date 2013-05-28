__author__ = 'Evolutiva'

import json
import urllib2
import base64

response=None
dc_url="https://www.documentcloud.org/api/projects.json"

authKey = base64.b64encode(dc_username+':'+dc_password)
headers={"Content-Type":"application/json", "Authorization":"Basic " + authKey}
request = urllib2.Request(dc_url)

for key,value in headers.items():
    request.add_header(key,value)
try:
    response = urllib2.urlopen(request)
except:
    response=None

if response!=None:
    #print response.info().headers
    jeison=json.loads(response.read())
    for project in jeison["projects"]:
        for document in project["document_ids"]:
            doc=db((db.documentCloud.dc_id==document) & (db.documentCloud.is_active==True)).select()
            if len(doc)==0:
                docs=db.documentCloud.validate_and_insert(dc_id=document,title='recientes',project=project['id'],is_active=True)
                if docs.errors: print docs.errors

    #for k,v in jei
