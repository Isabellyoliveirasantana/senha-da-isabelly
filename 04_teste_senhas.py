#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Teste de Força de Senhas
Valida e analisa a força das senhas geradas
"""

import re
from typing import Tuple


class TestadorSenha:
    """
    Classe para testar e validar a força de senhas.
    """
    
    def __init__(self):
        """Inicializa os padrões regex para análise."""
        self.padrao_minusculas = re.compile(r'[a-z]')
        self.padrao_maiusculas = re.compile(r'[A-Z]')
        self.padrao_numeros = re.compile(r'\d')
        self.padrao_especiais = re.compile(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]')
        self.padrao_sequencial = re.compile(r'(.)\1{2,}')
        self.padrao_alfabetico = re.compile(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', re.IGNORECASE)
    
    def tem_minusculas(self, senha: str) -> bool:
        """Verifica se a senha tem letras minúsculas."""
        return bool(self.padrao_minusculas.search(senha))
    
    def tem_maiusculas(self, senha: str) -> bool:
        """Verifica se a senha tem letras maiúsculas."""
        return bool(self.padrao_maiusculas.search(senha))
    
    def tem_numeros(self, senha: str) -> bool:
        """Verifica se a senha tem números."""
        return bool(self.padrao_numeros.search(senha))
    
    def tem_especiais(self, senha: str) -> bool:
        """Verifica se a senha tem caracteres especiais."""
        return bool(self.padrao_especiais.search(senha))
    
    def tem_caracteres_repetidos(self, senha: str) -> bool:
        """Verifica se há 3+ caracteres iguais em sequência."""
        return bool(self.padrao_sequencial.search(senha))
    
    def tem_sequencia_alfabetica(self, senha: str) -> bool:
        """Verifica se há 3+ caracteres sequenciais do alfabeto."""
        return bool(self.padrao_alfabetico.search(senha))
    
    def calcular_pontuacao(self, senha: str) -> Tuple[int, str]:
        """
        Calcula a pontuação de força de uma senha (0-100).
        
        Args:
            senha: A senha a ser testada
        
        Returns:
            Tupla (pontuação, classificação)
        """
        pontuacao = 0
        
        # Comprimento (máx 30 pontos)
        comprimento = len(senha)
        if comprimento >= 8:
            pontuacao += 10
        if comprimento >= 12:
            pontuacao += 10
        if comprimento >= 16:
            pontuacao += 10
        
        # Tipos de caracteres (máx 40 pontos)
        if self.tem_minusculas(senha):
            pontuacao += 10
        if self.tem_maiusculas(senha):
            pontuacao += 10
        if self.tem_numeros(senha):
            pontuacao += 10
        if self.tem_especiais(senha):
            pontuacao += 10
        
        # Penalidades (máx -20 pontos)
        if self.tem_caracteres_repetidos(senha):
            pontuacao -= 10
        if self.tem_sequencia_alfabetica(senha):
            pontuacao -= 10
        
        # Garantir que fica entre 0 e 100
        pontuacao = max(0, min(100, pontuacao))
        
        # Classificação
        if pontuacao < 25:
            classificacao = "🔴 Muito Fraca"
        elif pontuacao < 50:
            classificacao = "🟠 Fraca"
        elif pontuacao < 75:
            classificacao = "🟡 Média"
        elif pontuacao < 90:
            classificacao = "🟢 Forte"
        else:
            classificacao = "🟢🟢 Muito Forte"
        
        return pontuacao, classificacao
    
    def gerar_relatorio(self, senha: str) -> str:
        """
        Gera um relatório completo de análise da senha.
        
        Args:
            senha: A senha a ser analisada
        
        Returns:
            Relatório formatado
        """
        pontuacao, classificacao = self.calcular_pontuacao(senha)
        
        relatorio = []
        relatorio.append("\n" + "="*60)
        relatorio.append("📋 RELATÓRIO DE ANÁLISE DE SENHA")
        relatorio.append("="*60)
        relatorio.append(f"\n🔑 Senha: {senha}")
        relatorio.append(f"\n📊 PONTUAÇÃO: {pontuacao}/100")
        relatorio.append(f"   Classificação: {classificacao}")
        relatorio.append(f"\n✅ CARACTERÍSTICAS:")
        relatorio.append(f"   Comprimento: {len(senha)} caracteres")
        relatorio.append(f"   Letras minúsculas (a-z): {'✓' if self.tem_minusculas(senha) else '✗'}")
        relatorio.append(f"   Letras maiúsculas (A-Z): {'✓' if self.tem_maiusculas(senha) else '✗'}")
        relatorio.append(f"   Números (0-9): {'✓' if self.tem_numeros(senha) else '✗'}")
        relatorio.append(f"   Caracteres especiais: {'✓' if self.tem_especiais(senha) else '✗'}")
        relatorio.append(f"\n⚠️  PROBLEMAS:")
        relatorio.append(f"   Caracteres repetidos (3+): {'✗ Sim (problema)' if self.tem_caracteres_repetidos(senha) else '✓ Não'}")
        relatorio.append(f"   Sequência alfabética (3+): {'✗ Sim (problema)' if self.tem_sequencia_alfabetica(senha) else '✓ Não'}")
        relatorio.append(f"\n💡 RECOMENDAÇÕES:")
        
        recomendacoes = []
        if len(senha) < 12:
            recomendacoes.append("   - Aumente o comprimento para pelo menos 12 caracteres")
        if not self.tem_maiusculas(senha):
            recomendacoes.append("   - Adicione letras maiúsculas")
        if not self.tem_numeros(senha):
            recomendacoes.append("   - Adicione números")
        if not self.tem_especiais(senha):
            recomendacoes.append("   - Adicione caracteres especiais (!@#$%^&*)")
        
        if recomendacoes:
            for rec in recomendacoes:
                relatorio.append(rec)
        else:
            relatorio.append("   ✓ Nenhuma recomendação - Senha excelente!")
        
        relatorio.append("\n" + "="*60)
        
        return "\n".join(relatorio)


def main():
    """
    Função principal: Testa as senhas geradas.
    """
    testador = TestadorSenha()
    
    print("\n" + "="*60)
    print("🧪 TESTADOR DE FORÇA DE SENHAS")
    print("Validação das senhas geradas no projeto")
    print("="*60)
    
    # Exemplos de senhas para teste
    senhas_exemplo = [
        "abc123",           # Muito fraca
        "Senha123",         # Fraca
        "P@ssw0rd2024",     # Média
        "7KmP$xQ!wN2vL5",   # Forte
        "eMx9%Qr@4nK2pL!8sJ#"  # Muito forte
    ]
    
    print("\n📝 Testando senhas de exemplo:\n")
    for senha in senhas_exemplo:
        print(testador.gerar_relatorio(senha))
    
    print("\n✅ Testes concluídos!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
