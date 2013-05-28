__author__ = 'Evolutiva'

##def OldBrothers(aBrother,bBrother):

aBrother=46
bBrother=59

r=0; sets=set()

aBrotherListO=db((db.relFamiliar.origenP==aBrother) &(db.relFamiliar.parentesco==3)).select(db.relFamiliar.destinoP)
aBrotherListD=db((db.relFamiliar.destinoP==aBrother) &(db.relFamiliar.parentesco==3)).select(db.relFamiliar.origenP)
bBrotherListO=db((db.relFamiliar.origenP==bBrother) &(db.relFamiliar.parentesco==3)).select(db.relFamiliar.destinoP)
bBrotherListD=db((db.relFamiliar.destinoP==bBrother) &(db.relFamiliar.parentesco==3)).select(db.relFamiliar.origenP)
sets=createSet(aBrotherListO,bBrotherListO,'destinoP')

print sets

setsD = createSet(bBrotherListD,bBrotherListD,'origenP')
print setsD
setsfinal = sets | setsD
print setsfinal
relacion = set()
for detalle in setsfinal:
    pivot=detalle
    print pivot
    for destino in relacion:

        result = db(
            ((db.relFamiliar.origenP==pivot) & (db.relFamiliar.destinoP==destino) &(db.relFamiliar.parentesco==3)) |
            ((db.relFamiliar.destinoP==pivot) & (db.relFamiliar.origenP==destino) &(db.relFamiliar.parentesco==3))
        ).select().first()
        ##print result.origenP, result.destinoP
        if(result==None):
            r=db.relFamiliar.validate_and_insert(parentesco=3,origenP=pivot,destinoP=destino)
            ##if r.errors: print origenP, r.errors
            print pivot,destino, r
    relacion.add(pivot)
