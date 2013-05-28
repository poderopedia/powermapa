#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/RelacionesPersona2Org.csv','r'):
    print line;
    padre,relacion = line.strip().split(',')
    r = db.tipoRelacionP20.validate_and_insert(
                       parent=padre,
                       relationship=relacion)
    if r.errors: print line, r.errors

db.commit()
