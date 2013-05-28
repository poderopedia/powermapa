#! /usr/env python
# -*- coding: utf-8 -*-

for line in open('applications/PowerMapa/private/sectores.csv','r'):
    parent, name = line.strip().split(',')
    r = db.sector.validate_and_insert(
                       parent=parent,
                       name=name)
    if r.errors: print line, r.errors

db.commit()
