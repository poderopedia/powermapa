import json
import urllib2
import base64

response=None
dc_url="https://www.documentcloud.org/api/documents/[id].json"
documents=db(db.documentCloud.is_active==True).select()
for doc in documents:
    print doc.dc_id
    url=dc_url.replace('[id]',doc.dc_id)
    print url
    authKey = base64.b64encode(dc_username+':'+dc_password)
    headers={"Content-Type":"application/json", "Authorization":"Basic " + authKey}
    request = urllib2.Request(url)

    for key,value in headers.items():
        request.add_header(key,value)
    try:
        response = urllib2.urlopen(request)
    except:
        print "Archivo Borrado"
        response=None
        doc.is_active=False

    if response!=None:
        #print response.info().headers
        jeison=json.loads(response.read())
        doc.title=jeison["document"]["title"]
        doc.description=jeison["document"]["description"]
        doc.source=jeison["document"]["source"]
        #doc.related_article=jeison["document"]["related_article"]
        #doc.published_url=jeison["document"]["published_url"]
        doc.access=jeison["document"]["access"]
        #doc.project=jeison["document"]["project"]
    doc.update_record()
    #for k,v in jeison.items():
    #    print k,v
