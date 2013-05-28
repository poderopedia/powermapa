#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/iso-country-codes.csv','r'):
    linea = line.strip().split(',')
    print linea
    r = db.country.validate_and_insert(
                       name=linea[0],
                       iso2=linea[1],
		       iso3=linea[2],
		       iso_id=linea[3])
    if r.errors: print line, r.errors

db.commit()
