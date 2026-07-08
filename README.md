# 🔐 Segurança Digital: Matemática para Senhas Seguras

## Descrição do Projeto

Este projeto educacional demonstra como utilizar **matemática** para criar senhas seguras. Implementamos 4 diferentes estratégias de geração de senhas utilizando conceitos matemáticos como:

- **Sequência de Fibonacci** - Números sequenciais matemáticos
- **Números Primos** - Propriedades de números primos para segurança
- **Codificação Caesar + Hashing** - Criptografia clássica com técnicas modernas
- **Hash SHA-256 com Salt** - Algoritmo criptográfico de alta segurança

## 📋 Conteúdo

```
senha-da-isabelly/
├── README.md                          # Este arquivo
├── .gitignore                         # Configuração Git
├── geracao_senhas.py                  # Módulo principal de geração
├── teste_senhas.py                    # Script de testes
└── resultados/
    └── senhas_geradas.txt             # Saída do programa
```

## 🔑 As 4 Senhas Geradas

### 1️⃣ Senha com Fibonacci (Sequência Matemática)
- Usa números da sequência de Fibonacci
- Exemplo: `1-1-2-3-5-8-13-21-34-55`
- Segurança: Média (previsível se conhecer o padrão)

### 2️⃣ Senha com Números Primos (Teoria dos Números)
- Usa números primos em ordem
- Exemplo: `2-3-5-7-11-13-17-19-23-29`
- Segurança: Média (padrão matemático)

### 3️⃣ Senha com Caesar + Hashing (Criptografia Clássica + Moderna)
- Aplica cifra de Caesar + hash MD5
- Exemplo: `8f14e45fceea167a5a36dedd4bea2543`
- Segurança: Média-Alta (algoritmo combinado)

### 4️⃣ Senha com SHA-256 + Salt (Criptografia Moderna)
- Usa algoritmo SHA-256 com salt aleatório
- Exemplo: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`
- Segurança: ⭐⭐⭐⭐⭐ Alta (padrão de segurança moderna)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Nenhuma dependência externa necessária (usa biblioteca padrão)

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/Isabellyoliveirasantana/senha-da-isabelly.git
cd senha-da-isabelly

# Executar o programa
python geracao_senhas.py

# Executar testes
python teste_senhas.py
```

## 📊 Resultado Esperado

O programa exibirá as 4 senhas geradas com seus respectivos níveis de segurança:

```
=================================================
🔐 SEGURANÇA DIGITAL: MATEMÁTICA PARA SENHAS
=================================================

1️⃣  Senha Fibonacci: 1-1-2-3-5-8-13-21-34-55
    Nível de Segurança: ⭐⭐ Média

2️⃣  Senha Primos: 2-3-5-7-11-13-17-19-23-29
    Nível de Segurança: ⭐⭐ Média

3️⃣  Senha Caesar+MD5: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
    Nível de Segurança: ⭐⭐⭐ Média-Alta

4️⃣  Senha SHA-256+Salt: 7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w
    Nível de Segurança: ⭐⭐⭐⭐⭐ Alta

=================================================
```

## 📚 Conceitos Matemáticos Utilizados

### Sequência de Fibonacci
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

### Números Primos
- Números naturais maiores que 1 divisíveis apenas por 1 e por si mesmos
- Fundamentais em criptografia moderna

### Cifra de Caesar
- Substituição simples: cada letra é deslocada por um número fixo
- Exemplo: A → D (deslocamento de 3)

### Hash SHA-256
- Função criptográfica que gera 256 bits de saída
- Praticamente impossível reverter (função unidirecional)
- Padrão de segurança atual

## 🛡️ Recomendações de Segurança

✅ **Use senhas fortes como a Senha 4 (SHA-256+Salt)**
- Combinação de maiúsculas, minúsculas, números e símbolos
- Mínimo 12 caracteres
- Nunca reutilizar senhas
- Usar gerenciador de senhas

❌ **Evite padrões previsíveis** como Fibonacci e Primos

## 👨‍💻 Autor

**Isabelly Oliveira Santana**  
Projeto educacional sobre Segurança Digital

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

## 🔗 Recursos Adicionais

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
- [Criptografia Moderna](https://owasp.org/)
- [SHA-256 Explicado](https://en.wikipedia.org/wiki/SHA-2)

---

**Última atualização:** 2026-07-08
