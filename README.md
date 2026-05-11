# Sistema de Gestão Acadêmica (API Flask)

Este projeto é uma API REST para gestão acadêmica, permitindo o controle de alunos, professores, cadeiras (disciplinas) e notas. A aplicação foi construída com foco em uma arquitetura modular e segura, utilizando controle de acesso baseado em funções (**RBAC**).

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Flask** (Framework Web)
* **MongoDB** (Banco de Dados NoSQL)
* **Flask-JWT-Extended** (Autenticação e Autorização)
* **Flask-Bcrypt** (Criptografia de senhas)
* **PyMongo** (Driver de conexão com MongoDB)

## 🏗️ Arquitetura do Projeto

O projeto segue padrões de design para facilitar a manutenção e escalabilidade:

* **Repository Pattern:** Encapsula a lógica de acesso aos dados (MongoDB), isolando o banco de dados do restante da aplicação.
* **Controller Pattern:** Gerencia as regras de negócio e a comunicação entre as rotas e os repositórios.
* **Blueprints:** Organização das rotas do Flask de forma modular.
* **Middleware de Segurança:** Uso de decorators customizados para validação de permissões por nível de acesso (`admin`, `professor`, `aluno`).

## 🔐 Funcionalidades Principais

* **Gestão de Usuários:** Criação automática de usuários com geração de senhas temporárias e hashing via Bcrypt.
* **Controle de Alunos:** CRUD completo, matrícula em disciplinas e sistema de lançamento/cálculo de médias.
* **Controle de Professores:** Gestão de docentes e disciplinas ministradas.
* **Segurança RBAC:**
* **Admin:** Acesso total ao sistema.
* **Professor:** Pode gerenciar notas e visualizar alunos.
* **Aluno:** Acesso restrito aos próprios dados e notas.



## 📁 Estrutura de Pastas

```text
├── controller/          # Regras de negócio
├── model/
│   ├── connection/      # Singleton de conexão com MongoDB
│   └── repository/      # Camada de persistência de dados
├── security/            # Helpers de senha e decorators de roles
├── routes/              # Definição dos Blueprints e Endpoints
└── app.py               # Ponto de entrada da aplicação

```

## 🛠️ Como Executar (Exemplo)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git

```


2. Instale as dependências:

```bash
   pip install -r requirements.txt

```

3. Configure sua string de conexão do MongoDB no arquivo `DBConnectionHandler`.
4. Inicie o servidor:

```bash
   python app.py

```

## 📝 Endpoints Principais (Resumo)

| Método | Endpoint | Acesso | Descrição |
| --- | --- | --- | --- |
| POST | `/alunos/` | Admin | Cadastra um novo aluno e cria usuário |
| GET | `/alunos/<matricula>` | Todos | Retorna dados do aluno (protegido por lógica de ID) |
| GET | `/alunos/<matricula>/notas` | Aluno | Retorna as notas do aluno logado |
| POST | `/professores/` | Admin | Cadastra um novo professor |
| PUT | `/alunos/<matricula>` | Admin/Prof | Atualiza dados cadastrais |

---
