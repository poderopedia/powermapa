__author__ = 'Evolutiva'
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

# Incremental counter for person IDs
pid=0; cid=0; bid=0

detalle =db((db.relFamiliar.origenP==906)).select()
##personas=db((db.persona.is_active==True)&(db.relFamiliar.origenP==906)&(db.relFamiliar.destinoP==persona.id)).select()

for relfam in detalle:
    persona=db.persona(relfam.destinoP)
    alias=persona.alias.lower().replace(' ','_').replace(',','')
    alias=alias.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    alias=alias.replace('Á','a').replace('É','e').replace('Í','i').replace('Ó','o').replace('Ú','u')
    alias=alias.replace('Ñ','n').replace('ñ','n').replace('è','e').replace('“','').replace('”','')
    alias=alias.replace('ü','u').replace('ö','o').replace('ä','a')
    ##alias=alias.translate(trans)
    print alias
    person=TEST[str(persona.id)]
    jg.add((person, RDF.type, FOAF['Person']))
    if(persona.firstLastName!=None):
        jg.add((person, PODER['firstLastName'],Literal(persona.firstLastName)))
    if(persona.otherLastName!=None):
        jg.add((person, PODER['otherLastName'],Literal(persona.otherLastName)))
    if(persona.firstName!=None):
        jg.add((person, PODER['firstName'],Literal(persona.firstName)))
    if(persona.longBio!=None):
        longbiography=TESTING['LongBiography/'+str(persona.id)]
        jg.add((longbiography,RDF.type,PODER['LongBiography']))
        jg.add((person,PODER['hasLongBiography'],longbiography))
    if(persona.countryofResidence!=None):
        country=db.country(persona.countryofResidence)
        name=country.name.strip().capitalize().replace(' ','_').replace(',','')
        jg.add((person,PODER['countryOfResidence'],PODER[name]))
    jg.add((person,PODER['alias'],Literal(persona.alias)))
    ##jg.add((person,PODER['hasAlternativeMainSector'],Literal))
    if(persona.ICN!=None):
        jg.add((person,PODER['hasTaxId'],Literal(persona.ICN)))


familiares=db((db.relFamiliar.is_active==True)&(db.relFamiliar.origenP==db.persona.id)&(db.persona.is_active==True)
& (db.relFamiliar==906)&(db.relFamiliar.parentesco==db.tipoParentesco.id)).select()

for familiar in familiares:
    activo=db((db.persona.id==familiar.relFamiliar.destinoP)&(db.persona.is_active==True)).select()

    if(len(activo)==1):
        ##hasSibling
        if(familiar.relFamiliar.parentesco==3):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasSibling'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasChild
        if(familiar.relFamiliar.parentesco==1):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasChild'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasUncle
        if(familiar.relFamiliar.parentesco==4):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasAuntOrUncle'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasCousin
        if(familiar.relFamiliar.parentesco==6):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasCousin'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasGrandChild
        if(familiar.relFamiliar.parentesco==7):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasGrandChild'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasGrandparent
        if(familiar.relFamiliar.parentesco==8):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasGrandparent'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasNieceOrNephew
        if(familiar.relFamiliar.parentesco==5):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasNieceOrNephew'],TEST[str(familiar.relFamiliar.destinoP)]))
            ##hasParent
        if(familiar.relFamiliar.parentesco==2):
            jg.add((TEST[str(familiar.relFamiliar.origenP)],PODER['hasParent'],TEST[str(familiar.relFamiliar.destinoP)]))

relations = db((db.relPersona.is_active==True)&(db.relPersona.origenP==906)&(db.relPersona.origenP==db.persona.id)&(db.persona.is_active==True)).select()
for relation in relations:
    print relation.relPersona.origenP
    ##hasSpouse
    if(relation.relPersona.relacion==6):
        jg.add((TEST[str(relation.relPersona.origenP)],PODER['hasSpouse'],TEST[str(relation.relPersona.destinoP)]))
        ##Dating
    if(relation.relPersona.relacion==8):
        jg.add((TEST[str(relation.relPersona.origenP)],PODER['DomesticPartnership'],TEST[str(relation.relPersona.destinoP)]))
        ##ClassMate
    if(relation.relPersona.relacion==32):
        jg.add((TEST[str(relation.relPersona.origenP)],PODER['Classmate'],TEST[str(relation.relPersona.destinoP)]))

orgs = db((db.Organizacion.is_active==True)&(db.RelPersOrg.destinoO==db.Organizacion.id)&(db.RelPersOrg.origenP==906)).select()
for org in orgs:

    organization=TESTING['Organizacion/'+str(org.Organizacion.id)]
    ##generic
    if(org.Organizacion.tipoOrg==1):
        jg.add((organization, RDF.type, PODER['AcademicOrganization']))
    elif(org.Organizacion.tipoOrg==2):
        jg.add((organization, RDF.type, PODER['Company']))
    elif(org.Organizacion.tipoOrg==4):
        jg.add((organization, RDF.type, PODER['PoliticalOrganization']))
    elif(org.Organizacion.tipoOrg==5):
        jg.add((organization, RDF.type, PODER['ReligiousOrganization']))
    elif(org.Organizacion.tipoOrg==6):
        jg.add((organization, RDF.type, PODER['RestrictedAccessOrganization']))
    elif(org.Organizacion.tipoOrg==7):
        jg.add((organization, RDF.type, PODER['ProgrammaticOrganization']))
    elif(org.Organizacion.tipoOrg==9):
        jg.add((organization, RDF.type, PODER['NonGovernmentalOrganization']))
    elif(org.Organizacion.tipoOrg==10):
        jg.add((organization, RDF.type, PODER['InternationalOrganization']))
    else:
        jg.add((organization, RDF.type, FOAF['Organization']))
    if(org.Organizacion.alias!=None):
        jg.add((organization,PODER['alias'],Literal(org.Organizacion.alias)))
    if(org.Organizacion.hasTaxId!=None):
        jg.add((organization,PODER['hasTaxId'],Literal(org.Organizacion.hasTaxId)))
    if(org.Organizacion.hasSocialReason!=None):
        jg.add((organization,PODER['hasSocialReason'],Literal(org.Organizacion.hasSocialReason)))

orgsrelations = db((db.RelPersOrg.is_active==True)&(db.RelPersOrg.origenP==906)&(db.persona.id==db.RelPersOrg.origenP)&(db.persona.is_active==True)
                &(db.Organizacion.id==db.RelPersOrg.destinoO)&(db.Organizacion.is_active==True)&(db.RelPersOrg.specificRelation==db.tipoRelacionP20.id)).select()
for orgs in orgsrelations:
    person=TEST[str(906)]
    if(orgs.tipoRelacionP20.parent==1):
        jg.add((person,PODER['academicParticipant'],TESTING['Organization/'+str(orgs.RelPersOrg.destinoO)]))
    elif(orgs.tipoRelacionP20.parent==2):
        jg.add((person,PODER['hasEconomicOrganizationParticipant'],TESTING['Organization/'+str(orgs.RelPersOrg.destinoO)]))
    elif(orgs.tipoRelacionP20.parent==2):
        jg.add((person,PODER['hasEconomicOrganizationParticipant'],TESTING['Organization/'+str(orgs.RelPersOrg.destinoO)]))

# Print the serialized graph
data=jg.serialize(format='xml')
filename = open('applications/PowerMapa/private/pinera.rdf','w')
filename.write(data)
filename.close()
#c=pysesame.connection('http://freerisk.org:8280/openrdf-sesame/')
#c.use_repository('joblistings')
#print c.postdata(data)





