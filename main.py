import mysql.connector

#conectando ao banco

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='gestafy'
)
print('CONECTADO COM SUCESSO!!')
cursor = conexao.cursor()


def inserir():
    nome = str(input('Digite seu nome e sobrenome: '))
    email = str(input('Digite seu email: '))
    senha = str(input('Crie uma senha: '))

    comandosql = f'INSERT INTO usuarios (nome,email,senha) VALUES ("{nome}","{email}","{senha}")'
    cursor.execute(comandosql)
    conexao.commit()
    print("USUÁRIO CADASTRADO COM SUCESSO!!")

def consultar():
    comandosql = "SELECT concat('Nome: ', nome, ' Email: ', email) as usuario_info from usuarios"
    cursor.execute(comandosql)
    resultadodaconsulta = cursor.fetchall()
    print(resultadodaconsulta)

def consultarid():
    id_usuario = int(input('Digite o id do Usuário: '))
    comandosql = f'select nome from usuarios where id_usuario ={id_usuario}'
    cursor.execute(comandosql)
    resultadodaconsulta = cursor.fetchall()
    print(f'Id do usuário: {id_usuario} | Nome: {resultadodaconsulta}')

def atualizarcadastro():
    id_usuario = int(input('Digite seu id:'))
    nome = input('Digite o seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    comando = f'UPDATE usuarios set nome,email,senha = "{nome}","{email}","{senha}" where id_usuario = {id_usuario}'
    cursor.execute(comando)
    conexao.commit()

while True:
    menu = int(input("Escolha uma das opções:\n"
                     "1 - Cadastrar usuário\n"
                     "2 - Consultar usuários\n"
                     "3 - Consultar pelo id do usuário\n"
                     "4 - Atualizar cadastro\n"
                     "5 - Deletar usuário\n"
                     "6 - Sair do sistema\n"))
    if menu == 1:
        inserir()
    elif menu == 2:
        consultar()
    elif menu == 3:
        consultarid()
    elif menu == 4:
        atualizarcadastro()