# 📋 Task Flask API

API REST simples para gerenciamento de tarefas (Tasks) desenvolvida com Flask. Esta aplicação implementa operações CRUD completas (Create, Read, Update, Delete) para gerenciar tarefas.

## 🚀 Características

- ✅ Operações CRUD completas (Criar, Ler, Atualizar, Deletar)
- 🔄 API RESTful com endpoints JSON
- 📝 Modelo de dados simples e intuitivo
- 🎯 Interface REST clara e documentada

## 📦 Tecnologias Utilizadas

- **Flask** 3.0.0 - Framework web Python
- **Flask-Cors** 4.0.0 - Suporte a CORS
- **Werkzeug** 3.0.1 - Servidor WSGI
- **Python** 3.14+

## 🛠️ Instalação

### Pré-requisitos

- Python 3.12 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/LeafarxC/task-flask.git
cd task-flask
```

2. Crie um ambiente virtual:
```bash
python -m venv env
```

3. Ative o ambiente virtual:

**Linux/macOS:**
```bash
source env/bin/activate
```

**Windows:**
```bash
env\Scripts\activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🏃 Como Executar

Execute o servidor Flask:

```bash
python app.py
```

O servidor estará disponível em: `http://localhost:5000`

## 📡 Endpoints da API

### 1. Criar Tarefa

**POST** `/tasks`

Cria uma nova tarefa.

**Request Body:**
```json
{
  "title": "Comprar mantimentos",
  "description": "Ir ao supermercado",
  "completed": false
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "title": "Comprar mantimentos",
  "description": "Ir ao supermercado",
  "completed": false
}
```

### 2. Listar Todas as Tarefas

**GET** `/tasks`

Retorna uma lista com todas as tarefas cadastradas.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Comprar mantimentos",
    "description": "Ir ao supermercado",
    "completed": false
  },
  {
    "id": 2,
    "title": "Fazer exercícios",
    "description": "Treino na academia",
    "completed": true
  }
]
```

### 3. Obter Tarefa por ID

**GET** `/tasks/<id>`

Retorna os detalhes de uma tarefa específica.

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Comprar mantimentos",
  "description": "Ir ao supermercado",
  "completed": false
}
```

**Error:** `404 Not Found`
```json
{
  "error": "Task not found"
}
```

### 4. Atualizar Tarefa

**PUT** `/tasks/<id>`

Atualiza os dados de uma tarefa existente.

**Request Body:**
```json
{
  "title": "Comprar mantimentos e medicamentos",
  "description": "Ir ao supermercado e farmácia",
  "completed": true
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Comprar mantimentos e medicamentos",
  "description": "Ir ao supermercado e farmácia",
  "completed": true
}
```

### 5. Deletar Tarefa

**DELETE** `/tasks/<id>`

Remove uma tarefa do sistema.

**Response:** `200 OK`
```json
{
  "message": "Task deleted successfully"
}
```

## 📝 Modelo de Dados

### Task

```python
{
  "id": int,           # ID único da tarefa (gerado automaticamente)
  "title": string,     # Título da tarefa (obrigatório)
  "description": string, # Descrição da tarefa
  "completed": boolean  # Status de conclusão (padrão: false)
}
```

## 🧪 Testando a API

### Usando cURL

**Criar tarefa:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Nova tarefa", "description": "Descrição da tarefa", "completed": false}'
```

**Listar tarefas:**
```bash
curl http://localhost:5000/tasks
```

**Obter tarefa específica:**
```bash
curl http://localhost:5000/tasks/1
```

**Atualizar tarefa:**
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Tarefa atualizada", "completed": true}'
```

**Deletar tarefa:**
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

### Usando Postman

1. Base URL: `http://localhost:5000`
2. Configure o header `Content-Type: application/json` para requisições POST e PUT
3. Use os endpoints documentados acima

## 📁 Estrutura do Projeto

```
task-flask/
│
├── app.py                 # Aplicação Flask principal
├── models/
│   └── task.py           # Modelo de dados Task
├── requirements.txt       # Dependências do projeto
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Este arquivo
```

## ⚠️ Notas Importantes

- Esta aplicação usa armazenamento em memória (lista Python), então os dados são perdidos quando o servidor é reiniciado
- Para produção, considere adicionar um banco de dados (SQLite, PostgreSQL, etc.)
- O modo debug está ativado, o que não é recomendado para ambientes de produção

## 🔮 Possíveis Melhorias

- [ ] Integração com banco de dados (SQLite/PostgreSQL)
- [ ] Autenticação e autorização
- [ ] Validação de dados mais robusta
- [ ] Testes automatizados
- [ ] Documentação com Swagger/OpenAPI
- [ ] Paginação para listagem de tarefas
- [ ] Filtros e busca de tarefas

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

LeafarxC

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
