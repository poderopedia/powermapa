#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/diputados.csv','r'):
    lista = line.strip().split(',')
    w= db(db.persona.alias==lista[3]).select().first()
    if(w==None):
    	w = db.persona.validate_and_insert(
                       firstName=lista[2],
                       firstLastName=lista[0],
		         otherLastName=lista[1],
		         alias=lista[3],
		         countryofResidence=lista[4])
       ##if w.errors: print line, w.errors

    r=None
    s=None
    h1=None

    _id=w
    if(lista[8]!=""):
	r=None
	r= db(db.persona.alias==lista[8]).select().first()
	if(r==None or r==0):
		r = db.persona.validate_and_insert(			
		       alias=lista[8],
		       countryofResidence=44)
	
	t1 = db.relFamiliar.insert(
			parentesco=2,
			origenP=_id,
			destinoP=r
			)
	print _id,r
    if(lista[9]!=""):
	s=None
	s= db(db.persona.alias==lista[9]).select().first()
	if(s==None):
		s = db.persona.validate_and_insert(			
		       alias=lista[9],
		       countryofResidence=44)
	
	t2 = db.relFamiliar.insert(
			parentesco=2,
			origenP=_id,
			destinoP=s)
    h1==None
    ##hijos
    if(lista[10]!=""):
	hijos=lista[10].strip().split(';')
	for hijo in hijos:
		if(hijo!=""):
			
			h1= db(db.persona.alias==hijo).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=hijo,
					countryofResidence=44)
			print "h1="+str(h1)
			rel1=db.relFamiliar.insert(
				parentesco=1,
				origenP=_id,
				destinoP=h1
   				)
    h1=None
    ##tios
    if(lista[11]!=""):
	tios=lista[11].strip().split(';')
	for tio in tios:
		if(tio!=""):
			h1= db(db.persona.alias==tio).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=tio,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=4,
				origenP=_id,
				destinoP=h1
				)
    h1=None
    ##sobrinos
    if(lista[12]!=""):
	sobrinos=lista[12].strip().split(';')
	for sobrino in sobrinos:
		if(sobrino!=""):
			h1= db(db.persona.alias==sobrino).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=sobrino,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=5,
				origenP=_id,
				destinoP=h1
				)
    h1=None
    ##primos
    if(lista[13]!=""):
	primos=lista[13].strip().split(';')
	for primo in primos:
		if(primo!=""):
			h1= db(db.persona.alias==primo).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=primo,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=6,
				origenP=_id,
				destinoP=h1
				)
    h1=None
    ##abuelos
    if(lista[14]!=""):
	abuelos=lista[14].strip().split(';')
	for abuelo in abuelos:
		if(abuelo!=""):
			h1= db(db.persona.alias==abuelo).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=abuelo,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=8,
				origenP=_id,
				destinoP=h1
				)
    h1=None
    ##hermanos
    if(lista[15]!=""):
	hermanos=lista[15].strip().split(';')
	for hermano in hermanos:
		if(hermano!=""):
			h1= db(db.persona.alias==hermano).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=hermano,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=3,
				origenP=_id,
				destinoP=h1
				)
    h1=None
    ##nietos
    if(lista[16]!=""):
	hermanos=lista[16].strip().split(';')
	for hermano in hermanos:
		if(hermano!=""):
			h1= db(db.persona.alias==hermano).select().first()
			if(h1==None):
				h1 = db.persona.validate_and_insert(			
					alias=hermano,
					countryofResidence=44)
		
			rel1=db.relFamiliar.insert(
				parentesco=7,
				origenP=_id,
				destinoP=h1
				)


    ##if rel1.errors: print line, rel1.errors

db.commit()