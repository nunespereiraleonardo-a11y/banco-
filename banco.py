class Conta:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= 0: 
            print("O valor do saque deve ser maior que zero.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}") 
    def transferencia (self, valor)
  if valor <= 0:
    print("O valor de transferencia deve ser maior que zero.")
    else:
  self.saldo += valor
print 

  
