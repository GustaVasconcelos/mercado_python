import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:********@localhost:5432/estoque')
#Conectando o banco

sql = "SELECT id_produto,nome_produto,quantidade_produto,preco FROM estoque_produto"


connection = pg.connect(user = 'postgres', password='********',host='localhost',port='5432',database='estoque')
df = pd.read_sql_query(sql, con=engine)

curs = connection.cursor()

#Fim conexão


class menu:

    def mercado_menu(self):
        while True:
            print('-'*70)
            print('\n1 - Cadastrar produto estoque\n2 - Consulte o estoque\n3 - Alterar estoque\n4 - Comprar\n')
            print('-'*70)
            while True:
                try:
                    escolha_opcao = int(input('Escolha uma opção:'))
                    break
                except ValueError:
                    print('Apenas valores númericos')

            if(escolha_opcao == 1):
                cadastrarProduto()
                
            elif(escolha_opcao == 2):
                estq.verEstoque()
                
            elif(escolha_opcao == 3):
                editarEstoque()
            elif(escolha_opcao == 4):
                comprarProdutos()
            else:
                print('Nenhuma opção encontrada')
class estoque:


    def addProdutoNoEstoque(self,nome_produto,quantidade_produto,preco):

        inserirProduto = f"INSERT INTO estoque_produto(nome_produto,quantidade_produto,preco) VALUES ('{nome_produto}','{quantidade_produto}',{preco})"
        curs.execute(inserirProduto)
        connection.commit()

        print('-'*70)
        print('\nAdicionado no estoque')

    def verEstoque(self):
        print('-'*70)
        reg = consultar_db('SELECT * FROM estoque_produto')
        consultar_banco = pd.DataFrame(reg, columns=['id_produto','nome_produto','quantidade_produto',
                                   'preco'])
        print(consultar_banco)
    
    def alterarEstoque(self,id,opcao):

        if(opcao == 1):

            while True:

                novo_nome_produto = input('Digite o nome do produto: ').title()
                verificacao_replace = novo_nome_produto.replace(' ','')

                if(verificacao_replace.isalpha() == False):
                    print('Não é permitido caractere especial!')
                else:
                    break

            editarProduto = f"UPDATE estoque_produto SET nome_produto='{novo_nome_produto}' WHERE id_produto = {id}"

            curs.execute(editarProduto)
            connection.commit()

        elif(opcao == 2):

            while True:
                try:
                    nova_quantidade_produto = int(input("Digite a quantidade de produtos: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')
            editarProduto = f"UPDATE estoque_produto SET quantidade_produto='{nova_quantidade_produto}' WHERE id_produto = {id}"
            curs.execute(editarProduto)
            connection.commit()


        elif(opcao == 3):
            
            while True:
                try:
                    novo_preco = float(input("Digite o valor estoque do produto: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')

            editarProduto = f"UPDATE estoque_produto SET preco={novo_preco} WHERE id_produto = {id}"
            curs.execute(editarProduto)
            connection.commit()
        else:
            deletarProduto = f"DELETE FROM estoque_produto WHERE id_produto = {id}"
            curs.execute(deletarProduto)
            connection.commit()

        print('-'*70)
        print('\nAlteração Concluida!')

class Carrinho:
    valor_total = 0
    carrinho_lista = []

    def addCarrinho(self,id_produto,quantidade):

        procurar_produto = pd.read_sql_query(F'SELECT * FROM estoque_produto WHERE id_produto = {id_produto}',con=engine)
        try:
            if(int(procurar_produto['quantidade_produto']) < quantidade):
                print('-'*70)
                print('\nSem estoque')
            else:
                self.carrinho_lista.append(
                    {
                        'id_produto':int(procurar_produto['id_produto']),
                        'nome_produto':str(procurar_produto['nome_produto'].to_string()),
                        'quantidade_produtos':quantidade,
                        'valor_produto': float(procurar_produto['preco'])
                    }
                )
                self.valor_total += float(quantidade*procurar_produto['preco'])

                print('-'*70)
                print('\nProduto adicionado ao carrinho')
        except:
            print('-'*70)
            print('\nProduto não encontrado')
    def removerProdutoCarrinho(self,id_produto):
        print('-'*70)

        if(len(self.carrinho_lista) == 0):

            print('Carrinho está vazio\n')
        else:

            for index,valor in enumerate(self.carrinho_lista):

                print(f'ID: {index}\nNome Produto: {valor["nome_produto"]}\nQuantidade de Produtos: {valor["quantidade_produtos"]}\nValor do produto: {valor["valor_produto"]}')
                if(id_produto == index):
                    self.valor_total -= (valor['quantidade_produtos'] * valor['valor_produto'])
                    del(self.carrinho_lista[index])
                    
            print('-'*70)
            print('\nProduto removido')        
        
       

    def verCarrinho(self):

        print('-'*70)

        if(len(self.carrinho_lista) == 0):
            print('Nenhum produto no carrinho')
        else:
            for index,valor in enumerate(self.carrinho_lista):
                print(f'ID: {index}\nNome Produto: {valor["nome_produto"]}\nQuantidade de Produtos: {valor["quantidade_produtos"]}')
                
        print(f'Valor total: {self.valor_total}')

    def finalizarCompra(self,pagamento):
        self.valor_total -= pagamento

        for produto_carrinho in self.carrinho_lista:

            produto_verificar = pd.read_sql_query(F'SELECT * FROM estoque_produto WHERE id_produto = {produto_carrinho["id_produto"]}',con=engine)
            
            quantidade_remover = int(produto_verificar["quantidade_produto"]) - produto_carrinho['quantidade_produtos']
            diminuir_estoque = f'UPDATE estoque_produto SET quantidade_produto = {quantidade_remover} WHERE id_produto = {produto_carrinho["id_produto"]}'

            curs.execute(diminuir_estoque)
            connection.commit()

        self.carrinho_lista.clear()
        self.valor_total = 0
        
    def __str__(self):
        return self.carrinho_lista


def comprarProdutos():
    while True:
        estq.verEstoque()
        print('-'*70)
        print('1 - Adicionar ao carrinho\n2 - Remover produto do carrinho\n3 - Ver carrinho\n4 - Sair do carrinho \n5 - Finalizar a compra')
        print('-'*70)

        while True:
            try:
                escolha_opcao = int(input('Escolha uma opção:'))
                break
            except ValueError:
                print('Apenas valores númericos')
        if(escolha_opcao == 1):
            
            while True:
                try:
                    id_produto = int(input("Digite o id do produto: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')
            while True:
                try:
                    quantidade = int(input("Digite a quantidade de produtos: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')

            carrinho.addCarrinho(id_produto,quantidade)

        elif(escolha_opcao == 2):

            while True:
                try:
                    id_produto = int(input("Digite o id do produto: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')
            
            carrinho.removerProdutoCarrinho(id_produto)

        
        elif(escolha_opcao == 3):

            carrinho.verCarrinho()

        elif(escolha_opcao == 4):

            break

        elif(escolha_opcao == 5):

            for valor in carrinho.carrinho_lista:
                print(F'Produto: {valor["nome_produto"]}\nQuantidades: {valor["quantidade_produtos"]}\nValor unitario: {valor["valor_produto"]}\n')
            
            print(f'Valor total: {carrinho.valor_total}')
            while True:
                try:
                    pagamento = float(input("Digite o valor do pagamento: "))
                    while pagamento < carrinho.valor_total:
                        print('Valor menor que o valor da compra')
                        pagamento = float(input("Digite o valor do pagamento: "))
                    break            
                except ValueError:
                    print('Apenas valores númericos')
            carrinho.finalizarCompra(pagamento)
            print('-'*70)
            print('\nObrigado, a compra foi concluida, volte sempre!!')

            break

    
def cadastrarProduto():


    while True:

        nome_produto = input('Digite o nome do produto: ').title()
        verificacao_replace = nome_produto.replace(' ','')

        if(verificacao_replace.isalpha() == False):
            print('Não é permitido caractere especial!')
        else:
            break
    
    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade de produtos: "))
            break            
        except ValueError:
            print('Apenas valores númericos')

    while True:

        try:
            preco = float(input("Digite o preço do produto: "))
            break            
        except ValueError:
            print('Apenas valores númericos')

    
    estq.addProdutoNoEstoque(nome_produto,quantidade_produto,preco)

def editarEstoque():



    estq.verEstoque()
    print('-'*70)

    while True:
        try:
            id = int(input("Digite o id do produto: "))
            break            
        except ValueError:
            print('Apenas valores númericos')

    print('-'*70)
    print('1 - Nome do produto\n2 - Alterar quantidade do produto\n3 - Alterar valor do produto\n4 - Deletar produto\n')
    print('-'*70)

    while True:
        try:
            opcao = int(input("Digite uma opção: \n"))
            while opcao < 0 or opcao > 4:
                opcao = int(input("Digite uma opção válida: \n"))
            break            
        except ValueError:
            print('Apenas valores númericos')

    estq.alterarEstoque(id,opcao)


def consultar_db(sql):
  
  curs.execute(sql)
  recset = curs.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  return registros




carrinho = Carrinho()
estq = estoque()
menu_inicial = menu()
menu_inicial.mercado_menu()
   






        




