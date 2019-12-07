from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField, DateField, \
    DecimalField, FloatField

# nome do arquivo do banco de dados
# Connect to a SQLite local database.
# database = SqliteDatabase('sucellus.db')
# SQLite database using WAL journal mode and 64MB cache.
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