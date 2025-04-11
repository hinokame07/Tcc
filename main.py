import tkinter as tk
from tkinter import messagebox

# --- Dados da loja (atualizados) ---
produtos = {
    "Quadro geek": 450,
    "Funko pop": 3000,
    "Monitor Curvo": 1200,
    "Cubo mágico": 1800,
    "Bis": 400
}

saldo_inicial = 1000  # Ctrl Cash inicial

# --- Função de compra ---
def comprar():
    selecionado = lista_produtos.curselection()
    if not selecionado:
        messagebox.showwarning("Nenhum item selecionado", "Escolha um produto para comprar.")
        return

    nome_completo = lista_produtos.get(selecionado)
    produto = nome_completo.split(" - ")[0]
    preco = produtos[produto]

    global saldo
    if preco <= saldo:
        saldo -= preco
        adicionar_ao_inventario(produto, preco)
        atualizar_saldo()
        messagebox.showinfo("Compra realizada", f"Você comprou: {produto} por {preco} Ctrl Cash!")
    else:
        messagebox.showwarning("Saldo insuficiente", "Você não tem Ctrl Cash suficiente!")

# --- Função para adicionar saldo ---
def adicionar_saldo():
    global saldo
    try:
        valor = int(entrada_valor.get())
        if valor > 0:
            saldo += valor
            atualizar_saldo()
            entrada_valor.delete(0, tk.END)
            messagebox.showinfo("Saldo adicionado", f"Você adicionou {valor} Ctrl Cash!")
        else:
            messagebox.showwarning("Valor inválido", "Digite um valor positivo.")
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Digite um número válido.")

# --- Atualiza o saldo na interface ---
def atualizar_saldo():
    lbl_saldo.config(text=f"Saldo: {saldo} Ctrl Cash")

# --- Adiciona produto ao inventário ---
def adicionar_ao_inventario(produto, preco):
    inventario.insert(tk.END, f"{produto} - {preco} CC")
    atualizar_total()

# --- Atualiza o total do inventário ---
def atualizar_total():
    total = 0
    for item in inventario.get(0, tk.END):
        preco = int(item.split(" - ")[1].split(" ")[0])
        total += preco
    lbl_total.config(text=f"Total: {total} CC")

# --- Interface Gráfica ---
app = tk.Tk()
app.title("🛒 Lojinha Ctrl Cash")
app.geometry("400x600")
app.config(bg="#f4f4f9")  # Cor de fundo suave

# Título
lbl_titulo = tk.Label(app, text="🛒 Lojinha Ctrl Cash", font=("Verdana", 18, "bold"), fg="#4CAF50", bg="#f4f4f9")
lbl_titulo.pack(pady=15)

# Saldo
lbl_saldo = tk.Label(app, text=f"Saldo: {saldo_inicial} Ctrl Cash", font=("Verdana", 12), fg="#333333", bg="#f4f4f9")
lbl_saldo.pack()

# Lista de produtos
lista_produtos = tk.Listbox(app, height=6, font=("Verdana", 11), bg="#FFFFFF", fg="#333333", selectmode=tk.SINGLE, bd=2, relief="solid", width=30)
for item in produtos:
    lista_produtos.insert(tk.END, f"{item} - {produtos[item]} CC")
lista_produtos.pack(pady=10)

# Botão de compra
btn_comprar = tk.Button(app, text="Comprar", font=("Verdana", 12), bg="#4CAF50", fg="white", command=comprar, relief="flat", width=20, height=2)
btn_comprar.pack(pady=5)

# Campo de entrada para adicionar Ctrl Cash
entrada_valor = tk.Entry(app, font=("Verdana", 12), justify='center', bd=2, relief="solid", width=20)
entrada_valor.pack(pady=5)
entrada_valor.insert(0, "100")  # valor padrão, opcional

# Botão de adicionar saldo
btn_adicionar = tk.Button(app, text="Adicionar Ctrl Cash", font=("Verdana", 12), bg="#2196F3", fg="white", command=adicionar_saldo, relief="flat", width=20, height=2)
btn_adicionar.pack(pady=5)

# --- Inventário (seção azul) ---
lbl_inventario = tk.Label(app, text="📦 Inventário", font=("Verdana", 14, "bold"), fg="white", bg="#2196F3")
lbl_inventario.pack(pady=10, fill=tk.X)

# Lista do inventário
inventario = tk.Listbox(app, height=6, font=("Verdana", 11), bg="#f0f8ff", fg="#333333", selectmode=tk.SINGLE, bd=2, relief="solid", width=30)
inventario.pack(pady=10)

# Total do inventário
lbl_total = tk.Label(app, text="Total: 0 CC", font=("Verdana", 12), fg="#333333", bg="#f4f4f9")
lbl_total.pack(pady=5)

# Variável de saldo
saldo = saldo_inicial

app.mainloop()
