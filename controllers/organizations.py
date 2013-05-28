__author__ = 'Evolutiva'

def index():

    #Initialize the widget
    add_option = SELECT_OR_ADD_OPTION(form_title=T("Agregar Fuentes"), controller="fuentes", function="add_fuentes", button_text = T("Nueva Fuente"))
    #assign widget to field
    db.Organizacion.documentSource.widget = add_option.widget

    links=[]

    if request.args(0)=='view':
        #response.new_window = URL('visualizacion','caso_perfil',args=[request.args(1),request.args(1)])
        redirect(URL('visualizacion','caso_organizacion',args=[request.args(2),request.args(1)]))

    if auth.user_id:
        links = [dict(header=T('Conexiones'),_class='w2p_trap',
                      body=lambda row: A(IMG(_src=URL('static','plugin_powertable/images/details_open.png'),
                                            _alt=T('Ver Conexiones'),_id='image'+str(row.id)),
                                         #callback=URL('personas','conexiones',args=row.id),, target='t'
                                         _onclick='addConnections(event,'+str(row.id)+')'))]

    query = (db.Organizacion.is_active==True) & (db.Organizacion.tipoOrg!=2)
    fields=(db.Organizacion.id, db.Organizacion.alias,
            db.Organizacion.haslogo, db.Organizacion.hasSocialReason)
    grid = SQLFORM.grid(query, fields = fields, orderby=db.Organizacion.alias,
                        csv=False,formargs={'active':'persona'},links=links)
    return dict(companies_grid=grid)

def organization():
    return dict()

def new():
    response.view = 'personas/new.html'
    #Initialize the widget
    add_option = SELECT_OR_ADD_OPTION(form_title=T("Agregar Fuentes"), controller="fuentes", function="add_fuentes", button_text = T("Nueva Fuente"))
    #assign widget to field
    db.Organizacion.documentSource.widget = add_option.widget

    form=SQLFORM(db.Organizacion)

    if form.process().accepted:
       response.flash = 'Formulario Acceptado'
       redirect(URL('organizaciones','index',vars=dict(keywords='Organizacion.id="'+str(form.vars.id)+'"')))
    elif form.errors:
       response.flash = 'Formulario tiene errores'

    return dict(form=form,title=T('Organizaciones: Datos Básicos'))