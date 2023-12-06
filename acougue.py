import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import os.path
import pickle

class Produto():
    def __init__(self,codigo,descricao,preco):
        self.__codigo=codigo
        self.__descricao=descricao
        self.__preco=preco
    
    @property
    def codigo(self):
        return self.__codigo
    @property
    def descricao(self):
        return self.__descricao
    @property
    def preco(self):
        return self.__preco

    
    def getProduto(self):
        return "Descricao: " + str(self.descricao)+"\n"\
        + "Preço: " + str(self.preco)+"\n"


class Cliente():
    def __init__(self,nome,endereco,email,cpf):
        self.__nome=nome
        self.__endereco=endereco
        self.__email=email
        self.__cpf=cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self):
        return self.__cpf
    @property
    def listaClientes(self):
        return self.__listaClientes
    
    @cpf.setter
    def cpf(self,valor):
        if (valor.isnumeric()==False):
           raise ValueError("Valor invalido:{}".format(valor)) 
        
        else:
            self.__cpf=int(valor)
            
    def getCliente(self):
        return "Nome: " + str(self.nome) +"\n"\
        + "Endereço: " + str(self.endereco)+"\n"\
        + "E-mail: " + str(self.email)+"\n"

class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self,controle):
        tk.Toplevel.__init__(self)
        self.geometry("500x500")
        self.config(bg="#ffa500")
        self.title("Cadastrar Produto")
        self.ctrl=controle    
        
        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton=tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameButton.pack()
        
        #labels antes dos campos de inserção de dados
        self.labelCodigo=tk.Label(self.frameCodigo, text="Codigo: ",bg="#ffa500")
        self.labelDescricao=tk.Label(self.frameDescricao, text="Descrição: ",bg="#ffa500")
        self.labelPreco=tk.Label(self.framePreco, text="Preço: ",bg="#ffa500")
        
        #lfazendo as labels aparecerem
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPreco.pack(side="left")
        
        
        self.entryCodigo=tk.Entry(self.frameCodigo, width=10)
        self.entryDescricao=tk.Entry(self.frameDescricao, width=10)
        self.entryPreco=tk.Entry(self.framePreco, width=10)
        
        self.entryCodigo.pack(side="left")
        self.entryDescricao.pack(side="left")
        self.entryPreco.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", self.ctrl.enterHandlerProduto)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteCadastraCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("500x500")
        self.config(bg="#ffa500")
        self.title("Cadastrar Cliente")
        self.ctrl = controle    

        self.frameNome = tk.Frame(self)
        self.frameEndereco = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameCpf = tk.Frame(self)
        self.frameButton01 = tk.Frame(self)

        self.frameNome.pack()
        self.frameEndereco.pack()
        self.frameEmail.pack()
        self.frameCpf.pack()
        self.frameButton01.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ", bg="#ffa500")
        self.labelEndereco = tk.Label(self.frameEndereco, text="Endereço: ",bg="#ffa500")
        self.labelEmail = tk.Label(self.frameEmail, text="E-mail: ",bg="#ffa500")
        self.labelCpf = tk.Label(self.frameCpf, text="CPF: ",bg="#ffa500")

        self.labelNome.pack(side="left")
        self.labelEndereco.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelCpf.pack(side="left")

        
        self.entryNome=tk.Entry(self.frameNome, width=20)
        self.entryEndereco=tk.Entry(self.frameEndereco, width=20)
        self.entryEmail=tk.Entry(self.frameEmail, width=20)
        self.entryCpf=tk.Entry(self.frameCpf, width=20)

        self.entryNome.pack(side="left")
        self.entryEndereco.pack(side="left")
        self.entryEmail.pack(side="left")
        self.entryCpf.pack(side="left")
        
        self.buttonSubmit = tk.Button(self.frameButton01 ,text="Cadastrar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerCliente)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


#tela de busca de cliente
class LimiteConsultaCliente(tk.Toplevel):
    def __init__(self,controle):
        tk.Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Consultar Cliente")
        self.config(bg="#5e2129")
        self.ctrl=controle
        
        self.tituloFrame=tk.Frame(self)
        self.tituloFrame.pack()
        
        self.labelTitulo=tk.Label(self.tituloFrame, text="Digite o cpf: ", bg="#5e2129",fg="white")
        self.labelTitulo.pack()
        
        self.frameCPF=tk.Frame(self)
        self.frameCPF.pack()
        
        self.entryCpf=tk.Entry(self.frameCPF,width=15)
        self.entryCpf.pack()
        
        self.frameBotao=tk.Frame(self)
        self.frameBotao.pack()
        
        self.botao=tk.Button(self.frameBotao, command=controle.exibeCliente)
        self.botao.config(bg="yellow", text="Consultar")
        self.botao.pack()

        self.frameClientes = tk.Frame(self)
        self.frameClientes.pack()
        self.textClientes = tk.Text(self.frameClientes, height=20,width=40)
        self.textClientes.pack()
        self.textClientes.config(state=tk.DISABLED,bg="#5e2129")        
        


        
#tela de busca de produto
class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self,controle):
        tk.Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Consultar Produto")
        self.ctrl=controle
        self.config(bg="#5e2129")
        
        self.tituloFrame=tk.Frame(self)
        self.tituloFrame.pack()
        
        self.labelTitulo=tk.Label(self.tituloFrame, text="Digite o codigo: ", bg="#5e2129")
        self.labelTitulo.pack(side="left")
        
        
        self.entryCodigo=tk.Entry(self.tituloFrame,width=15)
        self.entryCodigo.pack()
        
        self.frameBotao=tk.Frame(self)
        self.frameBotao.pack()
        
        self.botao=tk.Button(self.frameBotao, command=controle.exibeProduto)
        self.botao.config(bg="blue", text="Consultar")
        self.botao.pack()

        self.frameProdutos = tk.Frame(self)
        self.frameProdutos.pack()
        self.textProdutos = tk.Text(self.frameProdutos, height=20,width=40)
        self.textProdutos.pack()
        self.textProdutos.config(state=tk.DISABLED,bg="#5e2129")  


