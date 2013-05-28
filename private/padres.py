__author__ = 'Evolutiva'

count = db.relFamiliar.origenP.count()
hijos=db(db.relFamiliar.parentesco==1).select(db.relFamiliar.origenP, count, groupby = db.relFamiliar.origenP)
for hijo in hijos:
    ##print "Maluenda" + str(hermano)
    if (hijo[count]>1):
        origenP=hijo.relFamiliar.origenP
        listaHijos=db((db.relFamiliar.origenP==origenP) &(db.relFamiliar.parentesco==1)).select(db.relFamiliar.destinoP)
        relacion= set()
        for detalle in listaHijos:
            pivot=detalle.destinoP
            print "pivot="+str(pivot)
            for destino in relacion:
                print destino
                ##check if are brothers
                result = db(
                    ((db.relFamiliar.origenP==pivot) & (db.relFamiliar.destinoP==destino) &(db.relFamiliar.parentesco==3)) |
                    ((db.relFamiliar.destinoP==pivot) & (db.relFamiliar.origenP==destino) &(db.relFamiliar.parentesco==3))
                ).select().first()
                print str(result)
                if (result==None):
                    print pivot,destino
                    r=db.relFamiliar.validate_and_insert(parentesco=3,origenP=pivot,destinoP=destino)
                    if r.errors: print origenP, r.errors
            relacion.add(pivot)

db.commit()
