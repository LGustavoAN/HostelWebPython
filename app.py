from flask import Flask, render_template, url_for, request, flash, redirect
import db
import populate_db

app = Flask(__name__)
app.secret_key = """Kazakhstan greatest country in the world
All other countries are run by little girls
Kazakhstan number one exporter of potassium"""


@app.route('/')
def index():
    address = db.todos_enderecos()
    section_location = 'Hostel'
    address = db.endereco_hostel()
    dados = {}
    dados['titulo'] = ''
    dados['section_location'] = ''
    dados['url_current'] = ''
    dados['url_ativo'] = '' #'url_for('customer_active')'
    dados['url_inativo'] = ''#url_for('customer_inactive')
    dados['url_criar'] = ''#url_for('customer_make')
    dados['url_editar'] = '' # 'customer_edit'
    dados['url_ativar'] = '' #'customer_enable'
    dados['url_desativar'] = '' #'customer_disable'
    dados['url_form'] = '' #url_for('customer_save', id=busca.id)
    return render_template('index.html',dados = dados,titulo='HostelWeb', address=address, section_location=section_location)

##########################################
@app.route('/customer/active')
def customer_active():
    tabela = db.todos_clientes_ativos()
    dados = {}
    dados['titulo'] = 'Clientes'
    dados['section_location'] = 'Customer'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('customer_active')
    dados['url_inativo'] = url_for('customer_inactive')
    dados['url_criar'] = url_for('customer_make')
    dados['url_editar'] = 'customer_edit'
    dados['url_ativar'] = 'customer_enable'
    dados['url_desativar'] = 'customer_disable'
    dados['url_form'] = ''
    return render_template('clientes.html', dados=dados, tabela=tabela)

@app.route('/customer/enable/id/<int:id>')
def customer_enable(id):
    """
       Vito
    """
    id = int(id)
    data = db.ativar_cliente(id)
    if data:
        flash(f'cliente:{data.first_name} {data.last_name}, ativado com sucesso!')
    return redirect(url_for('customer_inactive'))


@app.route('/customer/inactive')
def customer_inactive():
    tabela = db.todos_clientes_inativos()
    dados = {}
    dados['titulo'] = 'Clientes'
    dados['section_location'] = 'Customer'
    dados['url_current'] = 'inativo'
    dados['url_ativo'] = url_for('customer_active')
    dados['url_inativo'] = url_for('customer_inactive')
    dados['url_criar'] = url_for('customer_make')
    dados['url_editar'] = 'customer_edit'
    dados['url_ativar'] = 'customer_enable'
    dados['url_desativar'] = 'customer_disable'
    dados['url_form'] = ''
    return render_template('clientes.html', dados=dados, tabela=tabela)

@app.route('/customer/disable/id/<int:id>')
def customer_disable(id):
    """
       Vito
    """
    id = int(id)
    data = db.desativar_cliente(id)
    if data:
        flash(f'cliente:{data.first_name} {data.last_name}, desativado com sucesso!')
    return redirect(url_for('customer_active'))

@app.route('/customer/make')
def customer_make():
    dados = {}
    dados['titulo'] = 'Clientes'
    dados['section_location'] = 'Customer'
    dados['url_current'] = 'criar'
    dados['url_ativo'] = url_for('customer_active')
    dados['url_inativo'] = url_for('customer_inactive')
    dados['url_criar'] = url_for('customer_make')
    dados['url_editar'] = 'customer_edit'
    dados['url_ativar'] = 'customer_enable'
    dados['url_desativar'] = 'customer_disable'
    dados['url_form'] = url_for('customer_insert')
    return render_template('clientes_form.html', dados=dados)

@app.route('/customer/edit/id/<int:id>')
def customer_edit(id):
    id = int(id)
    busca = db.busca_id_cliente(id)
    dados = {}
    dados['titulo'] = 'Clientes'
    dados['section_location'] = 'Customer'
    dados['url_current'] = 'criar'
    dados['url_ativo'] = url_for('customer_active')
    dados['url_inativo'] = url_for('customer_inactive')
    dados['url_criar'] = url_for('customer_make')
    dados['url_editar'] = 'customer_edit'
    dados['url_ativar'] = 'customer_enable'
    dados['url_desativar'] = 'customer_disable'
    dados['url_form'] = url_for('customer_save', id=busca.id)
    return render_template('clientes_form.html', dados=dados, busca=busca)

@app.route('/customer/insert', methods=['POST'])
def customer_insert():
    """
       Vito
    """
    if len(request.form['first_name']) >= 3:
        data = db.inserir_cliente_endereco(request)
        if data:
            flash(f'{data.first_name} {data.last_name}, criado com sucesso!')
        return redirect(url_for('customer_active'))
    else:
        flash(f'Tamanho minimo de First Name 3 letras')
        return redirect(url_for('customer_make'))

