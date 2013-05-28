__author__ = 'Evolutiva'
# coding: utf8
from rdflib import ConjunctiveGraph
from rdflib import Namespace, BNode, Literal, RDF, URIRef

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
TESTING = Namespace("http://test.hackatons.org/PowerMapa/plugin_rdf/ld/read/")
TEST = Namespace("http://test.hackatons.org/PowerMapa/plugin_rdf/ld/read/persona/")
TEST0 = Namespace("http://test.hackatons.org/PowerMapa/plugin_rdf/ld/read/country/")
TEST1 = Namespace("http://test.hackatons.org/PowerMapa/plugin_rdf/ld/read/relPersona/")
TEST2 = Namespace("http://test.hackatons.org/PowerMapa/biography/longBio/")


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
jg.bind('test',TEST)
jg.bind('test',TEST1)
jg.bind('testing',TESTING)

orgs = db(db.Organizacion.is_active==True).select()
for org in orgs:

    organization=TESTING['Organizacion/'+str(org.id)]
    ##generic
    if(org.tipoOrg==1):
        jg.add((organization, RDF.type, PODER['AcademicOrganization']))
    elif(org.tipoOrg==2):
        jg.add((organization, RDF.type, PODER['Company']))
    elif(org.tipoOrg==4):
        jg.add((organization, RDF.type, PODER['PoliticalOrganization']))
    elif(org.tipoOrg==5):
        jg.add((organization, RDF.type, PODER['ReligiousOrganization']))
    elif(org.tipoOrg==6):
        jg.add((organization, RDF.type, PODER['RestrictedAccessOrganization']))
    elif(org.tipoOrg==7):
        jg.add((organization, RDF.type, PODER['ProgrammaticOrganization']))
    elif(org.tipoOrg==9):
        jg.add((organization, RDF.type, PODER['NonGovernmentalOrganization']))
    elif(org.tipoOrg==10):
        jg.add((organization, RDF.type, PODER['InternationalOrganization']))
    else:
        jg.add((organization, RDF.type, FOAF['Organization']))
    if(org.alias!=None):
        jg.add((organization,PODER['alias'],Literal(org.alias)))
    if(org.hasTaxId!=None):
        jg.add((organization,PODER['hasTaxId'],Literal(org.hasTaxId)))
    if(org.hasSocialReason!=None):
        jg.add((organization,PODER['hasSocialReason'],Literal(org.hasSocialReason)))

print jg

data=jg.serialize(format='xml')
if(data!=None):
    filename = open('applications/PowerMapa/private/orgs.rdf','w')
    filename.write(data)
    filename.close()