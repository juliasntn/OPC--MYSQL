import pymysql.cursors
import time
import random

def insert_into_table(value): 
    try:
        connection = pymysql.connect(
            host='172.28.208.1',
            user='root',
            password='root',
            database='teste',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection:
            with connection.cursor() as cursor:
                sql_insert_query = """INSERT INTO video (NUM) VALUES (%s)""" 
                cursor.execute(sql_insert_query, (value,)) 
            connection.commit()
            print("Registro inserido com sucesso")

    except pymysql.MySQLError as e:
        print("Erro ao conectar ou inserir dados no MySQL:", e)

class SubHandler(object):
    def __init__(self, node_name):
        self.node_name = node_name

    def datachange_notification(self, val):
        print(f"Dados alterados em {self.node_name}: {val}")
        insert_into_table(val)

    def event_notification(self, event):
        print("Evento recebido:", event)

def emulated_data_change(handler):
    while True:
        emulated_value = random.uniform(0, 100)
        handler.datachange_notification(emulated_value)
        time.sleep(5)  

if __name__ == "__main__":
    handler = SubHandler("Nome_do_Nó_Emulado")

    
    print("Iniciando emulação de mudanças de dados")
    try:
        emulated_data_change(handler)
    except KeyboardInterrupt:
        print("Emulação encerrada pelo usuário")
