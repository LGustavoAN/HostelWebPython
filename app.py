
from flask import Flask, render_template, url_for, request, flash, redirect
import db

app = Flask(_name_)
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