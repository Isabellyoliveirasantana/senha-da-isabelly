#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Geração de Senhas Seguras usando Matemática
Projeto: Segurança Digital - Matemática para Programar Senhas Seguras
Autor: Isabelly Oliveira Santana
"""

import hashlib
import os
import string
from datetime import datetime


class GeradorSenhas:
    """
    Classe para gerar senhas seguras utilizando diferentes estratégias matemáticas.
    """

    def __init__(self):
        """Inicializa o gerador de senhas."""
        self.senhas = {}
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def gerar_fibonacci(self, quantidade=10):
        """
        Gera senha baseada na sequência de Fibonacci.
        
        Matemática:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)
        
        Args:
            quantidade (int): Quantidade de números Fibonacci a gerar
            
        Returns:
            str: Senha gerada com padrão Fibonacci
        """
        fibonacci = [0, 1]
        
        # Gerar sequência de Fibonacci
        for i in range(2, quantidade):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        
        # Converter para string
        senha = '-'.join(map(str, fibonacci[:quantidade]))
        
        return senha

    def gerar_primos(self, quantidade=10):
        """
        Gera senha baseada em números primos.
        
        Matemática:
        Números primos são naturais maiores que 1 divisíveis apenas por 1 e por si mesmos.
        Fundamentais em criptografia moderna (RSA, etc)
        
        Args:
            quantidade (int): Quantidade de números primos a gerar
            
        Returns:
            str: Senha gerada com padrão de números primos
        """
        def eh_primo(num):
            """Verifica se um número é primo."""
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
        
        primos = []
        num = 2
        
        # Encontrar números primos
        while len(primos) < quantidade:
            if eh_primo(num):
                primos.append(num)
            num += 1
        
        # Converter para string
        senha = '-'.join(map(str, primos))
        
        return senha

    def gerar_caesar_md5(self, texto="SENHASEGURA", deslocamento=3):
        """
        Gera senha usando Cifra de Caesar + Hashing MD5.
        
        Matemática:
        1. Cifra de Caesar: C = (P + k) mod 26
           - P: posição do caractere (0-25)
           - k: deslocamento (chave)
           - C: caractere cifrado
        
        2. MD5: Função hash criptográfica (128 bits)
        
        Args:
            texto (str): Texto base para criptografia
            deslocamento (int): Chave para a cifra de Caesar
            
        Returns:
            str: Senha com Caesar+MD5
        """
        # Aplicar Cifra de Caesar
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                # Determinar se é maiúscula ou minúscula
                base = ord('A') if char.isupper() else ord('a')
                # Aplicar deslocamento
                posicao = ord(char) - base
                nova_posicao = (posicao + deslocamento) % 26
                texto_cifrado += chr(base + nova_posicao)
            else:
                texto_cifrado += char
        
        # Aplicar MD5
        hash_md5 = hashlib.md5(texto_cifrado.encode()).hexdigest()
        
        return hash_md5

    def gerar_sha256_com_salt(self, base_text="SENHASEGURA"):
        """
        Gera senha usando SHA-256 com salt aleatório.
        
        Matemática:
        SHA-256: Algoritmo de hash criptográfico que gera 256 bits de saída
        Salt: Valor aleatório para aumentar segurança
        Processo: hash = SHA-256(salt + password)
        
        Args:
            base_text (str): Texto base para hash
            
        Returns:
            str: Senha hash SHA-256 com salt
        """
        # Gerar salt aleatório (16 bytes)
        salt = os.urandom(16)
        
        # Combinar salt + texto
        salted_text = salt + base_text.encode()
        
        # Aplicar SHA-256
        hash_sha256 = hashlib.sha256(salted_text).hexdigest()
        
        return hash_sha256

    def gerar_todas_senhas(self):
        """
        Gera todas as 4 senhas diferentes.
        
        Returns:
            dict: Dicionário com as 4 senhas e seus níveis de segurança
        """
        self.senhas = {
            "1_fibonacci": {
                "senha": self.gerar_fibonacci(10),
                "nome": "Fibonacci",
                "seguranca": "⭐⭐ Média",
                "descricao": "Baseada em sequência matemática",
                "formula": "F(n) = F(n-1) + F(n-2)"
            },
            "2_primos": {
                "senha": self.gerar_primos(10),
                "nome": "Números Primos",
                "seguranca": "⭐⭐ Média",
                "descricao": "Baseada em teoria dos números",
                "formula": "Números divisíveis apenas por 1 e por si mesmos"
            },
            "3_caesar_md5": {
                "senha": self.gerar_caesar_md5(),
                "nome": "Caesar + MD5",
                "seguranca": "⭐⭐⭐ Média-Alta",
                "descricao": "Criptografia clássica + hashing",
                "formula": "C = (P + k) mod 26, depois MD5()"
            },
            "4_sha256_salt": {
                "senha": self.gerar_sha256_com_salt(),
                "nome": "SHA-256 + Salt",
                "seguranca": "⭐⭐⭐⭐⭐ Alta (Recomendada)",
                "descricao": "Criptografia moderna com salt aleatório",
                "formula": "SHA-256(salt + password)"
            }
        }
        
        return self.senhas

    def exibir_senhas(self):
        """
        Exibe as senhas geradas de forma formatada no console.
        """
        print("\n" + "="*60)
        print("🔐 SEGURANÇA DIGITAL: MATEMÁTICA PARA SENHAS SEGURAS")
        print("="*60)
        print(f"\n📅 Data/Hora: {self.timestamp}")
        print(f"👤 Autor: Isabelly Oliveira Santana")
        print("\n" + "-"*60)
        
        for chave, dados in self.senhas.items():
            numero = chave[0]
            print(f"\n{numero}️⃣  SENHA {dados['nome'].upper()}")
            print("-" * 60)
            print(f"   📝 Senha Gerada:")
            print(f"      {dados['senha']}")
            print(f"\n   📊 Nível de Segurança: {dados['seguranca']}")
            print(f"   📖 Descrição: {dados['descricao']}")
            print(f"   📐 Fórmula: {dados['formula']}")
        
        print("\n" + "="*60)
        print("💡 RECOMENDAÇÃO:")
        print("   Use a Senha 4 (SHA-256 + Salt) para máxima segurança!")
        print("   Combine com maiúsculas, minúsculas, números e símbolos.")
        print("="*60 + "\n")

    def salvar_resultado(self, nome_arquivo="resultados/senhas_geradas.txt"):
        """
        Salva as senhas geradas em um arquivo de texto.
        
        Args:
            nome_arquivo (str): Caminho do arquivo para salvar
        """
        # Criar diretório se não existir
        diretorio = os.path.dirname(nome_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("🔐 SEGURANÇA DIGITAL: SENHAS GERADAS\n")
            f.write("="*60 + "\n")
            f.write(f"Data/Hora: {self.timestamp}\n")
            f.write(f"Autor: Isabelly Oliveira Santana\n")
            f.write("\n" + "-"*60 + "\n")
            
            for chave, dados in self.senhas.items():
                numero = chave[0]
                f.write(f"\n{numero}. SENHA {dados['nome'].upper()}\n")
                f.write("-" * 60 + "\n")
                f.write(f"Senha: {dados['senha']}\n")
                f.write(f"Segurança: {dados['seguranca']}\n")
                f.write(f"Descrição: {dados['descricao']}\n")
                f.write(f"Fórmula: {dados['formula']}\n")
            
            f.write("\n" + "="*60 + "\n")
            f.write("RECOMENDAÇÕES DE SEGURANÇA:\n")
            f.write("- Use SHA-256 + Salt para máxima proteção\n")
            f.write("- Mínimo 12 caracteres em senhas reais\n")
            f.write("- Combine: maiúsculas, minúsculas, números, símbolos\n")
            f.write("- Nunca reutilize senhas\n")
            f.write("- Use gerenciador de senhas\n")
            f.write("="*60 + "\n")
        
        print(f"✅ Resultado salvo em: {nome_arquivo}")


def main():
    """
    Função principal - executa o programa completo.
    """
    print("\n🚀 Iniciando gerador de senhas seguras...")
    
    # Criar instância do gerador
    gerador = GeradorSenhas()
    
    # Gerar todas as senhas
    print("⏳ Gerando senhas...")
    gerador.gerar_todas_senhas()
    
    # Exibir senhas no console
    gerador.exibir_senhas()
    
    # Salvar em arquivo
    gerador.salvar_resultado()
    
    print("✅ Programa concluído com sucesso!")


if __name__ == "__main__":
    main()
