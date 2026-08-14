valor_da_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))
troco = valor_pago - valor_da_compra
print(f"Seu troco é: R$ {troco:.2f}")