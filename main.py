import tkinter as tk
import acougue as ac

class LimitePrincipal(tk.Tk):
    def __init__(self, root,controle):
        self.root=root
        self.controle=controle
        self.root.geometry('900x400')
        self.root.config(bg="#ffa500")
        #criando o menu
        self.menuBar=tk.Menu(self.root)
        #para cadastrar os produtos e clientes:
        self.menuCadastrar=tk.Menu(self.menuBar)
        #permite consultar faturamento por produto, produtos, clientes e faturamento por cliente
        self.menuConsultar=tk.Menu(self.menuBar)
        #para fazer compras de produtos e emitir nota fiscal
        self.menuComprar=tk.Menu(self.menuBar)


        #para salvar e sair do programa
        self.menuSair=tk.Menu(self.menuBar)

        self.menuBar.add_cascade(label="Cadastrar", menu=self.menuCadastrar)
        self.menuBar.add_cascade(label="Consultar", menu=self.menuConsultar)
        self.menuBar.add_cascade(label="Comprar", menu=self.menuComprar)
        self.menuBar.add_cascade(label="Sair", menu=self.menuSair)

        #criando comando do menu cadastrar
        self.menuCadastrar.add_command(label="Produto", command=self.controle.abrirCadastraProd)
        self.menuCadastrar.add_command(label="Cliente", command=self.controle.abrirCadastraCliente)

        #criando comandos do menu consultar
        self.menuConsultar.add_command(label="Produto", command=self.controle.abrirConsultaProd)
        self.menuConsultar.add_command(label="Cliente", command=self.controle.abrirConsultaCliente)
        self.menuConsultar.add_command(label="Faturamento Produto")
        self.menuConsultar.add_command(label="Faturamento Cliente")
        
        #criando comando do menu comprar
        self.menuComprar.add_command(label="Realizar Compra")

        self.root.config(menu=self.menuBar)
        
        self.frameTitulo=tk.Frame(self.root,bg="#ffa500")
        self.frameTitulo.pack()
        
        self.labelTitulo=tk.Label(self.frameTitulo, text="Olá Usuario(a)!",bg="#ffa500")
        self.labelTitulo.pack()
        
        self.frameText=tk.Frame(self.root,bg="#ffa500")
        self.frameText.pack()
        
        self.labelText=tk.Label(self.frameTitulo,bg="#ffa500", text="Esse é meu trabalho desenvolvido para a matéria de Programação Orientada a objetos. Explore e desvende um sistema gerencial de açougue")
        self.labelText.pack()

class ControlePrincipal():
    def __init__(self):
        self.root=tk.Tk()
        self.ctrlAcougue=ac.CtrlAcougue(self.root)
        self.limite=LimitePrincipal(self.root,self)
        self.root.title("Na Brasa - Açougue Itajubense")
        self.root.mainloop()
        
    def abrirConsultaProd(self):
       self.ctrlAcougue.consultaProd()
        
    def abrirConsultaCliente(self):
        self.ctrlAcougue.consultaClientes()
        
    def abrirCadastraProd(self):
        self.ctrlAcougue.cadastraProduto()
        
    def abrirCadastraCliente(self):
        self.ctrlAcougue.cadastraCliente()

if __name__ == '__main__':
    c = ControlePrincipal() 