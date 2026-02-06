# 📘 Nota.py - Loja / Sistema de Dados
# Autor: Ryan_0
# Data: 06/02/2026
# Tecnologia: Python 3.x
# Finalidade: Guardar dados de loja, itens, preços, unidades, alimentos, keys e chaves de acesso.

# =========================
# LISTA DE ITENS (100)
# =========================
itens = [
    "Arroz", "Feijão", "Macarrão", "Açúcar", "Sal", "Óleo de soja", "Azeite",
    "Farinha de trigo", "Farinha de milho", "Café", "Leite", "Leite em pó",
    "Achocolatado", "Pão francês", "Pão de forma", "Bolo", "Biscoito recheado",
    "Biscoito água e sal", "Bolacha cream cracker", "Chocolate", "Bala",
    "Chiclete", "Refrigerante", "Suco de caixinha", "Água mineral", "Cerveja",
    "Vinho", "Iogurte", "Queijo", "Presunto", "Mortadela", "Salsicha", "Linguiça",
    "Carne bovina", "Carne de frango", "Carne suína", "Peixe", "Ovo", "Manteiga",
    "Margarina", "Maionese", "Ketchup", "Mostarda", "Molho de tomate",
    "Extrato de tomate", "Milho em conserva", "Ervilha em conserva",
    "Atum em lata", "Sardinha em lata", "Salgadinho", "Pipoca",
    "Pipoca de micro-ondas", "Sorvete", "Gelatina", "Pudim", "Fermento",
    "Leite condensado", "Creme de leite", "Arroz integral", "Feijão preto",
    "Lentilha", "Grão-de-bico", "Aveia", "Cereal matinal", "Mel", "Doce de leite",
    "Geleia", "Fruta (banana)", "Fruta (maçã)", "Fruta (laranja)",
    "Verdura (alface)", "Verdura (tomate)", "Verdura (cebola)",
    "Verdura (batata)", "Verdura (cenoura)", "Sabão em pó", "Detergente",
    "Amaciante", "Água sanitária", "Desinfetante", "Esponja", "Papel higiênico",
    "Papel toalha", "Guardanapo", "Shampoo", "Condicionador", "Sabonete",
    "Pasta de dente", "Escova de dente", "Fio dental", "Desodorante",
    "Absorvente", "Fralda descartável", "Ração para cachorro",
    "Ração para gato", "Carvão", "Fósforo", "Vela", "Pilha", "Isqueiro"
]

# =========================
# PREÇOS CORRESPONDENTES
# =========================
precos = [
    25.90, 8.50, 6.99, 4.80, 2.50, 7.90, 18.50, 5.60, 4.20, 14.90,
    4.50, 18.90, 7.50, 0.80, 6.90, 12.00, 3.50, 3.20, 3.40, 6.80,
    1.50, 1.20, 8.90, 4.50, 2.00, 5.50, 22.00, 4.90, 18.00, 6.50,
    4.80, 4.20, 9.90, 32.00, 14.90, 19.90, 21.00, 12.50, 9.80, 7.90,
    6.50, 5.20, 4.90, 3.80, 4.20, 5.00, 4.80, 9.90, 8.50, 6.00,
    3.50, 4.00, 5.50, 2.80, 4.90, 6.20, 3.90, 7.50, 5.90, 8.20,
    7.80, 9.50, 6.90, 11.90, 10.50, 7.00, 12.90, 9.80, 3.00, 3.50,
    4.20, 2.50, 3.00, 3.80, 4.00, 15.90, 3.20, 6.80, 4.50, 5.90,
    3.00, 18.00, 6.00, 5.50, 2.50, 7.20, 9.90, 4.00, 12.00, 28.00,
    26.00, 15.00, 4.50, 1.20, 6.00, 7.50, 5.00, 4.20, 3.80, 2.00
]

# =========================
# UNIDADES DE MEDIDA
# =========================
unidades = ["mg","g","kg","t","mm","cm","dm","m","dam","hm","km",
            "ml","cl","dl","l","mm²","cm²","m²","km²","mm³","cm³","m³",
            "s","min","h","dia","°C","K","°F"]

info_unidades = {
    "mg":"miligrama (massa)","g":"grama (massa)","kg":"quilograma (massa)","t":"tonelada (massa)",
    "mm":"milímetro (comprimento)","cm":"centímetro (comprimento)","dm":"decímetro (comprimento)",
    "m":"metro (comprimento)","dam":"decâmetro (comprimento)","hm":"hectômetro (comprimento)",
    "km":"quilômetro (comprimento)","ml":"mililitro (volume)","cl":"centilitro (volume)",
    "dl":"decilitro (volume)","l":"litro","mm²":"milímetro quadrado (área)",
    "cm²":"centímetro quadrado (área)","m²":"metro quadrado (área)","km²":"quilômetro quadrado (área)",
    "mm³":"milímetro cúbico (volume)","cm³":"centímetro cúbico (volume)","m³":"metro cúbico (volume)",
    "s":"segundo (tempo)","min":"minuto (tempo)","h":"hora (tempo)","dia":"dia",
    "°C":"grau Celsius (temperatura)","K":"Kelvin (temperatura)","°F":"Fahrenheit (temperatura)"
}

# =========================
# ALIMENTOS COM DETALHES
# =========================
alimentos = {
    "Arroz":{"descricao":"Grão usado como base da alimentação","unidade":"kg","preco":25.90,"categoria":"Grãos"},
    "Feijão":{"descricao":"Leguminosa rica em proteínas","unidade":"kg","preco":8.50,"categoria":"Leguminosas"},
    "Macarrão":{"descricao":"Massa feita de trigo","unidade":"kg","preco":6.99,"categoria":"Massas"},
    "Açúcar":{"descricao":"Usado para adoçar alimentos","unidade":"kg","preco":4.80,"categoria":"Doces"},
    "Sal":{"descricao":"Usado para temperar","unidade":"kg","preco":2.50,"categoria":"Temperos"},
    "Óleo de soja":{"descricao":"Óleo para cozinhar","unidade":"l","preco":7.90,"categoria":"Óleos"},
    "Azeite":{"descricao":"Óleo de oliva","unidade":"l","preco":18.50,"categoria":"Óleos"}
    # Você pode continuar adicionando os 100 alimentos com todas informações aqui
}

# =========================
# KEYS DE ACESSO
# =========================
keys = [
    "KEY_001_A9273738282737282828272726263627272928273728282737ABCDEFGHJKLMNPQRSTUVWXYZ",
    "KEY_002_B8273628192736462819273646281927364628192736QWERTYUIOPASDFGHJK",
    "KEY_003_C8273628192736462819273646281927364628192736ZXCVBNMASDFGHJKQWERTY",
    # ... continue até KEY_100
]

# =========================
# CHAVES DE ACESSO
# =========================
chaves_acesso = [
    "1028277372828199282827372782828272726636272729",
    "9982736462819273646281927364628192736462819273",
    "1928374659283746592837465928374659283746592837",
    # ... continue até a última chave
]

# =========================
# FUNÇÕES EXEMPLO (Opcional)
# =========================
def mostrar_itens():
    for i, item in enumerate(itens):
        print(f"{i+1}: {item} - R${precos[i]:.2f}")

def buscar_item(nome):
    if nome in itens:
        idx = itens.index(nome)
        return {"item": nome, "preco": precos[idx]}
    return None

# =========================
# EXECUÇÃO DE TESTE
# =========================
if __name__ == "__main__":
    print("===== LISTA DE ITENS =====")
    mostrar_itens()
    print("\nBuscando 'Arroz':", buscar_item("Arroz"))