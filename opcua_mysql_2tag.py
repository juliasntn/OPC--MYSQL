import pymysql.cursors
from opcua import Client
from opcua import ua
import time

# Função para inserir dados no banco de dados MySQL
def insert_into_table(node1_value, node2_value):
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
                sql_insert_query = """INSERT INTO sensores (COLUMN, COLUMN) VALUES (%s, %s)"""
                cursor.execute(sql_insert_query, (node1_value, node2_value))
            connection.commit()
            print("Registro inserido com sucesso")

    except pymysql.MySQLError as e:
        print("Erro ao conectar ou inserir dados no MySQL:", e)


node1_value = None
node2_value = None

# Classe para monitorar alterações no OPC UA
class SubHandler(object):
    def _init_(self, node_name):
        self.node_name = node_name

    def datachange_notification(self, node, val, data):
        global node1_value, node2_value
        print(f"Dados alterados em {self.node_name}: {val}")
        if self.node_name == "Node1":
            node1_value = val
        elif self.node_name == "Node2":
            node2_value = val

        
        if node1_value is not None and node2_value is not None:
            insert_into_table(node1_value, node2_value)
            
            node1_value, node2_value = None, None

    def event_notification(self, event):
        print("Evento recebido:", event)


client = Client("SERVIDOROPC")
try:
    client.connect()
    print("Conectado ao servidor OPC UA")

    
    node1 = client.get_node("NODEID")
    node2 = client.get_node("NODEID")

    
    handler1 = SubHandler("Node1")
    handler2 = SubHandler("Node2")

    
    subscription = client.create_subscription(500, handler1)
    handle1 = subscription.subscribe_data_change(node1)
    
    subscription2 = client.create_subscription(500, handler2)
    handle2 = subscription2.subscribe_data_change(node2)

    # Mantém o script rodando
    print("Pressione Ctrl+C para sair")
    while True:
        time.sleep(1)

except Exception as e:
    print("Erro ao conectar ao servidor OPC UA:", e)
finally:
    client.disconnect()
    print("Conexão ao servidor OPC UA foi encerrada")