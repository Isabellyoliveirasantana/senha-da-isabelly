#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Testes para o Gerador de Senhas
Valida todas as funções e exibe relatório de testes
"""

import sys
from geracao_senhas import GeradorSenhas


class TestadorSenhas:
    """
    Classe para testar o gerador de senhas.
    """

    def __init__(self):
        """Inicializa o testador."""
        self.gerador = GeradorSenhas()
        self.testes_passados = 0
        self.testes_falhados = 0

    def teste_fibonacci(self):
        """
        Testa a geração de Fibonacci.
        """
        print("\n🧪 Testando Fibonacci...")
        try:
            senha = self.gerador.gerar_fibonacci(10)
            
            # Validações
            assert isinstance(senha, str), "Resultado deve ser string"
            assert len(senha) > 0, "Resultado não pode estar vazio"
            assert '-' in senha, "Resultado deve conter hífen"
            
            partes = senha.split('-')
            assert len(partes) == 10, "Deve ter 10 números"
            
            # Verificar sequência Fibonacci
            numeros = [int(x) for x in partes]
            for i in range(2, len(numeros)):
                assert numeros[i] == numeros[i-1] + numeros[i-2], \
                    f"Posição {i} não segue Fibonacci"
            
            print(f"   ✅ Teste PASSOU")
            print(f"   Resultado: {senha}")
            self.testes_passados += 1
            
        except AssertionError as e:
            print(f"   ❌ Teste FALHOU: {e}")
            self.testes_falhados += 1
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            self.testes_falhados += 1

    def teste_primos(self):
        """
        Testa a geração de números primos.
        """
        print("\n🧪 Testando Números Primos...")
        try:
            senha = self.gerador.gerar_primos(10)
            
            # Validações
            assert isinstance(senha, str), "Resultado deve ser string"
            assert len(senha) > 0, "Resultado não pode estar vazio"
            assert '-' in senha, "Resultado deve conter hífen"
            
            partes = senha.split('-')
            assert len(partes) == 10, "Deve ter 10 números"
            
            # Verificar se todos são primos
            def eh_primo(num):
                if num < 2:
                    return False
                if num == 2:
                    return True
                if num % 2 == 0:
                    return False
                for i in range(3, int(num**0.5) + 1, 2):
                    if num % i == 0:
                        return False
                return True
            
            numeros = [int(x) for x in partes]
            for num in numeros:
                assert eh_primo(num), f"{num} não é primo"
            
            print(f"   ✅ Teste PASSOU")
            print(f"   Resultado: {senha}")
            self.testes_passados += 1
            
        except AssertionError as e:
            print(f"   ❌ Teste FALHOU: {e}")
            self.testes_falhados += 1
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            self.testes_falhados += 1

    def teste_caesar_md5(self):
        """
        Testa a geração Caesar + MD5.
        """
        print("\n🧪 Testando Caesar + MD5...")
        try:
            senha = self.gerador.gerar_caesar_md5()
            
            # Validações
            assert isinstance(senha, str), "Resultado deve ser string"
            assert len(senha) == 32, "MD5 deve ter 32 caracteres"
            assert all(c in '0123456789abcdef' for c in senha), \
                "Deve ser hexadecimal"
            
            print(f"   ✅ Teste PASSOU")
            print(f"   Resultado (primeiros 20 chars): {senha[:20]}...")
            print(f"   Comprimento: {len(senha)} caracteres")
            self.testes_passados += 1
            
        except AssertionError as e:
            print(f"   ❌ Teste FALHOU: {e}")
            self.testes_falhados += 1
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            self.testes_falhados += 1

    def teste_sha256_salt(self):
        """
        Testa a geração SHA-256 + Salt.
        """
        print("\n🧪 Testando SHA-256 + Salt...")
        try:
            senha = self.gerador.gerar_sha256_com_salt()
            
            # Validações
            assert isinstance(senha, str), "Resultado deve ser string"
            assert len(senha) == 64, "SHA-256 deve ter 64 caracteres"
            assert all(c in '0123456789abcdef' for c in senha), \
                "Deve ser hexadecimal"
            
            # Testar randomicidade (duas chamadas devem ser diferentes)
            senha2 = self.gerador.gerar_sha256_com_salt()
            assert senha != senha2, "Salt deve gerar resultados diferentes"
            
            print(f"   ✅ Teste PASSOU")
            print(f"   Resultado 1 (primeiros 20 chars): {senha[:20]}...")
            print(f"   Resultado 2 (primeiros 20 chars): {senha2[:20]}...")
            print(f"   ✓ Hashes diferentes (salt aleatório funcionando)")
            print(f"   Comprimento: {len(senha)} caracteres")
            self.testes_passados += 1
            
        except AssertionError as e:
            print(f"   ❌ Teste FALHOU: {e}")
            self.testes_falhados += 1
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            self.testes_falhados += 1

    def teste_todas_senhas(self):
        """
        Testa a geração de todas as senhas juntas.
        """
        print("\n🧪 Testando Geração de Todas as Senhas...")
        try:
            senhas = self.gerador.gerar_todas_senhas()
            
            # Validações
            assert isinstance(senhas, dict), "Resultado deve ser dicionário"
            assert len(senhas) == 4, "Deve ter 4 senhas diferentes"
            
            for chave, dados in senhas.items():
                assert 'senha' in dados, f"{chave} sem 'senha'"
                assert 'nome' in dados, f"{chave} sem 'nome'"
                assert 'seguranca' in dados, f"{chave} sem 'seguranca'"
                assert isinstance(dados['senha'], str), \
                    f"{chave} senha não é string"
            
            print(f"   ✅ Teste PASSOU")
            print(f"   Total de senhas geradas: {len(senhas)}")
            self.testes_passados += 1
            
        except AssertionError as e:
            print(f"   ❌ Teste FALHOU: {e}")
            self.testes_falhados += 1
        except Exception as e:
            print(f"   ❌ Erro: {e}")
            self.testes_falhados += 1

    def executar_todos_testes(self):
        """
        Executa todos os testes.
        """
        print("\n" + "="*60)
        print("🧪 EXECUTANDO TESTES DO GERADOR DE SENHAS")
        print("="*60)
        
        self.teste_fibonacci()
        self.teste_primos()
        self.teste_caesar_md5()
        self.teste_sha256_salt()
        self.teste_todas_senhas()
        
        # Relatório final
        print("\n" + "="*60)
        print("📊 RELATÓRIO DE TESTES")
        print("="*60)
        print(f"✅ Testes Passados: {self.testes_passados}")
        print(f"❌ Testes Falhados: {self.testes_falhados}")
        print(f"📈 Taxa de Sucesso: {(self.testes_passados/5)*100:.1f}%")
        print("="*60 + "\n")
        
        if self.testes_falhados == 0:
            print("🎉 TODOS OS TESTES PASSARAM!\n")
            return 0
        else:
            print(f"⚠️  {self.testes_falhados} teste(s) falharam.\n")
            return 1


def main():
    """
    Função principal.
    """
    testador = TestadorSenhas()
    resultado = testador.executar_todos_testes()
    sys.exit(resultado)


if __name__ == "__main__":
    main()
