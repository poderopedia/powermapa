#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/datosbasicos.csv','r'):
    lista = line.strip().split(',')
    r = db.persona.validate_and_insert(
                       firstName=lista[2],
                       firstLastName=lista[0],
		       otherLastName=lista[1],
		       alias=lista[3],
		       countryofResidence=lista[4])
    if r.errors: print line, r.errors

db.commit()