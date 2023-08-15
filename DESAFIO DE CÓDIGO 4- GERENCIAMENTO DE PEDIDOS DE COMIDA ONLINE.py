def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
      
    cupom = input()
    if cupom == "10%":
        total *= 0.9
    elif cupom == "20%":
        total *= 0.8
 
    print(f"Valor total: {total:.2f}")
 
if __name__ == "__main__":
    main()
