import os

from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField, DateField, \
    DecimalField, FloatField

# nome do arquivo do banco de dados
# Connect to a SQLite local database.
# database = SqliteDatabase('sucellus.db')
# SQLite database using WAL journal mode and 64MB cache.
import populate_db

database = SqliteDatabase('hostel.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})
class ModelBase(Model):  # classe modelo
    """
       Classe que cria a Entidade modelo a ser usada no projeto através da biblioteca peewee.
       Best practice: define a base model class that points at the database object you wish to use,
       and then all your models will extend it:
    """
    class Meta:
        """
           Meta classe que ao ser herdada define o metodo de conexao atravez do objeto database
        """
        database = database


class Address(ModelBase):
    """
       Classe de Endereco para mapeamento
    """
    address = CharField()
    zipcode = CharField()
    city = CharField()
    state = CharField()
    country = CharField(default = 'Brazil')


class Customer(ModelBase):
    """
       Classe de Customer para mapeamento
    """
    title = CharField()
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    email = CharField(unique=True)
    address = ForeignKeyField(Address)
    ativo = CharField(null=False, default = 'ativo')


class Reservation(ModelBase):
    """
        Classe de Reservation para mapeamento
    """
    reservation_code = CharField(null=True, unique=True)
    number_of_guests = IntegerField()
    reservation_date = DateField()
    checkin_date = DateField()
    checkout_date = DateField()
    ativo = CharField(null=False, default = 'ativo')
    customer = ForeignKeyField(Customer)

class Room(ModelBase):
    """
        Classe de Room para mapeamento
    """
    number = IntegerField(unique=True)
    dimension = FloatField()
    ativo = CharField(null=False, default = 'ativo')


class Reservation_Room(ModelBase):
    '''
        Classe Reservation_Room para mapeamento
        esta classe serve para fazer a relacao entre reservation tem n quartos
    '''
    reservation_code = ForeignKeyField(Reservation)
    room_id = ForeignKeyField(Room)


def create_tables():
    """
    Função que cria o banco de dados baseado nas classes
    """
    database.connect()
    database.create_tables([Address, Customer, Reservation, Room, Reservation_Room])

def todos_enderecos():
    """
        Function for serach all Address
    """
    data = Address.select()
    return data
def endereco_hostel():
    data = Address.select().where(Address.id == 1)
    return data
#########################################################################################
####        Inicio DO CODIGO PARA MANIPULAR Customers                   #################
#########################################################################################
def todos_clientes_ativos()->[Customer]:
    """
        Function for serach all actived Customers
    """
    ativo = 'ativo'
    data = Customer.select().where(Customer.ativo == ativo).join(Address)
    return data

def todos_clientes_inativos()->[Customer]:
    """
        Function for search all inactive Customers
    """
    ativo = 'inativo'
    data = Customer.select().join(Address).where(Customer.ativo == ativo)
    return data

# Utiliza uma transacao atomica
@database.atomic()
def inserir_cliente_endereco(request)->Customer:
    """
        Function for insert a new Customer(obj) in table Customer
        and a Adress for this Customer
    # Utiliza uma transacao atomica
    http://docs.peewee-orm.com/en/3.1.0/peewee/transactions.html#decorator
    """
    ativo = 'ativo'
    # Address
    address = Address()
    address.address = request.form['address']
    address.zipcode = request.form['zipcode']
    address.city = request.form['city']
    address.state = request.form['state']
    address.country = request.form['country']
    address.save()
    # Customer
    customer = Customer()
    customer.title = request.form['title']
    customer.first_name = request.form['first_name']
    customer.last_name = request.form['last_name']
    customer.birthday = request.form['birthday']
    customer.email = request.form['email']
    customer.address = address.id
    customer.ativo = ativo
    customer.save()
    return customer

# Utiliza uma transacao atomica
@database.atomic()
def atualizar_cliente_endereco(id:int, request)->Customer:
    """
        Function for update a existence Customer
    # Utiliza uma transacao atomica
    http://docs.peewee-orm.com/en/3.1.0/peewee/transactions.html#decorator
    """

    # Customer
    customer = busca_id_cliente(id)
    if customer:
        customer.title = request.form['title']
        customer.first_name = request.form['first_name']
        customer.last_name = request.form['last_name']
        customer.birthday = request.form['birthday']
        customer.email = request.form['email']
        # Address
        address = busca_id_endereco(customer.address)
        address.address = request.form['address']
        address.zipcode = request.form['zipcode']
        address.city = request.form['city']
        address.state = request.form['state']
        address.country = request.form['country']
        # Save
        address.save()
        customer.save()
    return customer

def busca_id_endereco(id):
    """
    Verifica
    """
    id = id
    data = Address.select().where(Address.id == id)
    return data[0]

def busca_id_cliente(id):
    """
    Verifica
    """
    id = id
    data = Customer.select().where(Customer.id == id).join(Address)
    return data[0]


# Ativar Remessa
def ativar_cliente(id):
    """
    Vito
    """
    data = busca_id_cliente(id)
    if data:
        ativo = 'ativo'
        data.ativo = ativo
        data.save()
        return data


# Desativar Remessa
def desativar_cliente(id):
    """
    Vito
    """
    data = busca_id_cliente(id)
    if data:
        ativo = 'inativo'
        data.ativo = ativo
        data.save()
        return data
#########################################################################################
####        Inicio DO CODIGO PARA MANIPULAR ROOMS                       #################
#########################################################################################
def todos_room_ativos():
    """
    Vito
    """
    ativo = 'ativo'
    data = Room.select().where(Room.ativo == ativo)
    return data


def todos_room_inativos():
    """
    Vito
    """
    ativo = 'inativo'
    data = Room.select().where(Room.ativo == ativo)
    return data


@database.atomic()
def inserir_room(request):
    """
    Vito
    # Utiliza uma transacao atomica
    http://docs.peewee-orm.com/en/3.1.0/peewee/transactions.html#decorator
    """
    ativo = 'ativo'
    # Room
    room = Room()
    room.number = request.form['number']
    room.dimension = request.form['dimension']
    room.ativo = ativo
    room.save()
    return room


def busca_id_room(id:int)->Room:
    id = id
    data = Room.select().where(Room.id == id)
    return data[0]


def ativar_room(id:int)->Room:
    """
    Vito
    """
    data = busca_id_room(id)
    if data:
        ativo = 'ativo'
        data.ativo = ativo
        data.save()
        return data


def desativar_room(id:int)->Room:
    """
    Vito
    """
    data = busca_id_room(id)
    if data:
        ativo = 'inativo'
        data.ativo = ativo
        data.save()
        return data


@database.atomic()
def atualizar_room(id, request):
    room = busca_id_room(id)
    if room:
        room.number = request.form['number']
        room.dimension = request.form['dimension']
        room.save()
    return room
#########################################################################################
####        Inicio DO CODIGO PARA MANIPULAR Reservations                #################
#########################################################################################
def todas_reservas_ativas():
    """
    Vito
    """
    ativo = 'ativo'
    data = Reservation.select().where(Reservation.ativo == ativo).join(Customer)
    return data

def todas_reservas_inativas():
    """
    Vito
    """
    ativo = 'inativo'
    data = Reservation.select().where(Reservation.ativo == ativo)
    return data

def busca_id_reservation(id:int)->Reservation:
    id = id
    data = Reservation.select().where(Reservation.id == id)
    return data[0]


def busca_reservation_room(id_reservation:int):
    data = Reservation_Room.select().where(Reservation_Room.reservation_code == id_reservation)
    return data

@database.atomic()
def remover_reservation_rooms(id):
    reservation_rooms = busca_reservation_room(id)
    for i in reservation_rooms:
        Reservation_Room.delete_instance(i)

@database.atomic()
def atualizar_reservation(id:int, request)->Reservation:
    reservation = busca_id_reservation(id)
    if reservation:
        remover_reservation_rooms(id)
        listRoom = listRooms(request.form['room_id'])
        reservation.number_of_guests = request.form['number_of_guests']
        reservation.reservation_date = request.form['reservation_date']
        reservation.checkin_date = request.form['checkin_date']
        reservation.checkout_date = request.form['checkout_date']
        reservation.customer = request.form['customer_id']
        reservation.save()
        for i in listRoom:
            reservation_room = Reservation_Room()
            reservation_room.reservation_code = reservation.id
            reservation_room.room_id = i
            reservation_room.save()
    return reservation


def listRooms(roomString:str)->list:
    list = []
    roomString = roomString.split(" ")
    for i in roomString:
        list.append(int(i))
    return list


@database.atomic()
def inserir_reservation(request):
    """
    Vito
    # Utiliza uma transacao atomica
    http://docs.peewee-orm.com/en/3.1.0/peewee/transactions.html#decorator
    """
    ativo = 'ativo'
    # Room
    customer_id = int(request.form['customer_id'])
    listRoom = listRooms(request.form['room_id'])
    if busca_id_cliente(customer_id) and len(listRoom) > 0:
        reservation = Reservation()
        reservation.number_of_guests = request.form['number_of_guests']
        reservation.checkin_date = request.form['checkin_date']
        reservation.checkout_date = request.form['checkout_date']
        reservation.reservation_date = request.form['reservation_date']
        reservation.ativo = ativo
        reservation.customer = request.form['customer_id']
        reservation.save()
        # atribui reservation_code como igual ao id
        reservation.reservation_code = reservation.id
        reservation.save()
        #cria uma relacao entre reserva e room em uma tabela
        for i in listRoom:
            reservation_room = Reservation_Room()
            reservation_room.reservation_code = reservation.id
            reservation_room.room_id = i
            reservation_room.save()
        return reservation

def desativar_reservation(id:int)->Reservation:
    """
    Vito
    """
    data = busca_id_reservation(id)
    if data:
        ativo = 'inativo'
        data.ativo = ativo
        data.save()
        return data


def ativar_reservation(id:int)->Reservation:
    """
    Vito
    """
    data = busca_id_reservation(id)
    if data:
        ativo = 'ativo'
        data.ativo = ativo
        data.save()
        return data

def delete_banco_dados():
    path = os.getcwd()
    diretorio = os.listdir(path)
    for file in diretorio:
        if file == "hostel.db":
            os.remove(file)

def existe_banco_dados() -> bool:
    """verifica se existe um arquivo de banco de dados com nome ride_dote.db"""
    path = os.getcwd()
    diretorio = os.listdir(path)
    for file in diretorio:
        if file == "hostel.db":
            return True
    return False

if __name__ == '__main__':
    # Quando esse arquivo for executado como main será criada as tabelas de banco de dados
    create_tables()

    if existe_banco_dados():
        delete_banco_dados()
    create_tables()
    populate_db.criar_informacoes()