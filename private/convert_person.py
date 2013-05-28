# coding: utf8
from rdflib import ConjunctiveGraph
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from string import maketrans
import csv
#import pysesame

RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
BIO = Namespace("http://purl.org/vocab/bio/0.1/")
REL = Namespace("http://purl.org/vocab/relationship/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
RDFS=Namespace('http://www.w3.org/2000/01/rdf-schema#')
DCTERMS = Namespace("http://purl.org/dc/terms/")
DC = Namespace("http://purl.org/dc/elements/1.1/")
VANN = Namespace("http://purl.org/vocab/vann/")
ORG = Namespace("http://www.w3.org/ns/org#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
BCNBIO = Namespace("http://datos.bcn.cl/ontologies/bcn-biographies#")
PODER = Namespace("http://poderopedia.com/vocab/")




jg=ConjunctiveGraph()
jg.bind('rdf',RDF)
jg.bind('owl',OWL)
jg.bind('skos',SKOS)
jg.bind('bio',BIO)
jg.bind('rel',REL)
jg.bind('foaf',FOAF)
jg.bind('rdfs',RDFS)
jg.bind('dcterms',DCTERMS)
jg.bind('dc',DC)
jg.bind('vann',VANN)
jg.bind('org',ORG)
jg.bind('xsd',XSD)
jg.bind('bcnbio',BCNBIO)
jg.bind('poder',PODER)


# Incremental counter for person IDs
pid=0

personas=db(db.persona.is_active==True).select()

for persona in personas:
    ##alias=persona.alias.lower().replace(' ','_').replace(',','')
    intab=
    trans=maketrans(u'ñáéíóúÑÁÉÍÓÚ', 'naeiounaeiou')
    alias=persona.alias.lower().replace(' ','_').replace(',','')
    alias=alias.translate(trans)
    print alias
    person=PODER[str(alias)]
    jg.add((person, RDF.type, FOAF['Person']))
    jg.add((person, PODER['firstLastName'],Literal(persona.firstLastName)))
    jg.add((person, PODER['otherLastName'],Literal(persona.otherLastName)))
    jg.add((person, PODER['firstName'],Literal(persona.firstName)))
    jg.add((person,PODER['alias'],Literal(persona.alias)))
    ##jg.add((person,PODER['hasAlternativeMainSector'],Literal))
    jg.add((person,PODER['hasTaxId'],Literal(persona.ICN)))



    
# Print the serialized graph
data=jg.serialize(format='xml')
print data
#c=pysesame.connection('http://freerisk.org:8280/openrdf-sesame/')
#c.use_repository('joblistings')
#print c.postdata(data)


    
