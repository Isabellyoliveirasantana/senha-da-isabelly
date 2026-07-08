# 📐 Conceitos Matemáticos Utilizados

## 1. Sequência de Fibonacci

### Definição
A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores.

### Fórmula Matemática
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  para n ≥ 2
```

### Sequência
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
```

### Aplicação em Senhas
- ✅ Fácil de gerar
- ✅ Padrão matemático interessante
- ❌ Previsível se conhecer o padrão
- ❌ Segurança média

### Exemplo
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 2. Números Primos

### Definição
Números primos são números naturais maiores que 1 que têm apenas dois divisores: 1 e ele próprio.

### Propriedades
- Infinitos em quantidade
- Fundamentais em criptografia (RSA, por exemplo)
- Difíceis de fatorizar em números grandes

### Primeiros Primos
```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47...
```

### Teste de Primalidade
```
Para verificar se n é primo:
1. Se n < 2: não é primo
2. Se n = 2: é primo
3. Se n é par: não é primo
4. Testar divisão por números ímpares até √n
```

### Aplicação em Senhas
- ✅ Propriedades matemáticas interessantes
- ✅ Usado em criptografia real
- ❌ Padrão ainda previsível
- ❌ Segurança média

---

## 3. Cifra de Caesar

### Definição
Cifra de substituição simples que desloca cada letra por um número fixo de posições no alfabeto.

### Fórmula Matemática
```
C = (P + k) mod 26

Onde:
- C: caractere cifrado
- P: posição do caractere (0-25)
- k: chave (deslocamento)
- mod 26: operação módulo (resto da divisão)
```

### Exemplo
```
Deslocamento = 3
A → D
B → E
C → F
...
X → A
Y → B
Z → C

Palavra: HELLO
Cifrado: KHOOR
```

### Aplicação em Senhas
- ✅ Conceito clássico de criptografia
- ❌ Muito fraca (apenas 25 possibilidades)
- ❌ Facilmente quebrável
- ✅ Combinada com hash: mais segura

---

## 4. Função Hash MD5

### Definição
MD5 (Message Digest 5) é um algoritmo criptográfico que gera um hash de 128 bits a partir de uma entrada de qualquer tamanho.

### Características
- **Entrada**: Qualquer tamanho
- **Saída**: 128 bits (32 caracteres hexadecimais)
- **Determinístico**: Mesma entrada sempre gera mesma saída
- **Unidirecional**: Impossível reverter para entrada original
- **Efeito avalanche**: Pequena mudança causa grande mudança no hash

### Exemplo
```
MD5("SENHASEGURA") = 9a0364b9e99bb480dd25e1f0284c8555
MD5("SENHASEGURB") = 5c6a82c78ae4f7c85e1f8f5a9e1e9c3d
```

### Saída Hexadecimal
```
0-9 e a-f (16 caracteres possíveis)
32 caracteres total = 128 bits
```

### Segurança
- ⚠️ **DEPRECATED**: Não use para segurança crítica
- ❌ Colisões descobertas (múltiplas entradas = mesmo hash)
- ✅ Bom para verificação de integridade
- ✅ Adequado para fins educacionais

---

## 5. Função Hash SHA-256

### Definição
SHA-256 (Secure Hash Algorithm 256-bit) é um algoritmo criptográfico que gera um hash de 256 bits.

### Características
- **Entrada**: Qualquer tamanho
- **Saída**: 256 bits (64 caracteres hexadecimais)
- **Determinístico**: Mesma entrada sempre gera mesma saída
- **Unidirecional**: Impossível reverter
- **Resistência a colisão**: Extremamente difícil encontrar duas entradas com mesmo hash
- **Efeito avalanche**: Pequena mudança causa grande mudança no hash

### Exemplo
```
SHA-256("SENHASEGURA") = 
7e9f8f4c2a1e9c3d5b7a6f4e8c2d1a9b6c5e3f2d1a0b9c8d7e6f5a4b3c2d1e
```

### Saída Hexadecimal
```
64 caracteres hexadecimais = 256 bits
Mais seguro que MD5 (128 bits)
```

### Segurança
- ✅ **PADRÃO ATUAL**: Recomendado para segurança
- ✅ Nenhuma colisão prática conhecida
- ✅ Usado em Bitcoin e blockchain
- ✅ Padrão NIST

---

## 6. Salt em Hashing

### Definição
Salt é um valor aleatório adicionado ao texto antes do hashing para aumentar a segurança.

### Por quê?
Sem salt:
```
Palavra: "senha123"
SHA-256("senha123") = xxxxx...xxxxx

Todos com "senha123" têm o mesmo hash!
Podemos usar tabelas pré-computadas (rainbow tables)
```

Com salt:
```
Salt: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
SHA-256(salt + "senha123") = yyyyy...yyyyy

Cada salt gera hash diferente!
Rainbow tables inúteis
```

### Implementação
```python
salt = os.urandom(16)  # 16 bytes aleatórios
hash = SHA-256(salt + password)
```

### Segurança
- ✅ Previne rainbow tables
- ✅ Força atacante a calcular cada hash
- ✅ Padrão em sistemas modernos
- ✅ Essencial para senhas

---

## 7. Bits vs Hexadecimal

### Conversão
```
1 byte = 8 bits
1 caractere hexadecimal = 4 bits

MD5:     128 bits = 16 bytes = 32 caracteres hex
SHA-256: 256 bits = 32 bytes = 64 caracteres hex
```

### Exemplo
```
Valor binário: 1010 1100 = 172
Valor hex: AC

A = 1010 (10 em binário)
C = 1100 (12 em binário)
```

---

## 8. Operação Módulo (mod)

### Definição
Operação que retorna o resto da divisão entre dois números.

### Fórmula
```
a mod n = resto de a ÷ n
```

### Exemplos
```
7 mod 3 = 1    (pois 7 ÷ 3 = 2 resto 1)
10 mod 5 = 0   (pois 10 ÷ 5 = 2 resto 0)
26 mod 26 = 0  (pois 26 ÷ 26 = 1 resto 0)
27 mod 26 = 1  (pois 27 ÷ 26 = 1 resto 1)
```

### Aplicação: Cifra de Caesar
```
Cifra de Caesar com deslocamento 3:
Z (posição 25) + 3 = 28
28 mod 26 = 2 → C
```

---

## Comparação de Segurança

| Método | Bits | Tamanho | Segurança | Recomendado |
|--------|------|---------|-----------|-------------|
| Fibonacci | N/A | Variável | ⭐⭐ Baixa | Educacional |
| Primos | N/A | Variável | ⭐⭐ Baixa | Educacional |
| Caesar | ~5 | Variável | ⭐ Muito Baixa | Histórico |
| MD5 | 128 | 32 hex | ⭐⭐⭐ Média | ⚠️ Deprecated |
| SHA-256 | 256 | 64 hex | ⭐⭐⭐⭐⭐ Alta | ✅ **RECOMENDADO** |

---

## Recomendações Finais

### Para Senhas REAIS:
1. ✅ Use SHA-256 com salt aleatório
2. ✅ Mínimo 12 caracteres
3. ✅ Misture maiúsculas, minúsculas, números e símbolos
4. ✅ Use gerenciador de senhas (Bitwarden, 1Password, etc)
5. ✅ Habilite autenticação em dois fatores (2FA)

### Para Fins Educacionais:
- 📚 Entenda cada conceito matematicamente
- 🧪 Teste diferentes abordagens
- 📊 Compare resultados
- 🔬 Analise a segurança de cada método
