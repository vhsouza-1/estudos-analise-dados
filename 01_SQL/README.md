# SQL - Estudos Completos

Esta pasta documenta toda a minha jornada de aprendizado em SQL, organizada em 4 níveis de complexidade. São **mais de 100 exercícios resolvidos**, desde consultas básicas até análises avançadas com Window Functions.

- Ambiente: MySQL
- Período: Fevereiro - Março 2026
- Status: ✅ Concluído

## Estrutura dos Estudos

| Pasta | Foco Principal | Arquivos | Destaque |
|-------|----------------|----------|----------|
| [`01_basico`](./01_basico) | Fundamentos, subconsultas | 3 arquivos | Subconsultas correlacionadas |
| [`02_basico_intermediario`](./02_basico_intermediario) | JOINs, tabelas derivadas | 5 arquivos | Rankings manuais com SELF JOIN |
| [`03_intermediario`](./03_intermediario) | String/Date functions, CASE, UNION | 5 arquivos | Análises temporais, Pivot Tables |
| [`04_avancado`](./04_avancado) | CTEs, Window Functions | 9 arquivos | Mais importante! |

---

## Destaque: Pasta Avançada

A pasta [`04_avancado`](./04_avancado) contém meus estudos mais aprofundados, com **9 arquivos SQL** e **mais de 50 exercícios** sobre:

### CTEs (Common Table Expressions)
- CTEs básicas, múltiplas e aninhadas
- Rankings manuais com SELF JOIN
- Análises mês a mês e comparações temporais
- Criação de calendários com UNION ALL

### Window Functions - Ranking
- `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()` - comparações e usos
- `NTILE()` para quartis e distribuições
- TOP N por categoria, cor e mês
- Identificação de gaps no ranking

### Window Functions - Agregação
- `SUM()`, `AVG()`, `COUNT()` como janelas acumuladas
- Médias móveis com diferentes janelas (3, 5, 7 períodos)
- `RANGE BETWEEN INTERVAL` para análises temporais
- Análise de Pareto (80/20) com percentuais acumulados
- Z-score e classificação estatística

### Window Functions - Deslocamento
- `LAG()` e `LEAD()` para acessar valores anteriores/posteriores
- `FIRST_VALUE()` e `LAST_VALUE()` para comparações
- Detecção de tendências (subidas, quedas, picos)
- Customer journey: dias desde a última venda

### Desafios Analíticos Avançados
- **Dashboard gerencial** com múltiplas métricas
- **Relatório completo de vendas** com 10+ métricas
- **Análise de performance por produto** com classificação estatística
- **Dashboard executivo com storytelling** - 20+ métricas combinadas:
  - Métricas gerais, evolução temporal, destaques
  - Análise de ranking (acima/abaixo da média, posição mediana)

---

## 🗺️ Resumo por Nível

### [Básico](./01_basico)
**Fundamentos do SQL**
- `SELECT`, `WHERE`, `ORDER BY`, operadores lógicos
- Funções agregadas: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
- `GROUP BY`, `HAVING`, `LIMIT`, `OFFSET`
- Subconsultas escalares e correlacionadas

### [Básico-Intermediário](./02_basico_intermediario)
**JOINs e Tabelas Derivadas**
- `INNER JOIN`, `LEFT JOIN` (simples e múltiplos)
- `GROUP BY` com JOIN para estatísticas
- Subconsultas correlacionadas com JOIN
- Tabelas derivadas (subconsultas no `FROM`)
- Rankings manuais sem Window Functions

### [Intermediário](./03_intermediario)
**Funções Específicas e Lógica Condicional**
- Funções de String: `LEFT`, `RIGHT`, `SUBSTRING`, `CONCAT`
- Funções de Data: `DATEDIFF`, `DATE_FORMAT`, `MONTHNAME`
- `CASE WHEN` para classificação e agregação condicional
- `UNION` vs `UNION ALL` para combinar resultados
- Criação de calendários e timelines

### [Avançado](./04_avancado) ⭐
**CTEs e Window Functions**
- CTEs em múltiplos níveis de complexidade
- Funções de Ranking, Agregação e Deslocamento
- Frames, médias móveis, análises temporais
- Dashboards e relatórios gerenciais
- Análises estatísticas (Pareto, Z-score)

---

## Estatísticas da Jornada

| Nível | Arquivos | Exercícios | Principais Técnicas |
|-------|----------|------------|---------------------|
| Básico | 3 | ~20 | Fundamentos, subconsultas |
| Básico-Intermediário | 5 | ~25 | JOINs, tabelas derivadas |
| Intermediário | 5 | ~25 | Funções, CASE, UNION |
| Avançado | 9 | ~50 | CTEs, Window Functions |
| **Total** | **22** | **+120** | **SQL Completo!** |

---

## Próximos Passos

Com o SQL concluído, sigo para:
- [ ] Python para Análise de Dados
- [ ] Projetos integrados (SQL + Python)
- [ ] Power BI


---

## Contato

- **Autor:** Vinícius Henrique Souza
- **Email:** vinicius.h.zlc@gmail.com
- **LinkedIn:** [linkedin.com/in/vinícius-henrique-souza](https://www.linkedin.com/in/vin%C3%ADcius-henrique-souza-17a077218/)

---

 *Este repositório documenta minha evolução como analista de dados. Sugestões e feedbacks são bem-vindos!*
