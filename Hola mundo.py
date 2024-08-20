#Compra camisa tipo polo descuento 5%
#Compra superior a 200.000 descuesto del 30%
#Total a pagar y total de descuento (ahorro)

Jeans = 125000
Camisas = 45000
Tipo_Polo = 30000

compra = Jeans * 2 + Camisas * 2 + Tipo_Polo

if Tipo_Polo >= 30000:
    descuento = 0.05 * Tipo_Polo
    
if compra >= 300000:
    descuento = 0.30 * compra
    
descuento = 0.05 * Tipo_Polo + 0.30 * compra
    
print("Total a pagar: ", compra - descuento)
print("Total descuento:", descuento)