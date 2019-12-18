import db


def inserir_enderecos(rows):
    """
       Vito
    """
    db.Address.insert_many(rows).execute()


def inserir_clientes(rows):
    """
       Vito
    """
    db.Customer.insert_many(rows).execute()

def inserir_reservas(rows):
    """

    :param rows:
    :return:
    """
    db.Reservation.insert_many(rows).execute()

def inserir_rooms(rows):
    """
    :param rows:
    :return:
    """
    db.Room.insert_many(rows).execute()

def inserir_reservas_rooms(rows):
    db.Reservation_Room.insert_many(rows).execute()
ENDERECOS = [
    {'id': 1, 'address': 'Rua Gabriel Monteiro da Silva', 'zipcode': '37130-001', 'city': 'Alfenas',
     'state': 'Minas Gerais', 'country': 'Brasil'},
    {'id': 2, 'address': 'Rua 7 de setembro', 'zipcode': '13760-000', 'city': 'Tapiratiba', 'state': 'São Paulo',
     'country': 'Brasil'},
    {'id': 3, 'address': 'Rua 8 de setembro', 'zipcode': '13760-000', 'city': 'Tapiratiba', 'state': 'São Paulo',
     'country': 'Brasil'},
    {'id': 4, 'address': 'Rua 9 de setembro', 'zipcode': '13760-000', 'city': 'Tapiratiba', 'state': 'São Paulo',
     'country': 'Brasil'},
    {'id': 5, 'address': 'Rua 10 de setembro', 'zipcode': '13760-000', 'city': 'Tapiratiba', 'state': 'São Paulo',
     'country': 'Brasil'}, ]

CLIENTES = [
    {'id': 1, 'title': 'Mr', 'first_name': 'Gordon', 'last_name': 'Freeman',
     'birthday': '2018-09-10', 'email': 'half@life.com', 'address': 2},
    {'id': 2, 'title': 'Ms', 'first_name': 'Pepa', 'last_name': 'Pig',
     'birthday': '2018-09-10', 'email': 'half2@life.com', 'address': 3},
    {'id': 3, 'title': 'Mr', 'first_name': 'Jhon', 'last_name': 'Snow',
     'birthday': '2018-09-10', 'email': 'half23@life.com', 'address': 4},
    {'id': 4, 'title': 'Mr', 'first_name': 'Tyron', 'last_name': 'Lannister',
     'birthday': '2018-09-10', 'email': 'half424@life.com', 'address': 5} ]

RESERVAS =  [
    {'id': 1, 'reservation_code': "1", 'number_of_guests': 1, 'reservation_date': '2018-05-10'
        , 'checkin_date': '2018-09-10', 'checkout_date': '2018-09-15', 'customer_id': 1},
    {'id': 2, 'reservation_code': "2", 'number_of_guests': 3, 'reservation_date': '2019-09-10'
        , 'checkin_date': '2018-09-10', 'checkout_date': '2018-09-15', 'customer_id' : 2},
    {'id': 3, 'reservation_code': "3", 'number_of_guests': 2, 'reservation_date': '2019-09-10'
        , 'checkin_date': '2018-09-10', 'checkout_date': '2018-09-15', 'customer_id' : 3},
    {'id': 4, 'reservation_code': "4", 'number_of_guests': 2, 'reservation_date': '2018-09-10'
        , 'checkin_date': '2018-09-10', 'checkout_date': '2018-09-15', 'customer_id' : 1} ]

RESERVA_ROOM = [{'reservation_code': 1, 'room_id': 1}, {'reservation_code': 2, 'room_id': 2},
                {'reservation_code': 3, 'room_id': 3}, {'reservation_code': 4, 'room_id': 4}]
ROOMS = [
    {'id': 1, 'number': 1, 'dimension': 13.5},
    {'id': 2, 'number': 2, 'dimension': 12.5},
    {'id': 3, 'number': 3, 'dimension': 12.5},
    {'id': 4, 'number': 4, 'dimension': 25 } ]

def criar_informacoes():
    inserir_enderecos(ENDERECOS)
    inserir_clientes(CLIENTES)
    inserir_rooms(ROOMS)
    inserir_reservas(RESERVAS)
    inserir_reservas_rooms(RESERVA_ROOM)
