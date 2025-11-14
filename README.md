# SuperAlmoxarifado

Sistema de gerenciamento de almoxarifado desenvolvido em Django para controle de estoque, produtos, fornecedores, pedidos e retiradas.

## 📋 Especificações do Projeto

### Tecnologias Utilizadas
- **Framework:** Django 5.2.8
- **Linguagem:** Python 3.x
- **Banco de Dados:** SQLite3 (desenvolvimento)
- **Interface Admin:** Django Admin

### Estrutura do Projeto
O projeto está organizado em módulos (apps) para melhor manutenibilidade:

```
SuperAlmoxarifado/
├── SuperAlmoxarifado/          # Configurações principais do projeto
│   ├── settings.py             # Configurações do Django
│   ├── urls.py                 # Rotas principais
│   ├── wsgi.py                 # Configuração WSGI
│   └── asgi.py                 # Configuração ASGI
├── apps/                       # Aplicações do sistema
│   ├── fornecedores/           # Gestão de fornecedores
│   ├── usuarios/               # Gestão de usuários
│   ├── produtos/               # Gestão de produtos/itens
│   ├── pedidos/                # Gestão de pedidos
│   └── retirada/               # Gestão de retiradas de estoque
├── db.sqlite3                  # Banco de dados SQLite
├── manage.py                   # Utilitário de gerenciamento Django
└── README.md                   # Este arquivo
```

## 🚀 Funcionalidades Planejadas

### Módulos do Sistema

#### 1. **Fornecedores** (`apps.fornecedores`)
- Cadastro e gerenciamento de fornecedores
- Informações de contato e dados comerciais
- Histórico de fornecimentos

#### 2. **Usuários** (`apps.usuarios`)
- Gestão de usuários do sistema
- Controle de permissões e acessos
- Perfis de usuário

#### 3. **Produtos** (`apps.produtos`)
- Cadastro de produtos/itens do almoxarifado
- Controle de estoque
- Categorização de produtos
- Informações de quantidade, localização e especificações

#### 4. **Pedidos** (`apps.pedidos`)
- Registro de pedidos de compra
- Acompanhamento de status de pedidos
- Vinculação com fornecedores
- Histórico de pedidos

#### 5. **Retirada** (`apps.retirada`)
- Controle de retiradas de produtos do estoque
- Registro de responsáveis pela retirada
- Baixa automática no estoque
- Histórico de movimentações

## 💡 Funcionamento Básico

### Fluxo de Trabalho

1. **Cadastro Inicial**
   - Cadastrar fornecedores no sistema
   - Cadastrar produtos disponíveis no almoxarifado
   - Configurar usuários e permissões

2. **Gestão de Pedidos**
   - Criar pedidos de compra vinculados a fornecedores
   - Acompanhar status dos pedidos
   - Registrar entrada de produtos no estoque

3. **Controle de Estoque**
   - Visualizar produtos disponíveis
   - Consultar quantidades e localizações
   - Atualizar informações de produtos

4. **Retirada de Produtos**
   - Registrar retiradas de produtos
   - Identificar responsável pela retirada
   - Atualizar automaticamente o estoque
   - Manter histórico de movimentações

### Acesso ao Sistema

O sistema utiliza o Django Admin como interface principal:

```bash
# Acessar o painel administrativo
http://localhost:8000/admin/
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.12.3
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

### Passos para Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd SuperAlmoxarifado
```

2. **Execute as migrações**
```bash
python manage.py migrate
```

3. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

4. **Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver
```

5. **Acesse o sistema**
```
http://localhost:8000/admin/
```

## 📝 Configurações Importantes

### Aplicações
Atualmente, as seguintes aplicações estão comentadas no `settings.py` e precisam ser descomentadas conforme o desenvolvimento:

```python
INSTALLED_APPS = [
    # Usuários do sistema
     'apps.fornecedores',
     'apps.usuarios',

    # Controle de itens
     'apps.produtos',
     'apps.retirada',
     'apps.pedidos',
]
```

### Banco de Dados
O projeto está configurado para usar SQLite3 em desenvolvimento. Para produção, considere migrar para PostgreSQL ou MySQL.

### Segurança
⚠️ **IMPORTANTE:** Antes de colocar em produção:
- Altere a `SECRET_KEY` no `settings.py`
- Configure `DEBUG = False`
- Defina `ALLOWED_HOSTS` apropriadamente
- Configure um banco de dados robusto
- Implemente HTTPS

## 🐛 Erros do Sistema

## Nota: Talisson, sinto muito mas não consegui resolver os arquivos inúteis, deixo para você.

2. Mandei alguns arquivos inúteis para o git. Dê um jeito de evitar isso

ASS: O outro dev do sistema



**Versão:** 1.0.0
**Última Atualização:** 2025-11-13
