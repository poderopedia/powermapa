#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/dtos.txt','r'):
    name,nameInverso = line.strip().split(';')
    r = db.tipoParentesco.validate_and_insert(
                       name=nameInverso,
                       nameInverso=nameInverso)
    if r.errors: print line, r.errors

db.commit()
