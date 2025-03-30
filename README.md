# API simples de Doação de Livros

Este projeto é uma API desenvolvida em Flask para gerenciar doações de livros como parte de um Desafio no VNW no módulo de Back-end. A API é consumida pelo seguinte site: [Repositório](https://github.com/Davi-D18/desafio3_livros_vnw)

## Estrutura do Projeto

A estrutura do projeto segue uma arquitetura organizada em camadas, com separação de responsabilidades:

```
.
├── requirements.txt
├── run.py
├── app/
│   ├── __init__.py
│   ├── config/
│   ├── docs/
│   ├── database/
│   ├── extensions/
|   ├── logs/
|   ├── messages/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
├── migrations/
├── swagger/
```

Mais informações: [Link](./app/docs/informacoes.md)

## Endpoints da API

### **GET /**

Retorna uma mensagem.

```json
{
  "message": "API doação de livros"
}
```

---

### **GET /livros**

Lista todos os livros disponíveis no banco de dados.

### **POST /doar**

Adiciona um novo livro ao banco de dados.

Para acessar mais informações das rotas, você pode clonar o repositório e acessar o seguinte link: http://localhost:5000/docs

## Configuração do Banco de Dados

O projeto utiliza **Postgres** como banco de dados. A configuração está localizada em `app/database/config.py`.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Davi-D18/desafio-3-livros.git
   cd desafio-3-livros
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Renomeie o arquivo `.env.example` para `.env`.

5. Configure o arquivo `.env` com as variáveis de ambiente desejadas.
   - **OBS:** Se você não configurar a variável `DATABASE_URL`, o banco de dados padrão será o SQLite. Caso contrário, será usado o banco de dados na variavel `DATABASE_URL`, se atente para instalar os pacotes necessários para o banco de dados.

6. **Inicializando o Banco de Dados (Migrações):**
   - **O que são Migrações?**
     - Migrações são uma forma de controlar as mudanças no esquema do seu banco de dados ao longo do tempo. Elas permitem que você crie, altere e exclua tabelas e colunas de forma organizada e consistente.
   - **O que é Flask-Migrate?**
     - Flask-Migrate é uma extensão do Flask que facilita o uso de migrações com o SQLAlchemy, o ORM (Object-Relational Mapper) usado neste projeto.
   - **Como usar?**
     - **Inicializar o ambiente de migrações:**
       ```bash
       flask db init
       ```
       - Este comando cria um diretório `migrations/` que armazenará os arquivos de migração.
     - **Criar uma nova migração:**
       ```bash
       flask db migrate -m "Initial database structure"
       ```
       - Este comando detecta as mudanças nos seus modelos (definidos em `app/models/`) e cria um arquivo de migração que descreve como aplicar essas mudanças ao banco de dados.
       - Cada arquivo na pasta model, representa uma tabela no banco de dados
       - Substitua `"Initial database structure"` por uma mensagem descritiva da alteração.
     - **Aplicar as migrações ao banco de dados:**
       ```bash
       flask db upgrade
       ```
       - Este comando executa as migrações pendentes, aplicando as mudanças ao banco de dados.
7. Inicie o servidor:
   ```bash
   python run.py
   ```

6. Acesse a API em `localhost:5000`.