class CtrlAcougue():
    def __init__(self,controlador):
        if os.path.isfile("clientes.pickle"):
            with open("clientes.pickle", "rb") as f:
                self.listaClientes = pickle.load(f) 
        
        else:
            self.listaClientes=[]
            
        if os.path.isfile("produtos.pickle"):
            with open("produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)
            
        else:
            self.listaProdutos=[]
        
        self.controlador=controlador
    
    def consultaProd(self):
        self.limConProd=LimiteConsultaProduto(self)
        
    def consultaClientes(self):
        self.limConCli=LimiteConsultaCliente(self)
            
    def cadastraProduto(self):
        self.limCadProd=LimiteCadastraProduto(self)
        
    def cadastraCliente(self):
        self.limCadCliente=LimiteCadastraCliente(self)
        
    def enterHandlerCliente(self):
        nome=self.limCadCliente.entryNome.get()
        endereco=self.limCadCliente.entryEndereco.get()
        email=self.limCadCliente.entryEmail.get()
        cpf=self.limCadCliente.entryCpf.get()
        
        try:
            cliente=Cliente(nome,endereco,email,cpf)
            self.listaClientes.append(cliente)
            self.limCadCliente.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
            
            # Salvar os dados no arquivo após cadastrar um cliente
            with open("clientes.pickle", "wb") as f:
                pickle.dump(self.listaClientes, f)
        except ValueError:
            self.limCadCliente.mostraJanela('Error', error)
            
    def enterHandlerProduto(self,event=None):
        codigo=self.limCadProd.entryCodigo.get()
        descricao=self.limCadProd.entryDescricao.get()
        preco = self.limCadProd.entryPreco.get()
        try:
            produto=Produto(codigo,descricao,preco)
            self.listaProdutos.append(produto)
            self.limCadProd.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
            
            # Salvar os dados no arquivo após cadastrar um cliente
            with open("produtos.pickle", "wb") as f:
                pickle.dump(self.listaProdutos, f)
        except ValueError as error:
            self.limCadCliente.mostraJanela('Error', error)
            
    def exibeCliente(self):
        cpf = self.limConCli.entryCpf.get()
        self.limConCli.textClientes.config(state="normal")
        for pessoa in self.listaClientes:
            if pessoa.cpf==cpf:
                clienteSel=pessoa.getCliente()+"\n\n"
                self.limConCli.textClientes.insert(1.0,clienteSel)
        self.limConCli.textClientes.config(state="disabled")
        
    def exibeProduto(self):
        codigo = self.limConProd.entryCodigo.get()
        self.limConProd.textProdutos.config(state="normal")
        for produto in self.listaProdutos:
            if produto.codigo==codigo:
                produtoSel=produto.getProduto()+"\n\n"
                self.limConProd.textProdutos.insert(1.0,produtoSel)
        self.limConProd.textProdutos.config(state="disabled")
        

        