@app.route('/customer/save/id/<int:id>', methods=['POST'])
def customer_save(id):
    """
       Vito
    """
    id = int(id)
    data = db.atualizar_cliente_endereco(id, request)
    if data:
        flash(f'{data.first_name} {data.last_name}, editado com sucesso!')
    return redirect(url_for('customer_active'))

##########################################
@app.route('/rooms/active')
def room_active():
    rooms = db.todos_room_ativos()
    dados = {}
    dados['titulo'] = 'Quarto'
    dados['section_location'] = 'Rooms'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('room_active')
    dados['url_inativo'] = url_for('room_inactive')
    dados['url_criar'] = url_for('room_make')
    dados['url_editar'] = 'room_edit'
    dados['url_ativar'] = 'room_enable'
    dados['url_desativar'] = 'room_disable'
    dados['url_form'] = '' #url_for('room_insert')
    return render_template('rooms.html', dados=dados, titulo='Rooms', rooms=rooms)

@app.route('/rooms/inactive')
def room_inactive():
    rooms = db.todos_room_inativos()
    dados = {}
    dados['titulo'] = 'Quarto'
    dados['section_location'] = 'Rooms'
    dados['url_current'] = 'inativo'
    dados['url_ativo'] = url_for('room_active')
    dados['url_inativo'] = url_for('room_inactive')
    dados['url_criar'] = url_for('room_make')
    dados['url_editar'] = 'room_edit'
    dados['url_ativar'] = 'room_enable'
    dados['url_desativar'] = 'room_disable'
    dados['url_form'] = '' #url_for('room_insert')
    return render_template('rooms.html', dados = dados, titulo='Rooms', rooms=rooms)

@app.route('/rooms/make')
def room_make():
    section_location = 'Make Room'
    dados = {}
    dados['titulo'] = 'Quarto'
    dados['section_location'] = 'Rooms'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('room_active')
    dados['url_inativo'] = url_for('room_inactive')
    dados['url_criar'] = url_for('room_make')
    dados['url_editar'] = 'room_edit'
    dados['url_ativar'] = 'room_enable'
    dados['url_desativar'] = 'room_disable'
    dados['url_form'] = url_for('room_insert')
    return render_template('room_form.html', dados=dados, titulo='Rooms', section_location=section_location)

@app.route('/room/insert', methods=['POST'])
def room_insert():
    """
       Vito
    """
    data = db.inserir_room(request)
    if data:
        flash(f'{data.number} {data.dimension},room criado com sucesso!')
    return redirect(url_for('room_active'))

@app.route('/room/enable/id/<int:id>')
def room_enable(id):
    """
       Vito
    """
    id = int(id)
    data = db.ativar_room(id)
    if data:
        flash(f'Room:{data.number} {data.dimension},room ativado com sucesso!')
    return redirect(url_for('room_inactive'))

@app.route('/room/disable/id/<int:id>')
def room_disable(id):
    """
       Vito
    """
    id = int(id)
    data = db.desativar_room(id)
    if data:
        flash(f'Room:{data.number} {data.dimension}, desativado com sucesso!')
    return redirect(url_for('room_active'))

@app.route('/room/edit/id/<int:id>')
def room_edit(id):
    id = int(id)
    busca = db.busca_id_room(id)
    dados = {}
    dados['titulo'] = 'Quarto'
    dados['section_location'] = 'Rooms'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('room_active')
    dados['url_inativo'] = url_for('room_inactive')
    dados['url_criar'] = url_for('room_make')
    dados['url_editar'] = 'room_edit'
    dados['url_ativar'] = 'room_enable'
    dados['url_desativar'] = 'room_disable'
    dados['url_form'] = url_for('room_save', id=busca.id)
    return render_template('room_form.html', dados=dados, busca=busca)

@app.route('/room/save/id/<int:id>', methods=['POST'])
def room_save(id):
    """
       Vito
    """
    id = int(id)
    data = db.atualizar_room(id, request)
    if data:
        flash(f'Room: {data.number} {data.dimension}, editado com sucesso!')
    return redirect(url_for('room_active'))

########################################################################
########################################################################

@app.route('/reservation/active')
def reservation_active():
    reservas = db.todas_reservas_ativas()
    dados = {}
    dados['titulo'] = 'Reservas'
    dados['section_location'] = 'Reservation'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('reservation_active')
    dados['url_inativo'] = url_for('reservation_inactive')
    dados['url_criar'] = url_for('reservation_make')
    dados['url_editar'] = 'reservation_edit'
    dados['url_ativar'] = 'reservation_enable'
    dados['url_desativar'] = 'reservation_disable'
    dados['url_form'] = '' #url_for('reservation_save', id=busca.id)
    return render_template('reservation.html',dados = dados, reservas=reservas)

