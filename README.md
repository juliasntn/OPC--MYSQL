# OPC UA to MySQL Integration

Este script Python facilita a integração entre um servidor OPC UA e um banco de dados MySQL. Ele se conecta a um servidor OPC UA, monitora as mudanças nos valores de um nó específico e insere esses valores em uma tabela MySQL.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pymysql`
  - `opcua`

## Instalação

1. Clone este repositório em seu ambiente local:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
```

2. Instale as dependências Python necessárias:

```bash
pip install pymysql opcua
```

## Uso

1. Substitua as seguintes informações no script `opcua_to_mysql.py`:

   - `localhost`: Endereço do host do seu servidor MySQL.
   - `USER`: Nome de usuário do seu servidor MySQL.
   - `PASS`: Senha do seu servidor MySQL.
   - `DATABASE`: Nome do banco de dados MySQL.
   - `opc.tcp://SERVIDOR`: Endereço do servidor OPC UA.
   - `NODEID`: ID do nó que você deseja monitorar.
   - `Nome_do_Nó`: Nome do nó que você deseja monitorar.

2. Execute o script Python:

```bash
python opcua_to_mysql.py
```

3. O script começará a monitorar o nó especificado no servidor OPC UA. Quando houver uma alteração nos dados desse nó, o valor será inserido na tabela MySQL especificada.

4. Pressione `Ctrl+C` para encerrar o script.

## Observação

opcua_mysql_1tag.py - possui apenas uma tag sendo enviada para o banco de dados
opcua_mysql_2tags.py - possui duas tags sendo enviadas caso precise de mais basta adicionar

## Banco de dados

Utilizado:\
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Exemplo de tabela para 1 tag:

```
CREATE TABLE sensores (
id INT AUTO_INCREMENT PRIMARY KEY,
node1_value FLOAT NOT NULL,
dataehora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```

Exemplo de tabela para 2 tag:

```
CREATE TABLE sensores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    node1_value FLOAT NOT NULL,
    node2_value FLOAT NOT NULL,
    dataehora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```

## Contatos:

[![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:falecomjuliasantana@gmail.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/julia-santana-040a12180/)

## E-mail: falecomjuliasantana@gmail.com
