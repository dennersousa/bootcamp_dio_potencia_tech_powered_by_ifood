valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


def conta(valorHamburguer,quantidadeHamburguer,valorBebida,quantidadeBebida,valorPago):
  vHamburguer = valorHamburguer * quantidadeHamburguer
  vBebida = valorBebida * quantidadeBebida
  precoFinal = vHamburguer + vBebida
  troco = valorPago - precoFinal
  return print(f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}.")

conta(valorHamburguer,quantidadeHamburguer,valorBebida,quantidadeBebida,valorPago)