@app.route('/reservation/inactive')
def reservation_inactive():
    reservas = db.todas_reservas_inativas()
    dados = {}
    dados['titulo'] = 'Reservas'
    dados['section_location'] = 'Reservation'
    dados['url_current'] = 'inativo'
    dados['url_ativo'] = url_for('reservation_active')
    dados['url_inativo'] = url_for('reservation_inactive')
    dados['url_criar'] = url_for('reservation_make')
    dados['url_editar'] = 'reservation_edit'
    dados['url_ativar'] = 'reservation_enable'
    dados['url_desativar'] = 'reservation_disable'
    dados['url_form'] = '' #url_for('reservation_save', id=busca.id)
    return render_template('reservation.html',dados = dados, reservas=reservas)

@app.route('/reservation/make')
def reservation_make():
    section_location = 'Make Reserv'
    rooms = db.todos_room_ativos()
    customers = db.todos_clientes_ativos()
    dados = {}
    dados['titulo'] = 'Reservas'
    dados['section_location'] = 'Reservation'
    dados['url_current'] = 'inativo'
    dados['url_ativo'] = url_for('reservation_active')
    dados['url_inativo'] = url_for('reservation_inactive')
    dados['url_criar'] = url_for('reservation_make')
    dados['url_editar'] = 'reservation_edit'
    dados['url_ativar'] = 'reservation_disable'
    dados['url_desativar'] = ''  # 'reservation_disable'
    dados['url_form'] = url_for('reservation_insert')
    return render_template('reservation_form.html', dados=dados
                           , section_location=section_location, rooms=rooms, customers=customers)

@app.route('/reservation/insert', methods=['POST'])
def reservation_insert():
    """
           Vito
    """
    data = db.inserir_reservation(request)
    if data:
        flash(f'Reserva: {data.id},reserva criada com sucesso!')
    return redirect(url_for('reservation_active'))

@app.route('/room/disenable/id/<int:id>')
def reservation_disable(id):
    """
       Vito
    """
    id = int(id)
    data = db.desativar_reservation(id)
    if data:
        flash(f'Reserve: {data.id},room ativado com sucesso!')
    return redirect(url_for('reservation_active'))

@app.route('/room/enable/id/<int:id>')
def reservation_enable(id):
    """
       Vito
    """
    id = int(id)
    data = db.ativar_reservation(id)
    if data:
        flash(f'Reserve: {data.id},room ativado com sucesso!')
    return redirect(url_for('reservation_inactive'))

@app.route('/reservation/edit/id/<int:id>')
def reservation_edit(id):
    def reservation_room_str(reservation_rooms)->list(db.Room):
        list = []
        string = ""
        for i in range(len(reservation_rooms)):
            list.append(reservation_rooms[i].room_id)

            string += reservation_rooms[i].room_id.__str__() + " "
        print(string)
        return string
    id = int(id)
    busca = db.busca_id_reservation(id)
    rooms = db.todos_room_ativos()
    customers = db.todos_clientes_ativos()
    rooms_id = db.busca_reservation_room(id)
    rooms_id = reservation_room_str(rooms_id)
    dados = {}
    dados['titulo'] = 'Reservation'
    dados['section_location'] = 'Reservation'
    dados['url_current'] = 'ativo'
    dados['url_ativo'] = url_for('reservation_active')
    dados['url_inativo'] = url_for('reservation_inactive')
    dados['url_criar'] = url_for('reservation_make')
    dados['url_editar'] = 'reservation_edit'
    dados['url_ativar'] = 'reservation_enable'
    dados['url_desativar'] = 'reservation_disable'
    dados['url_form'] = url_for('reservation_save', id=busca.id)
    return render_template('reservation_form.html', dados=dados, busca=busca, rooms=rooms,
                           customers=customers, rooms_id=rooms_id)

@app.route('/reservation/save/id/<int:id>', methods=['POST'])
def reservation_save(id):
    """
       Vito
    """
    id = int(id)
    data = db.atualizar_reservation(id, request)
    if data:
        flash(f'Reservation: {data.reservation_code}, {data.customer}, editado com sucesso!')
    return redirect(url_for('reservation_active'))
if __name__ == '__main__':
    if not(db.existe_banco_dados()):
        db.create_tables()
        populate_db.criar_informacoes()
    app.run(host='0.0.0.0', port=80, debug=True)
