# TaskFlow – Sistema Ágil de Gerenciamento de Tarefas

## 🎯 Objetivo
Desenvolver um sistema ágil e funcional de gerenciamento de tarefas para uma startup de logística, permitindo a priorização de tarefas críticas, monitoramento do desempenho da equipe e visualização do fluxo de trabalho.

## 📊 Escopo do Projeto
- CRUD de tarefas
- Visualização por status (Kanban)
- Priorizador de tarefas por urgência

## 🤝 Metodologia Adotada
Aplicamos a metodologia Kanban com uso de GitHub Projects para gestão de tarefas, GitHub Actions para controle de qualidade (testes automatizados) e modelagem UML no draw.io.

## 📝 Instruções para Execução
1. Clone o repositório:
```bash
git clone https://github.com/igorcfluna/taskflow-agile-project.git
cd taskflow-agile-project
```
2. Instale dependências (Python):
```bash
pip install -r requirements.txt
```
3. Execute o sistema:
```bash
python src/main.py
```

## ⚖️ Simulação de Mudança de Escopo
Durante o desenvolvimento, foi solicitada a adição de um campo de "prioridade" às tarefas. A funcionalidade foi incluída e a estrutura do código e o quadro Kanban foram atualizados.

## 🔄 Quadro Kanban (GitHub Projects)
- A Fazer
- Em Progresso
- Concluído

Cada tarefa está vinculada a issues e milestones, com atualização frequente de status.

## ✅ Pipeline de Testes (CI)
Utilizamos GitHub Actions com `pytest` para execução de testes automáticos a cada push. Ver pasta `.github/workflows/ci.yml`

## 📄 Modelagem de Requisitos e UML
Disponível na pasta `docs/`:
- `diagrama-casos-uso.drawio`
- `diagrama-classes.drawio`

## 💡 Tecnologias Utilizadas
- Python 3.11
- Pytest
- GitHub Actions
- draw.io (UML)

## 🎓 Autoria
Este projeto foi desenvolvido por Igor Luna como parte da disciplina de Engenharia de Software - UNIFECAF.

---

### Estrutura de Pastas
```
taskflow-agile-project/
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── requisitos.md
│   ├── diagrama-casos-uso.drawio
│   └── diagrama-classes.drawio
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
└── requirements.txt
```

### Exemplo de Commit
```
feat: adiciona funcionalidade de criação de tarefa com prioridade
fix: corrige bug na listagem de tarefas concluídas
chore: atualiza README com instruções
```

### Licença
Este projeto é livre para fins educacionais. Sinta-se à vontade para explorar, clonar e adaptar.
