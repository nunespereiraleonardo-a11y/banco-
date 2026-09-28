
ENZO SOARES PEDRO
12:10 (há 0 minuto)
para mim

class Conta:

    def __init__(self, titular, senha, saldo_inicial=0):
        self.titular = titular
        self._senha = str(senha)
        self._saldo = saldo_inicial
        self._tentativas_senha = 0  # Contador de erros de senha
        self._bloqueada = False     # Estado da conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def esta_bloqueada(self):
        return self._bloqueada

    def validar_senha(self, senha_digitada):
        """Verifica a senha e bloqueia a conta se errar 3 vezes seguidas."""
        if self._bloqueada:
            print("\n⛔ CONTA BLOQUEADA! Dirija-se a uma agência para desbloquear.")
            return False

        if str(senha_digitada) == self._senha:
            self._tentativas_senha = 0  # Reseta o contador ao acertar
            return True
        else:
            self._tentativas_senha += 1
            tentativas_restantes = 3 - self._tentativas_senha

            if self._tentativas_senha >= 3:
                self._bloqueada = True
                print("\n⛔ Senha incorreta 3 vezes! A CONTA FOI BLOQUEADA por segurança.")
            else:
                print(f"\n❌ Senha incorreta! Você tem mais {tentativas_restantes} tentativa(s).")
           
            return False

    def sacar(self, valor, senha_digitada):
        if not self.validar_senha(senha_digitada):
            return False

        if valor <= 0:
            print("\n❌ O valor do saque deve ser maior que zero.")
            return False
        if valor > self._saldo:
            print("\n❌ Saldo insuficiente.")
            return False

        self._saldo -= valor
        print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        if self._bloqueada:
            print("\n⛔ Operação cancelada. A conta está bloqueada.")
            return False

        if valor <= 0:
            print("\n❌ O valor do depósito deve ser maior que zero.")
            return False

        self._saldo += valor
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True

    def ver_saldo(self, senha_digitada):
        if not self.validar_senha(senha_digitada):
            return False

        print(f"\n💵 Saldo atual de {self.titular}: R$ {self._saldo:.2f}")
        return True


# --- Execução do Programa Interativo ---
def main():
    print("=== BEM-VINDO AO BANCO PYTHON ===")
    nome = input("Digite o nome do titular da conta: ").strip()

    while True:
        senha = input("Crie uma senha para sua conta: ").strip()
        if len(senha) > 0:
            break
        print("A senha não pode ser vazia.")

    while True:
        try:
            saldo_ini = float(input("Digite o saldo inicial (R$): "))
            if saldo_ini < 0:
                print("O saldo inicial não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.")

    conta = Conta(nome, senha, saldo_ini)

    while True:
        # Se a conta for bloqueada durante o uso, encerra o loop de operações
        if conta.esta_bloqueada:
            print("\n" + "=" * 30)
            print("Sua conta está bloqueada. Programa encerrado.")
            print("=" * 30)
            break

        print("\n" + "=" * 30)
        print("      MENU DE OPÇÕES")
        print("=" * 30)
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            senha_digitada = input("Digite sua senha: ")
            conta.ver_saldo(senha_digitada)

        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("\n❌ Erro: Digite um valor numérico válido.")

        elif opcao == "3":
            try:
                valor = float(input("Digite o valor para saque: R$ "))
                senha_digitada = input("Digite sua senha para confirmar: ")
                conta.sacar(valor, senha_digitada)
            except ValueError:
                print("\n❌ Erro: Digite um valor numérico válido.")

        elif opcao == "4":
            print(
                f"\nObrigado por utilizar nossos serviços, {conta.titular}!"
            )
            break

        else:
            print("\n❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

