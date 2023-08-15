numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input() == "s"
    tipo_vegano = "Vegano" if ehVegano else "Nao-vegano"

    print(f"Pedido {i}: {prato} ({tipo_vegano}) - {calorias} calorias")
