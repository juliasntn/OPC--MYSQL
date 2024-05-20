import pymysql.cursors
from opcua import Client
from opcua import ua

def insert_into_table(value): 
    try:
        connection = pymysql.connect(
            host='localhost',
            user='USER',
            password='PASS',
            database='DATABASE',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection:
            with connection.cursor() as cursor:
                sql_insert_query = """INSERT INTO video (COLUMN) VALUES (%s)""" 
                cursor.execute(sql_insert_query, (value,)) 
            connection.commit()
            print("Registro inserido com sucesso")

    except pymysql.MySQLError as e:
        print("Erro ao conectar ou inserir dados no MySQL:", e)

class SubHandler(object):
    def _init_(self, node_name):
        self.node_name = node_name

    def datachange_notification(self, node, val, data):
        print(f"Dados alterados em {self.node_name}: {val}")
        insert_into_table(val)

    def event_notification(self, event):
        print("Evento recebido:", event)

# Conectar ao servidor OPC UA
client = Client("opc.tcp://SERVIDOR")
try:
    client.connect()
    print("Conectado ao servidor OPC UA")

    node = client.get_node("NODEID") 
    handler = SubHandler("Nome_do_Nó")
    subscription = client.create_subscription(500, handler)
    handle = subscription.subscribe_data_change(node)

    # Mantém o script rodando
    print("Pressione Ctrl+C para sair")
    while True:
        pass

except Exception as e:
    print("Erro ao conectar ao servidor OPC UA:", e)
finally:
    client.disconnect()
    print("Conexão ao servidor OPC UA foi encerrada")