#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/relacionesP2P_1.csv','r'):
    parent,name = line.strip().split(';')
    r = db.tipoRelacionP2P.validate_and_insert(
                       parent=parent,
                       name=name)
    if r.errors: print line, r.errors

db.commit()
