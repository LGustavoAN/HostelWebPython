from flask import Flask, render_template, url_for, request, flash, redirect
import db

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
