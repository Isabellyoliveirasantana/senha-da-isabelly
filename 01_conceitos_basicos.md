# 📚 Conceitos Básicos de Segurança Digital

## O que é uma Senha Segura?

Uma senha segura é aquela que é:
- **Difícil de adivinhar** através de tentativa e erro
- **Difícil de quebrar** com força bruta
- **Imprevisível** e sem padrões óbvios
- **Longa o suficiente** para ter alta entropia

## 🔢 Conceitos Matemáticos

### 1. Entropia de Shannon
```
Entropia (H) = -∑ p(x) × log₂(p(x))
```

Mede a quantidade de informação e incerteza em uma senha.

**Exemplo:**
- Senha com apenas números (0-9): 3,32 bits por caractere
- Senha com letras + números: 5,7 bits por caractere
- Senha com caracteres especiais: 6,55 bits por caractere

### 2. Força Bruta vs Segurança

**Tempo para quebrar uma senha por força bruta:**
```
Tempo = (Combinações Possíveis / 2) / Tentativas por Segundo
```

**Exemplo com 1 bilhão de tentativas/segundo:**

| Tipo de Senha | Comprimento | Tempo para Quebrar |
|---------------|-------------|-----------
| Números | 8 | 0.0045 segundos |
| Letras minúsculas | 8 | 0.68 horas |
| Letras + números | 12 | 2.1 anos |
| Caracteres especiais | 16 | 17 milhões de anos |

### 3. Combinações Possíveis

```
Combinações = (tamanho_do_conjunto)^(comprimento)
```

**Conjuntos de caracteres:**
- Dígitos (0-9): 10 caracteres
- Letras minúsculas (a-z): 26 caracteres
- Letras maiúsculas (A-Z): 26 caracteres
- Caracteres especiais: ~32 caracteres (! @ # $ % ^ & * etc)

**Total comum: 94 caracteres**

**Cálculo de uma senha com 16 caracteres:**
```
Combinações = 94^16 ≈ 7.9 × 10^31
```

## 🔐 Princípios de Segurança

### 1. Princípio de Kerckhoffs
"A segurança de um sistema não deve depender da confidencialidade do algoritmo, mas da confidencialidade da chave"

### 2. Defesa em Profundidade
Use múltiplas camadas de segurança

### 3. Aleatoriedade Verdadeira
Use geradores criptograficamente seguros, não pseudoaleatórios

## ⛔ Erros Comuns

❌ Senhas baseadas em datas pessoais (123456 ou 1990)
❌ Palavras do dicionário (password, dragon, master)
❌ Padrões teclado (qwerty, asdfgh)
❌ Substituições óbvias (l33t speak: P@ssw0rd)
❌ Informações pessoais (nome, sobrenome, pet)
❌ Reutilizar a mesma senha em múltiplos sites

## ✅ Boas Práticas

✓ Mínimo 12 caracteres (idealmente 16+)
✓ Misture maiúsculas, minúsculas, números e símbolos
✓ Use um gerenciador de senhas
✓ Ative autenticação de dois fatores (2FA)
✓ Altere senhas regularmente
✓ Nunca compartilhe sua senha
✓ Use passphrases aleatórias em vez de palavras

## 📊 Escala de Força de Senha

| Nível | Entropia | Exemplos |
|-------|----------|----------|
| Muito Fraca | < 30 bits | 123456, password |
| Fraca | 30-50 bits | Senha123 |
| Média | 50-80 bits | P@ssw0rd2024 |
| Forte | 80-120 bits | 7KmP$xQ!wN2vL5 |
| Muito Forte | > 120 bits | eMx9%Qr@4nK2pL!8sJ# |
