#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/SenSociedades.csv','r'):
    linea = line.strip().split(',')
    if(linea[0]!=None):
	senId=db(db.persona.alias==linea[0]).select().first()
	if(senId==None):
		senId = db.persona.validate_and_insert(			
		       alias=linea[0],
		       countryofResidence=44)
	sociedades=linea[1].strip().split(';')
	for sociedad in sociedades:
		if(sociedad!=""):
			sociedad=sociedad.strip()
			h1= db(db.Organizacion.alias==sociedad).select().first()
			if(h1==None):
				h1 = db.Organizacion.validate_and_insert(
					name=sociedad,
					tipoOrg=12,
					alias=sociedad,
					countryOfResidence=44)
			print "h1="+str(h1)
			rel1=db.RelPersOrg.insert(
				specificRelation=11,
				origenP=senId,
				destinoO=h1
   				)

    ##if r.errors: print line, r.errors

db.commit()
