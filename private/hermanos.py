__author__ = 'Evolutiva'

count = db.relFamiliar.origenP.count()
hermanos=db(db.relFamiliar.parentesco==3).select(db.relFamiliar.origenP, count, groupby = db.relFamiliar.origenP)
for hermano in hermanos:
    ##print "Maluenda" + str(hermano)
    if (hermano[count]>1):
        origenP=hermano.relFamiliar.origenP
        listaHermanos=db((db.relFamiliar.origenP==origenP) &(db.relFamiliar.parentesco==3)).select(db.relFamiliar.destinoP)
        relacion= set()
        for detalle in listaHermanos:
            pivot=detalle.destinoP
            print "pivot="+str(pivot)
            for destino in relacion:
                print destino
                result = db(
                    ((db.relFamiliar.origenP==pivot) & (db.relFamiliar==destino) &(db.relFamiliar.parentesco==3)) |
                    ((db.relFamiliar.destinoP==pivot) & (db.relFamiliar.origenP==destino) &(db.relFamiliar.parentesco==3))
                ).select().first()
                if(result==None):
                    r=db.relFamiliar.validate_and_insert(parentesco=3,origenP=pivot,destinoP=destino)
                    if r.errors: print origenP, r.errors
            relacion.add(pivot)

db.commit()
