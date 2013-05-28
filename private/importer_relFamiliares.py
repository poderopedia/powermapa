#! /usr/env python
# -*- coding: utf-8 -*-
from types import *
r=None
s=None
h1=None
for line in open('applications/PowerMapa/private/empresarios3.csv','r'):
    lista = line.strip().split(',')
    for row in db(db.persona.alias==lista[0]).select():
        _id= row.id
    if(lista[1]!=""):
	r=None
	r= db(db.persona.alias==lista[1]).select().first()
	if(r==None or r==0):
		r = db.persona.validate_and_insert(			
		       alias=lista[1],
		       countryofResidence=44)
	
	t1 = db.relFamiliar.insert(
			parentesco=2,
			origenP=_id,
			destinoP=r
			)
	print _id,r
    if(lista[2]!=""):
	s=None
	s= db(db.persona.alias==lista[2]).select().first()
	if(s==None):
		s = db.persona.validate_and_insert(			
		       alias=lista[2],
		       countryofResidence=44)
	
	t2 = db.relFamiliar.insert(
			parentesco=2,
			origenP=_id,
			destinoP=s)
    h1==None
    ##hijos
    if(lista[3]!=""):
	hijos=lista[3].strip().split(';')
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
    if(lista[4]!=""):
	tios=lista[4].strip().split(';')
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
    if(lista[5]!=""):
	sobrinos=lista[5].strip().split(';')
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
    if(lista[6]!=""):
	primos=lista[6].strip().split(';')
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
    if(lista[7]!=""):
	abuelos=lista[7].strip().split(';')
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

    if rel1.errors: print line, rel1.errors

db.commit()