#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Projeto: Segurança Digital - Gerador de Senhas Seguras com Matemática
Autor: Isabelly Oliveira Santana
Descrição: Implementação de gerador de senhas seguras usando conceitos matemáticos
"""

import secrets
import string
import math
from datetime import datetime
from typing import List, Tuple


class GeradorSenhaSegura:
    """
    Classe para gerar e analisar senhas seguras usando matemática e criptografia.
    """
    
    def __init__(self):
        """Inicializa os conjuntos de caracteres disponíveis."""
        self.digitos = string.digits  # 0-9
        self.minusculas = string.ascii_lowercase  # a-z
        self.maiusculas = string.ascii_uppercase  # A-Z
        self.especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Caracteres especiais
        self.todos_caracteres = (
            self.digitos + self.minusculas + self.maiusculas + self.especiais
        )
    
    def calcular_entropia(self, tamanho_alfabeto: int, comprimento: int) -> float:
        """
        Calcula a entropia de uma senha usando a fórmula de Shannon.
        
        Fórmula: H = log₂(tamanho_alfabeto^comprimento)
        
        Args:
            tamanho_alfabeto: Número de caracteres diferentes disponíveis
            comprimento: Comprimento da senha em caracteres
        
        Returns:
            Entropia em bits
        """
        combinacoes = tamanho_alfabeto ** comprimento
        entropia = math.log2(combinacoes)
        return entropia
    
    def calcular_combinacoes(self, tamanho_alfabeto: int, comprimento: int) -> float:
        """
        Calcula o número de combinações possíveis.
        
        Fórmula: C = m^n
        
        Args:
            tamanho_alfabeto: m (número de caracteres diferentes)
            comprimento: n (comprimento da senha)
        
        Returns:
            Número de combinações possíveis
        """
        return tamanho_alfabeto ** comprimento
    
    def calcular_tempo_forca_bruta(self, combinacoes: float, 
                                   tentativas_por_segundo: float = 1e9) -> str:
        """
        Calcula o tempo aproximado para quebrar uma senha por força bruta.
        
        Fórmula: Tempo = (Combinações / 2) / Tentativas por Segundo
        (dividimos por 2 porque em média quebra na metade)
        
        Args:
            combinacoes: Número total de combinações possíveis
            tentativas_por_segundo: Velocidade de teste (padrão: 1 bilhão/segundo)
        
        Returns:
            String formatada com o tempo estimado
        """
        tempo_segundos = (combinacoes / 2) / tentativas_por_segundo
        
        # Converter para unidades legíveis
        if tempo_segundos < 1:
            return f"{tempo_segundos:.3f} segundos"
        elif tempo_segundos < 60:
            return f"{tempo_segundos:.2f} segundos"
        elif tempo_segundos < 3600:
            minutos = tempo_segundos / 60
            return f"{minutos:.2f} minutos"
        elif tempo_segundos < 86400:
            horas = tempo_segundos / 3600
            return f"{horas:.2f} horas"
        elif tempo_segundos < 31536000:
            dias = tempo_segundos / 86400
            return f"{dias:.2f} dias"
        else:
            anos = tempo_segundos / 31536000
            return f"{anos:.2e} anos"
    
    def classificar_forca(self, entropia: float) -> str:
        """
        Classifica a força de uma senha baseado em sua entropia.
        
        Args:
            entropia: Entropia em bits
        
        Returns:
            Classificação da força
        """
        if entropia < 30:
            return "🔴 Muito Fraca"
        elif entropia < 50:
            return "🟠 Fraca"
        elif entropia < 80:
            return "🟡 Média"
        elif entropia < 120:
            return "🟢 Forte"
        else:
            return "🟢🟢 Muito Forte"
    
    def gerar_senha_tipo_1(self) -> Tuple[str, dict]:
        """
        Gera uma senha do Tipo 1: Caracteres aleatórios (16 caracteres)
        Segue padrão: Alta aleatoriedade, sem estrutura fixa
        """
        comprimento = 16
        senha = ''.join(secrets.choice(self.todos_caracteres) for _ in range(comprimento))
        
        tamanho_alfabeto = len(self.todos_caracteres)
        combinacoes = self.calcular_combinacoes(tamanho_alfabeto, comprimento)
        entropia = self.calcular_entropia(tamanho_alfabeto, comprimento)
        tempo = self.calcular_tempo_forca_bruta(combinacoes)
        
        return senha, {
            'tipo': 'Caracteres Aleatórios',
            'comprimento': comprimento,
            'tamanho_alfabeto': tamanho_alfabeto,
            'combinacoes': combinacoes,
            'entropia': entropia,
            'tempo_forca_bruta': tempo,
            'classificacao': self.classificar_forca(entropia)
        }
    
    def gerar_senha_tipo_2(self) -> Tuple[str, dict]:
        """
        Gera uma senha do Tipo 2: Com padrão de distribuição (18 caracteres)
        Garante mistura de maiúsculas, minúsculas, números e símbolos
        """
        comprimento = 18
        
        # Garantir pelo menos um de cada tipo
        senha_chars = [
            secrets.choice(self.maiusculas),
            secrets.choice(self.minusculas),
            secrets.choice(self.digitos),
            secrets.choice(self.especiais)
        ]
        
        # Preencher o resto com caracteres aleatórios
        for _ in range(comprimento - len(senha_chars)):
            senha_chars.append(secrets.choice(self.todos_caracteres))
        
        # Embaralhar para evitar padrões óbvios
        secrets.SystemRandom().shuffle(senha_chars)
        senha = ''.join(senha_chars)
        
        tamanho_alfabeto = len(self.todos_caracteres)
        combinacoes = self.calcular_combinacoes(tamanho_alfabeto, comprimento)
        entropia = self.calcular_entropia(tamanho_alfabeto, comprimento)
        tempo = self.calcular_tempo_forca_bruta(combinacoes)
        
        return senha, {
            'tipo': 'Com Padrão de Distribuição',
            'comprimento': comprimento,
            'tamanho_alfabeto': tamanho_alfabeto,
            'combinacoes': combinacoes,
            'entropia': entropia,
            'tempo_forca_bruta': tempo,
            'classificacao': self.classificar_forca(entropia)
        }
    
    def gerar_senha_tipo_3(self) -> Tuple[str, dict]:
        """
        Gera uma senha do Tipo 3: Passphrase (24 caracteres)
        Comprimento maior para máxima segurança
        """
        comprimento = 24
        senha = ''.join(secrets.choice(self.todos_caracteres) for _ in range(comprimento))
        
        tamanho_alfabeto = len(self.todos_caracteres)
        combinacoes = self.calcular_combinacoes(tamanho_alfabeto, comprimento)
        entropia = self.calcular_entropia(tamanho_alfabeto, comprimento)
        tempo = self.calcular_tempo_forca_bruta(combinacoes)
        
        return senha, {
            'tipo': 'Passphrase',
            'comprimento': comprimento,
            'tamanho_alfabeto': tamanho_alfabeto,
            'combinacoes': combinacoes,
            'entropia': entropia,
            'tempo_forca_bruta': tempo,
            'classificacao': self.classificar_forca(entropia)
        }
    
    def gerar_senha_tipo_4(self) -> Tuple[str, dict]:
        """
        Gera uma senha do Tipo 4: Máxima Segurança (32 caracteres)
        Para aplicações críticas e contas super-importantes
        """
        comprimento = 32
        
        # Garantir mistura variada
        senha_chars = []
        proporcoes = {
            'maiusculas': 8,
            'minusculas': 8,
            'digitos': 8,
            'especiais': 8
        }
        
        for _ in range(proporcoes['maiusculas']):
            senha_chars.append(secrets.choice(self.maiusculas))
        for _ in range(proporcoes['minusculas']):
            senha_chars.append(secrets.choice(self.minusculas))
        for _ in range(proporcoes['digitos']):
            senha_chars.append(secrets.choice(self.digitos))
        for _ in range(proporcoes['especiais']):
            senha_chars.append(secrets.choice(self.especiais))
        
        # Embaralhar
        secrets.SystemRandom().shuffle(senha_chars)
        senha = ''.join(senha_chars)
        
        tamanho_alfabeto = len(self.todos_caracteres)
        combinacoes = self.calcular_combinacoes(tamanho_alfabeto, comprimento)
        entropia = self.calcular_entropia(tamanho_alfabeto, comprimento)
        tempo = self.calcular_tempo_forca_bruta(combinacoes)
        
        return senha, {
            'tipo': 'Máxima Segurança',
            'comprimento': comprimento,
            'tamanho_alfabeto': tamanho_alfabeto,
            'combinacoes': combinacoes,
            'entropia': entropia,
            'tempo_forca_bruta': tempo,
            'classificacao': self.classificar_forca(entropia)
        }
    
    def gerar_todas_senhas(self) -> List[Tuple[str, dict]]:
        """
        Gera as 4 senhas recomendadas.
        
        Returns:
            Lista de tuplas (senha, informações)
        """
        return [
            self.gerar_senha_tipo_1(),
            self.gerar_senha_tipo_2(),
            self.gerar_senha_tipo_3(),
            self.gerar_senha_tipo_4()
        ]


def formatar_numero_grande(numero: float) -> str:
    """
    Formata números grandes de forma legível.
    
    Args:
        numero: Número a formatar
    
    Returns:
        String formatada
    """
    if numero >= 1e30:
        return f"{numero:.2e}"
    elif numero >= 1e9:
        return f"{numero/1e9:.2f} bilhões"
    elif numero >= 1e6:
        return f"{numero/1e6:.2f} milhões"
    else:
        return f"{numero:,.0f}"


def main():
    """
    Função principal: Gera e exibe as 4 senhas seguras.
    """
    print("\n" + "="*80)
    print("🔐 PROJETO: SEGURANÇA DIGITAL - GERADOR DE SENHAS SEGURAS")
    print("Unidade de Aprendizagem: Matemática em Segurança Digital")
    print("Autor: Isabelly Oliveira Santana")
    print(f"Data: {datetime.now().strftime('%d de %B de %Y')}")
    print("="*80 + "\n")
    
    gerador = GeradorSenhaSegura()
    senhas_geradas = gerador.gerar_todas_senhas()
    
    for idx, (senha, info) in enumerate(senhas_geradas, 1):
        print(f"\n{'='*80}")
        print(f"SENHA #{idx}: {info['tipo']}")
        print(f"{'='*80}")
        print(f"\n🔑 Senha: {senha}")
        print(f"\n📊 ANÁLISE MATEMÁTICA:")
        print(f"   Comprimento: {info['comprimento']} caracteres")
        print(f"   Tamanho do Alfabeto: {info['tamanho_alfabeto']} caracteres")
        print(f"   Combinações Possíveis: {formatar_numero_grande(info['combinacoes'])}")
        print(f"   Entropia: {info['entropia']:.2f} bits")
        print(f"   Classificação: {info['classificacao']}")
        print(f"\n⏱️  TEMPO PARA QUEBRAR (Força Bruta):")
        print(f"   Com 1 bilhão de tentativas/segundo: {info['tempo_forca_bruta']}")
        print(f"\n📚 CÁLCULOS:")
        print(f"   Fórmula de Combinações: C = m^n = {info['tamanho_alfabeto']}^{info['comprimento']}")
        print(f"   Fórmula de Entropia: H = log₂(C) = log₂({formatar_numero_grande(info['combinacoes'])})")
        print(f"   Resultado: {info['entropia']:.2f} bits de entropia")
    
    print(f"\n\n{'='*80}")
    print("✅ Projeto concluído com sucesso!")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
