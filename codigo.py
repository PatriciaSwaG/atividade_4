import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Produto:
    def __init__(self, nome_produto, tipo, preco, nome_cliente, email_cliente):
        self.nome_produto = nome_produto
        self.tipo = tipo
        self.preco = preco
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente

    def mostrar(self):
        return f"{self.nome_produto} ({self.tipo}) - R${self.preco:.2f} - Cliente: {self.nome_cliente} - E-mail: {self.email_cliente}"

class Notebook(Produto):
    def __init__(self, nome_produto, preco, nome_cliente, email_cliente):
        super().__init__(nome_produto, "Notebook", preco, nome_cliente, email_cliente)

class Desktop(Produto):
    def __init__(self, nome_produto, preco, nome_cliente, email_cliente):
        super().__init__(nome_produto, "Desktop", preco, nome_cliente, email_cliente)

class Monitor(Produto):
    def __init__(self, nome_produto, preco, nome_cliente, email_cliente):
        super().__init__(nome_produto, "Monitor", preco, nome_cliente, email_cliente)

class Periferico(Produto):
    def __init__(self, nome_produto, preco, nome_cliente, email_cliente):
        super().__init__(nome_produto, "Periférico", preco, nome_cliente, email_cliente)

def carregarProdutos():
    try:
        with open("database.txt", "r") as file:
            for line in file:
                nome_produto, tipo, preco, nome_cliente, email_cliente = line.strip().split(", ")
                preco = float(preco)
                if tipo == "Notebook":
                    produto = Notebook(nome_produto, preco, nome_cliente, email_cliente)
                elif tipo == "Desktop":
                    produto = Desktop(nome_produto, preco, nome_cliente, email_cliente)
                elif tipo == "Monitor":
                    produto = Monitor(nome_produto, preco, nome_cliente, email_cliente)
                else:
                    produto = Periferico(nome_produto, preco, nome_cliente, email_cliente)
                lista_produtos.append(produto)
    except FileNotFoundError:
        pass  

def salvarProdutos():
    with open("database.txt", "w") as file:
        for produto in lista_produtos:
            file.write(f"{produto.nome_produto}, {produto.tipo}, {produto.preco}, {produto.nome_cliente}, {produto.email_cliente}\n")

lista_produtos = []

def cadastraProduto():
    nome_produto = entryNomeProduto.get()
    preco = entryPreco.get()
    tipo = varTipo.get()
    nome_cliente = entryNomeCliente.get()
    email_cliente = entryEmailCliente.get()
    erro = 0

    if nome_produto == "" or preco == "" or nome_cliente == "" or email_cliente == "":
        messagebox.showinfo("Erro", "Todos os campos devem ser preenchidos!")
        erro = 1

    if erro == 0:
        try:
            preco = float(preco)
        except ValueError:
            messagebox.showinfo("Erro", "Preço deve ser um número válido!")
            erro = 1

    if erro == 0:
        if tipo == "Notebook":
            produto = Notebook(nome_produto, preco, nome_cliente, email_cliente)
        elif tipo == "Desktop":
            produto = Desktop(nome_produto, preco, nome_cliente, email_cliente)
        elif tipo == "Monitor":
            produto = Monitor(nome_produto, preco, nome_cliente, email_cliente)
        else:
            produto = Periferico(nome_produto, preco, nome_cliente, email_cliente)
        
        lista_produtos.append(produto)
        salvarProdutos()
        messagebox.showinfo("Cadastro", f"Produto {nome_produto} cadastrado com sucesso!")
        entryNomeProduto.delete(0, tk.END)
        entryPreco.delete(0, tk.END)
        entryNomeCliente.delete(0, tk.END)
        entryEmailCliente.delete(0, tk.END)
        atualizaListabox()

def atualizaListabox():
    listbox.delete(0, tk.END)
    for produto in lista_produtos:
        listbox.insert(tk.END, produto.mostrar())

janela = tk.Tk()
janela.title("Cadastro de Produtos de Computadores")
janela.geometry("600x400")
janela.config(bg="#f0f0f0")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
tab1.grid_rowconfigure(6, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista de Produtos")

label1 = tk.Label(tab1, text="Nome do Produto: ", font=("Helvetica", 14), bg="#f0f0f0")
label1.grid(row=0, column=0, sticky="w", padx=15, pady=10)

entryNomeProduto = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryNomeProduto.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label2 = tk.Label(tab1, text="Preço: R$", font=("Helvetica", 14), bg="#f0f0f0")
label2.grid(row=1, column=0, sticky="w", padx=15, pady=10)

entryPreco = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryPreco.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label3 = tk.Label(tab1, text="Nome do Cliente: ", font=("Helvetica", 14), bg="#f0f0f0")
label3.grid(row=2, column=0, sticky="w", padx=15, pady=10)

entryNomeCliente = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryNomeCliente.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

label4 = tk.Label(tab1, text="Email do Cliente: ", font=("Helvetica", 14), bg="#f0f0f0")
label4.grid(row=3, column=0, sticky="w", padx=15, pady=10)

entryEmailCliente = tk.Entry(tab1, font=("Helvetica", 14), bd=2, relief="solid", width=30)
entryEmailCliente.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo de Produto: ", font=("Helvetica", 14), bg="#f0f0f0").grid(row=4, column=0, sticky="w", padx=15, pady=10)

varTipo = tk.StringVar(value="Notebook")
tk.Radiobutton(tab1, text="Notebook", font=("Helvetica", 14), variable=varTipo, value="Notebook", bg="#f0f0f0").grid(row=4, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Desktop", font=("Helvetica", 14), variable=varTipo, value="Desktop", bg="#f0f0f0").grid(row=4, column=1, sticky="e", padx=10)
tk.Radiobutton(tab1, text="Monitor", font=("Helvetica", 14), variable=varTipo, value="Monitor", bg="#f0f0f0").grid(row=5, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Periférico", font=("Helvetica", 14), variable=varTipo, value="Periferico", bg="#f0f0f0").grid(row=5, column=1, sticky="e", padx=10)

tk.Button(tab1, text="Cadastrar Produto", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=cadastraProduto, relief="solid").grid(row=6, columnspan=2, pady=20)

listbox = tk.Listbox(tab2, font=("Helvetica", 12), width=45, height=10, bd=2, relief="solid")
listbox.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)
tk.Button(tab2, text="Atualizar Lista", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=atualizaListabox, relief="solid").grid(row=1, column=0, pady=10)

carregarProdutos()

janela.mainloop()