#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/tipo_Organizaciones.csv','r'):
    name = line.strip().split(',')
    r = db.tipoOrganizacion.validate_and_insert(
                       name=name)
    if r.errors: print line, r.errors

db.commit()
