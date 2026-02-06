
itens = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Açúcar",
    "Sal",
    "Óleo de soja",
    "Azeite",
    "Farinha de trigo",
    "Farinha de milho",
    "Café",
    "Leite",
    "Leite em pó",
    "Achocolatado",
    "Pão francês",
    "Pão de forma",
    "Bolo",
    "Biscoito recheado",
    "Biscoito água e sal",
    "Bolacha cream cracker",
    "Chocolate",
    "Bala",
    "Chiclete",
    "Refrigerante",
    "Suco de caixinha",
    "Água mineral",
    "Cerveja",
    "Vinho",
    "Iogurte",
    "Queijo",
    "Presunto",
    "Mortadela",
    "Salsicha",
    "Linguiça",
    "Carne bovina",
    "Carne de frango",
    "Carne suína",
    "Peixe",
    "Ovo",
    "Manteiga",
    "Margarina",
    "Maionese",
    "Ketchup",
    "Mostarda",
    "Molho de tomate",
    "Extrato de tomate",
    "Milho em conserva",
    "Ervilha em conserva",
    "Atum em lata",
    "Sardinha em lata",
    "Salgadinho",
    "Pipoca",
    "Pipoca de micro-ondas",
    "Sorvete",
    "Gelatina",
    "Pudim",
    "Fermento",
    "Leite condensado",
    "Creme de leite",
    "Arroz integral",
    "Feijão preto",
    "Lentilha",
    "Grão-de-bico",
    "Aveia",
    "Cereal matinal",
    "Mel",
    "Doce de leite",
    "Geleia",
    "Fruta (banana)",
    "Fruta (maçã)",
    "Fruta (laranja)",
    "Verdura (alface)",
    "Verdura (tomate)",
    "Verdura (cebola)",
    "Verdura (batata)",
    "Verdura (cenoura)",
    "Sabão em pó",
    "Detergente",
    "Amaciante",
    "Água sanitária",
    "Desinfetante",
    "Esponja",
    "Papel higiênico",
    "Papel toalha",
    "Guardanapo",
    "Shampoo",
    "Condicionador",
    "Sabonete",
    "Pasta de dente",
    "Escova de dente",
    "Fio dental",
    "Desodorante",
    "Absorvente",
    "Fralda descartável",
    "Ração para cachorro",
    "Ração para gato",
    "Carvão",
    "Fósforo",
    "Vela",
    "Pilha",
    "Isqueiro"
]
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
unidades = [
    "mg",   # miligrama
    "g",    # grama
    "kg",   # quilograma
    "t",    # tonelada

    "mm",   # milímetro
    "cm",   # centímetro
    "dm",   # decímetro
    "m",    # metro
    "dam",  # decâmetro
    "hm",   # hectômetro
    "km",   # quilômetro

    "ml",   # mililitro
    "cl",   # centilitro
    "dl",   # decilitro
    "l",    # litro

    "mm²",  # milímetro quadrado
    "cm²",  # centímetro quadrado
    "m²",   # metro quadrado
    "km²",  # quilômetro quadrado

    "mm³",  # milímetro cúbico
    "cm³",  # centímetro cúbico
    "m³",   # metro cúbico

    "s",    # segundo
    "min",  # minuto
    "h",    # hora
    "dia",  # dia

    "°C",   # grau Celsius
    "K",    # Kelvin
    "°F"    # Fahrenheit
]
info_unidades = {
    "mg": "miligrama (massa)",
    "g": "grama (massa)",
    "kg": "quilograma (massa)",
    "t": "tonelada (massa)",

    "mm": "milímetro (comprimento)",
    "cm": "centímetro (comprimento)",
    "dm": "decímetro (comprimento)",
    "m": "metro (comprimento)",
    "dam": "decâmetro (comprimento)",
    "hm": "hectômetro (comprimento)",
    "km": "quilômetro (comprimento)",

    "ml": "mililitro (volume)",
    "cl": "centilitro (volume)",
    "dl": "decilitro (volume)",
    "l": "litro (volume)",

    "mm²": "milímetro quadrado (área)",
    "cm²": "centímetro quadrado (área)",
    "m²": "metro quadrado (área)",
    "km²": "quilômetro quadrado (área)",

    "mm³": "milímetro cúbico (volume)",
    "cm³": "centímetro cúbico (volume)",
    "m³": "metro cúbico (volume)",

    "s": "segundo (tempo)",
    "min": "minuto (tempo)",
    "h": "hora (tempo)",
    "dia": "dia (tempo)",

    "°C": "grau Celsius (temperatura)",
    "K": "Kelvin (temperatura)",
    "°F": "Fahrenheit (temperatura)"
}
alimentos = {
    "Arroz": {
        "descricao": "Grão usado como base da alimentação",
        "unidade": "kg",
        "preco": 25.90,
        "categoria": "Grãos"
    },
    "Feijão": {
        "descricao": "Leguminosa rica em proteínas",
        "unidade": "kg",
        "preco": 8.50,
        "categoria": "Leguminosas"
    },
    "Macarrão": {
        "descricao": "Massa feita de trigo",
        "unidade": "kg",
        "preco": 6.99,
        "categoria": "Massas"
    },
    "Açúcar": {
        "descricao": "Doçante extraído da cana",
        "unidade": "kg",
        "preco": 4.80,
        "categoria": "Açúcares"
    },
    "Sal": {
        "descricao": "Condimento mineral",
        "unidade": "kg",
        "preco": 2.50,
        "categoria": "Temperos"
    },
    "Óleo de soja": {
        "descricao": "Óleo vegetal para cozinhar",
        "unidade": "litro",
        "preco": 7.90,
        "categoria": "Óleos"
    },
    "Azeite": {
        "descricao": "Óleo extraído da oliva",
        "unidade": "litro",
        "preco": 18.50,
        "categoria": "Óleos"
    },
    "Farinha de trigo": {
        "descricao": "Base para pães e massas",
        "unidade": "kg",
        "preco": 5.60,
        "categoria": "Farinhas"
    },
    "Café": {
        "descricao": "Pó para bebida estimulante",
        "unidade": "kg",
        "preco": 14.90,
        "categoria": "Bebidas"
    },
    "Leite": {
        "descricao": "Bebida de origem animal",
        "unidade": "litro",
        "preco": 4.50,
        "categoria": "Laticínios"
    },
    "Pão francês": {
        "descricao": "Pão tradicional diário",
        "unidade": "unidade",
        "preco": 0.80,
        "categoria": "Padaria"
    },
    "Biscoito recheado": {
        "descricao": "Biscoito doce com recheio",
        "unidade": "pacote",
        "preco": 3.50,
        "categoria": "Doces"
    },
    "Refrigerante": {
        "descricao": "Bebida gaseificada açucarada",
        "unidade": "litro",
        "preco": 8.90,
        "categoria": "Bebidas"
    },
    "Água mineral": {
        "descricao": "Água potável engarrafada",
        "unidade": "litro",
        "preco": 2.00,
        "categoria": "Bebidas"
    },
    "Iogurte": {
        "descricao": "Leite fermentado",
        "unidade": "unidade",
        "preco": 4.90,
        "categoria": "Laticínios"
    },
    "Queijo": {
        "descricao": "Derivado do leite",
        "unidade": "kg",
        "preco": 18.00,
        "categoria": "Laticínios"
    },
    "Presunto": {
        "descricao": "Carne suína processada",
        "unidade": "kg",
        "preco": 6.50,
        "categoria": "Embutidos"
    },
    "Salsicha": {
        "descricao": "Embutido de carne",
        "unidade": "kg",
        "preco": 4.20,
        "categoria": "Embutidos"
    },
    "Carne bovina": {
        "descricao": "Carne de boi",
        "unidade": "kg",
        "preco": 32.00,
        "categoria": "Carnes"
    },
    "Carne de frango": {
        "descricao": "Carne de ave",
        "unidade": "kg",
        "preco": 14.90,
        "categoria": "Carnes"
    },
    "Peixe": {
        "descricao": "Carne de peixe",
        "unidade": "kg",
        "preco": 21.00,
        "categoria": "Carnes"
    },
    "Ovo": {
        "descricao": "Alimento de origem animal",
        "unidade": "dúzia",
        "preco": 12.50,
        "categoria": "Proteínas"
    },
    "Arroz integral": {
        "descricao": "Arroz com casca preservada",
        "unidade": "kg",
        "preco": 7.50,
        "categoria": "Grãos"
    },
    "Feijão preto": {
        "descricao": "Tipo de feijão escuro",
        "unidade": "kg",
        "preco": 5.90,
        "categoria": "Leguminosas"
    },
    "Lentilha": {
        "descricao": "Leguminosa rica em ferro",
        "unidade": "kg",
        "preco": 8.20,
        "categoria": "Leguminosas"
    },
    "Aveia": {
        "descricao": "Cereal nutritivo",
        "unidade": "kg",
        "preco": 7.80,
        "categoria": "Cereais"
    },
    "Banana": {
        "descricao": "Fruta rica em potássio",
        "unidade": "kg",
        "preco": 3.00,
        "categoria": "Frutas"
    },
    "Maçã": {
        "descricao": "Fruta doce e crocante",
        "unidade": "kg",
        "preco": 4.20,
        "categoria": "Frutas"
    },
    "Tomate": {
        "descricao": "Legume usado em saladas",
        "unidade": "kg",
        "preco": 3.80,
        "categoria": "Verduras"
    },
    "Batata": {
        "descricao": "Tubérculo energético",
        "unidade": "kg",
        "preco": 4.00,
        "categoria": "Verduras"
    }
}
itens_2 = [
    "Arroz","Feijão","Macarrão","Açúcar","Sal","Óleo de soja","Azeite",
    "Farinha de trigo","Farinha de milho","Café","Leite","Leite em pó",
    "Achocolatado","Pão francês","Pão de forma","Bolo","Biscoito recheado",
    "Biscoito água e sal","Bolacha cream cracker","Chocolate","Bala",
    "Chiclete","Refrigerante","Suco de caixinha","Água mineral","Cerveja",
    "Vinho","Iogurte","Queijo","Presunto","Mortadela","Salsicha","Linguiça",
    "Carne bovina","Carne de frango","Carne suína","Peixe","Ovo","Manteiga",
    "Margarina","Maionese","Ketchup","Mostarda","Molho de tomate",
    "Extrato de tomate","Milho em conserva","Ervilha em conserva",
    "Atum em lata","Sardinha em lata","Salgadinho","Pipoca",
    "Pipoca de micro-ondas","Sorvete","Gelatina","Pudim","Fermento",
    "Leite condensado","Creme de leite","Arroz integral","Feijão preto",
    "Lentilha","Grão-de-bico","Aveia","Cereal matinal","Mel","Doce de leite",
    "Geleia","Fruta (banana)","Fruta (maçã)","Fruta (laranja)",
    "Verdura (alface)","Verdura (tomate)","Verdura (cebola)",
    "Verdura (batata)","Verdura (cenoura)","Sabão em pó","Detergente",
    "Amaciante","Água sanitária","Desinfetante","Esponja","Papel higiênico",
    "Papel toalha","Guardanapo","Shampoo","Condicionador","Sabonete",
    "Pasta de dente","Escova de dente","Fio dental","Desodorante",
    "Absorvente","Fralda descartável","Ração para cachorro",
    "Ração para gato","Carvão","Fósforo","Vela","Pilha","Isqueiro","lava-Cd100092763afdadaad"
] # veio do arquivo/Loja/loja.py # FAQUE VAR==>
precos_2 = [
    25.90,8.50,6.99,4.80,2.50,7.90,18.50,5.60,4.20,14.90,
    4.50,18.90,7.50,0.80,6.90,12.00,3.50,3.20,3.40,6.80,
    1.50,1.20,8.90,4.50,2.00,5.50,22.00,4.90,18.00,6.50,
    4.80,4.20,9.90,32.00,14.90,19.90,21.00,12.50,9.80,7.90,
    6.50,5.20,4.90,3.80,4.20,5.00,4.80,9.90,8.50,6.00,
    3.50,4.00,5.50,2.80,4.90,6.20,3.90,7.50,5.90,8.20,
    7.80,9.50,6.90,11.90,10.50,7.00,12.90,9.80,3.00,3.50,
    4.20,2.50,3.00,3.80,4.00,15.90,3.20,6.80,4.50,5.90,
    3.00,18.00,6.00,5.50,2.50,7.20,9.90,4.00,12.00,28.00,
    26.00,15.00,4.50,1.20,6.00,7.50,5.00,4.20,3.80,2.00,3.00
]
keys = [
    "KEY_001_A9273738282737282828272726263627272928273728282737ABCDEFGHJKLMNPQRSTUVWXYZ",
    "KEY_002_B8273628192736462819273646281927364628192736QWERTYUIOPASDFGHJK",
    "KEY_003_C9988776655443322110099887766554433221100ZXCVBNMASDFGHJKL",
    "KEY_004_D19283746556473829101928374655647382910ABCDEFGHIJKLMN",
    "KEY_005_EAA11BB22CC33DD44EE55FF6677889900QAZWSXEDCRFVTGB",
    "KEY_006_F1029384756102938475610293847561029384756MNBVCXZLKJHGFDSA",
    "KEY_007_G5647382910564738291056473829105647382910POIUYTREWQLKJH",
    "KEY_008_H88776655443322110099887766554433221100ASDFGHJKLZXCVBNM",
    "KEY_009_I31415926535897932384626433832795028841QWERTYASDF",
    "KEY_010_J27182818284590452353602874713526624977ZXCVBNM",
    "KEY_011_K00112233445566778899AABBCCDDEEFF112233445566",
    "KEY_012_L55667788990011223344556677889900AABBCCDD",
    "KEY_013_MABCDEF1234567890ABCDEF1234567890ABCDEF",
    "KEY_014_NFEDCBA0987654321FEDCBA0987654321FEDCBA",
    "KEY_015_O999888777666555444333222111000AAAABBBB",
    "KEY_016_P135791357913579135791357913579QWERTYUI",
    "KEY_017_Q246802468024680246802468024680ASDFGHJK",
    "KEY_018_R777777777777777777777777777777ZXCVBNM",
    "KEY_019_S888888888888888888888888888888QAZWSX",
    "KEY_020_T123123123123123123123123123123EDCRFV",
    "KEY_021_U321321321321321321321321321321TGBNHY",
    "KEY_022_V456456456456456456456456456456UJMIKO",
    "KEY_023_W654654654654654654654654654654PLKJHG",
    "KEY_024_XABCABCABCABCABCABCABCABCABCABCZXCV",
    "KEY_025_YDEFDEFDEFDEFDEFDEFDEFDEFDEFDEFBNM",
    "KEY_026_Z010101010101010101010101010101QWERT",
    "KEY_027_A020202020202020202020202020202ASDFG",
    "KEY_028_B030303030303030303030303030303ZXCVB",
    "KEY_029_C040404040404040404040404040404NMJKL",
    "KEY_030_D050505050505050505050505050505HGFD",
    "KEY_031_E606060606060606060606060606060QAZ",
    "KEY_032_F707070707070707070707070707070WSX",
    "KEY_033_G808080808080808080808080808080EDC",
    "KEY_034_H909090909090909090909090909090RFV",
    "KEY_035_I111213141516171819202122232425GBN",
    "KEY_036_J262728293031323334353637383940NHY",
    "KEY_037_K414243444546474849505152535455UJM",
    "KEY_038_L565758596061626364656667686970IKO",
    "KEY_039_M717273747576777879808182838485PLK",
    "KEY_040_N868788899091929394959697989910HG",
    "KEY_041_OA1B2C3D4E5F6G7H8I9J0KLMNOPQRST",
    "KEY_042_PTSRQPONMLKJIHGFEDCBA0987654321",
    "KEY_043_QABC123ABC123ABC123ABC123ABC123",
    "KEY_044_RXYZ789XYZ789XYZ789XYZ789XYZ789",
    "KEY_045_SMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT",
    "KEY_046_TTTTSSSSRRRRQQQQPPPPOOOONNNNMMMM",
    "KEY_047_UA9A8A7A6A5A4A3A2A1A0Z9Z8Z7Z6",
    "KEY_048_VZ6Z7Z8Z9Z0A1A2A3A4A5A6A7A8A9",
    "KEY_049_W13572468135724681357246813572468",
    "KEY_050_X86427531864275318642753186427531",
    "KEY_051_YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "KEY_052_ZBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "KEY_053_A12345678901234567890123456789012",
    "KEY_054_B09876543210987654321098765432109",
    "KEY_055_CCAFEBABECAFEBABECAFEBABECAFEBABE",
    "KEY_056_DDEADBEEFDEADBEEFDEADBEEFDEADBEEF",
    "KEY_057_EFACEFEEDFACEFEEDFACEFEEDFACEFEED",
    "KEY_058_FBAADF00DBAADF00DBAADF00DBAADF00D",
    "KEY_059_G0F1E2D3C4B5A69788796A5B4C3D2E1F0",
    "KEY_060_H11235813213455891442333776109871",
    "KEY_061_I31415926535897932384626433832795",
    "KEY_062_J27182818284590452353602874713526",
    "KEY_063_K99999999999999999999999999999999",
    "KEY_064_L88888888888888888888888888888888",
    "KEY_065_M77777777777777777777777777777777",
    "KEY_066_N66666666666666666666666666666666",
    "KEY_067_O55555555555555555555555555555555",
    "KEY_068_P44444444444444444444444444444444",
    "KEY_069_Q33333333333333333333333333333333",
    "KEY_070_R22222222222222222222222222222222",
    "KEY_071_S11111111111111111111111111111111",
    "KEY_072_TABCDEABCDEABCDEABCDEABCDEABCDE",
    "KEY_073_UVWXYZVWXYZVWXYZVWXYZVWXYZ",
    "KEY_074_VQWERTYQWERTYQWERTYQWERTY",
    "KEY_075_WASDFGHASDFGHASDFGHASDFGH",
    "KEY_076_XZXCVBNZXCVBNZXCVBNZXCVBN",
    "KEY_077_YMNBVCXMNBVCXMNBVCXMNBVCX",
    "KEY_078_ZLKJHGFDSALKJHGFDSALKJHG",
    "KEY_079_AQAZWSXEDCQAZWSXEDCQAZWS",
    "KEY_080_BRFVTGBYHNRFVTGBYHNRFVTG",
    "KEY_081_CUJMKIOLPUJMKIOLPUJMKIOL",
    "KEY_082_D123ABC123ABC123ABC123ABC",
    "KEY_083_E789XYZ789XYZ789XYZ789XYZ",
    "KEY_084_FAAA111BBB222CCC333DDD444",
    "KEY_085_G444DDD333CCC222BBB111AAA",
    "KEY_086_HABCDEFFEDCBAABCDEFFEDCBA",
    "KEY_087_I0123456789ABCDEF0123456789AB",
    "KEY_088_JFEDCBA987654321FEDCBA987654",
    "KEY_089_KAAAAAAAA11111111BBBBBBBB",
    "KEY_090_LCCCCCCCC22222222DDDDDDDD",
    "KEY_091_MEEEEEEEE33333333FFFFFFFF",
    "KEY_092_N9999AAAA8888BBBB7777CCCC",
    "KEY_093_OCCCC7777BBBB8888AAAA9999",
    "KEY_094_PABCDEFABCDEFABCDEFABCDEF",
    "KEY_095_QFEDCBAFEDCBAFEDCBAFEDCBA",
    "KEY_096_R123412341234123412341234",
    "KEY_097_S432143214321432143214321",
    "KEY_098_TABCD1234EFGH5678IJKL9012",
    "KEY_099_U2109LKJI8765HGFE4321DCBA",
    "KEY_100_VENDKEYFINAL000111222333444555666"
]
chaves_acesso = [
    "1028277372828199282827372782828272726636272729",
    "9982736462819273646281927364628192736462819273",
    "7726262829926363738272672726262102827737282819",
    "1112223334445556667778889990001112223334445556",
    "9876543210987654321098765432109876543210987654",
    "1234567890123456789012345678901234567890123456",
    "6543210987654321098765432109876543210987654321",
    "1928374655647382910192837465564738291019283746",
    "3141592653589793238462643383279502884197169399",
    "2718281828459045235360287471352662497757247093",
    "1000000000000000000000000000000000000000000001",
    "2000000000000000000000000000000000000000000002",
    "3000000000000000000000000000000000000000000003",
    "4000000000000000000000000000000000000000000004",
    "5000000000000000000000000000000000000000000005",
    "6000000000000000000000000000000000000000000006",
    "7000000000000000000000000000000000000000000007",
    "8000000000000000000000000000000000000000000008",
    "9000000000000000000000000000000000000000000009",
    "0101010101010101010101010101010101010101010101",
    "0202020202020202020202020202020202020202020202",
    "0303030303030303030303030303030303030303030303",
    "0404040404040404040404040404040404040404040404",
    "0505050505050505050505050505050505050505050505",
    "0606060606060606060606060606060606060606060606",
    "0707070707070707070707070707070707070707070707",
    "0808080808080808080808080808080808080808080808",
    "0909090909090909090909090909090909090909090909",
    "1122334455667788990011223344556677889900112233",
    "2233445566778899001122334455667788990011223344",
    "3344556677889900112233445566778899001122334455",
    "4455667788990011223344556677889900112233445566",
    "5566778899001122334455667788990011223344556677",
    "6677889900112233445566778899001122334455667788",
    "7788990011223344556677889900112233445566778899",
    "8899001122334455667788990011223344556677889900",
    "9990001112223334445556667778889990001112223334",
    "1357913579135791357913579135791357913579135791",
    "2468024680246802468024680246802468024680246802",
    "1212121212121212121212121212121212121212121212",
    "3434343434343434343434343434343434343434343434",
    "5656565656565656565656565656565656565656565656",
    "7878787878787878787878787878787878787878787878",
    "9090909090909090909090909090909090909090909090",
    "1111111111111111111111111111111111111111111111",
    "2222222222222222222222222222222222222222222222",
    "3333333333333333333333333333333333333333333333",
    "4444444444444444444444444444444444444444444444",
    "5555555555555555555555555555555555555555555555",
    "6666666666666666666666666666666666666666666666",
    "7777777777777777777777777777777777777777777777",
    "8888888888888888888888888888888888888888888888",
    "9999999999999999999999999999999999999999999999",
    "1010101010101010101010101010101010101010101010",
    "2020202020202020202020202020202020202020202020",
    "3030303030303030303030303030303030303030303030",
    "4040404040404040404040404040404040404040404040",
    "5050505050505050505050505050505050505050505050",
    "6060606060606060606060606060606060606060606060",
    "7070707070707070707070707070707070707070707070",
    "8080808080808080808080808080808080808080808080",
    "9091919191919191919191919191919191919191919191",
    "9191919191919191919191919191919191919191919191",
    "8282828282828282828282828282828282828282828282",
    "7373737373737373737373737373737373737373737373",
    "6464646464646464646464646464646464646464646464",
    "5554443332221110009998887776665554443332221110",
    "0001112223334445556667778889990001112223334445",
    "1213141516171819202122232425262728293031323334",
    "3433323130292827262524232221201918171615141312",
    "9098765432101234567890987654321012345678909876",
    "5678901234567890123456789012345678901234567890",
    "1123581321345589144233377610987159725844181676",
    "8675309867530986753098675309867530986753098675",
    "9998887776665554443332221110009998887776665554",
    "1231231231231231231231231231231231231231231231",
    "3213213213213213213213213213213213213213213213",
    "1472583691472583691472583691472583691472583691",
    "9638527419638527419638527419638527419638527419"
]

