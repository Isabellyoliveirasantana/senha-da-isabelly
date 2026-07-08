# 🧮 Matemática por Trás das Senhas Seguras

## 1. Teoria da Informação

### Entropia de Shannon
A entropia mede quantos bits de informação uma senha contém.

```
H = log₂(N)
```

Onde N é o número de combinações possíveis.

**Exemplo:**
- Senha com 8 dígitos: H = log₂(10^8) = 8 × log₂(10) ≈ 26.6 bits
- Senha com 8 caracteres (94 possíveis): H = log₂(94^8) ≈ 52.7 bits
- Senha com 16 caracteres (94 possíveis): H = log₂(94^16) ≈ 105.5 bits

### Recomendação NIST
O Instituto Nacional de Padrões e Tecnologia recomenda:
- **Mínimo 128 bits de entropia** para senhas muito fortes
- **Calculador online**: https://www.ncsc.gov.uk/collection/mobile-device-guidance/using-built-in-platform-features/storing-data-securely

---

## 2. Análise Combinatória

### Princípio Fundamental da Contagem

Para criar uma senha com:
- **Comprimento**: n caracteres
- **Tamanho do alfabeto**: m caracteres diferentes

**Número de combinações possíveis:**
```
C = m^n
```

### Exemplo Prático

**Senha com 12 caracteres, usando 94 caracteres diferentes:**
```
C = 94^12
C = 475,920,314,814,253,376 combinações possíveis
C ≈ 4.76 × 10^17 combinações
```

**Tempo para quebrar com força bruta:**
```
Velocidade de teste: 1 bilhão de senhas/segundo (10^9)
Tempo médio = (C / 2) / 10^9
Tempo médio = 238,960,157,407 segundos
Tempo médio ≈ 7,576 anos
```

---

## 3. Aleatoriedade e Distribuição Uniforme

### Gerador Linear Congruencial (LCG) - ❌ NÃO SEGURO

```
X(n+1) = (a × X(n) + c) mod m
```

**Problema:** Padrões previsíveis

### Gerador Criptograficamente Seguro - ✅ RECOMENDADO

**Python `secrets` module:**
```python
import secrets
caractere_aleatorio = secrets.choice(opcoes)
```

Usa:
- Sistema operacional `/dev/urandom` (Linux/Mac)
- `CryptGenRandom` (Windows)
- Entropia de alta qualidade

---

## 4. Distribuição de Probabilidade

### Distribuição Uniforme
Cada caractere tem a **mesma probabilidade** de aparecer.

```
P(caractere_i) = 1/m
```

Onde m = 94 (número total de caracteres possíveis)

**Cada caractere:**
```
P(caractere) = 1/94 ≈ 0.0106 (aproximadamente 1%)
```

### Entropia por Caractere

```
Entropia por caractere = log₂(m)
```

**Exemplos:**
- Apenas números: log₂(10) ≈ 3.32 bits/caractere
- Letras + números: log₂(36) ≈ 5.17 bits/caractere
- Caracteres completos: log₂(94) ≈ 6.55 bits/caractere

---

## 5. Força Bruta vs Algoritmos Avançados

### Força Bruta
```
Tentativas = C / 2 (na média, quebra na metade)
Tempo = Tentativas / (velocidade de teste)
```

### Rainbow Tables (Tabelas Arco-íris)
Pré-computadas para hashes comuns.

**Defesa:** Use SALT + HASH
```
hash = SHA256(senha + salt_aleatorio)
```

### Ataques de Dicionário
Tenta palavras do dicionário.

**Defesa:** Não use palavras reais, use caracteres aleatórios

---

## 6. Fórmula de Cálculo de Força

### Índice de Força de Senha (PSS - Password Strength Score)

```
PSS = log₂(C) = comprimento × log₂(tamanho_alfabeto)
```

**Classificação:**
```
PSS < 30:      Muito Fraca  🔴
30 ≤ PSS < 50: Fraca        🟠
50 ≤ PSS < 80: Média        🟡
80 ≤ PSS < 120: Forte       🟢
PSS ≥ 120:     Muito Forte  🟢🟢
```

---

## 7. Cálculos das 4 Senhas Geradas

### Senha 1: Caracteres Aleatórios (16 caracteres)
```
Alfabeto: 94 caracteres
Comprimento: 16
Combinações: 94^16 ≈ 7.9 × 10^31
Entropia: log₂(94^16) ≈ 105.5 bits
Força: Muito Forte ✓
```

### Senha 2: Com Padrão Específico (18 caracteres)
```
Alfabeto: 94 caracteres
Comprimento: 18
Combinações: 94^18 ≈ 6.9 × 10^34
Entropia: log₂(94^18) ≈ 112.6 bits
Força: Muito Forte ✓
```

### Senha 3: Passphrase (24 caracteres)
```
Alfabeto: Misto (letras, números, símbolos)
Comprimento: 24
Combinações: 94^24 ≈ 5.2 × 10^47
Entropia: log₂(94^24) ≈ 157 bits
Força: Ultra-Forte ✓✓
```

### Senha 4: Máxima Segurança (32 caracteres)
```
Alfabeto: 94 caracteres
Comprimento: 32
Combinações: 94^32 ≈ 2.3 × 10^63
Entropia: log₂(94^32) ≈ 211 bits
Força: Máxima Segurança ✓✓✓
```

---

## 📖 Referências Matemáticas

- **Shannon, C. E. (1948)**: "A Mathematical Theory of Communication"
- **NIST SP 800-63B**: Autenticação e Gerenciamento de Ciclo de Vida
- **Schneier, B. (2015)**: "Secrets and Lies: Digital Security in a Networked World"

---

## 🔬 Exercícios Práticos

### Exercício 1: Calcular Entropia
Calcule a entropia de uma senha com 20 caracteres usando um alfabeto de 62 caracteres (letras + números).

**Solução:**
```
H = log₂(62^20) = 20 × log₂(62) ≈ 20 × 5.95 ≈ 119 bits
```

### Exercício 2: Tempo para Quebrar
Uma senha tem 10^30 combinações possíveis. Quanto tempo levaria para quebrá-la testando 10^9 tentativas por segundo?

**Solução:**
```
Tempo = (10^30 / 2) / 10^9 = 5 × 10^20 segundos ≈ 15.8 trilhões de anos
```

### Exercício 3: Comparar Força
Compare a força de uma senha com 8 caracteres (94 possíveis) versus 12 caracteres (94 possíveis).

**Solução:**
```
8 caracteres: H = log₂(94^8) ≈ 52.7 bits
12 caracteres: H = log₂(94^12) ≈ 79.1 bits
Diferença: 79.1 - 52.7 = 26.4 bits (4 vezes mais segura)
```
