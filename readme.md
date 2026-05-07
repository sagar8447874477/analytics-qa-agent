# 📊 Analytics Q&A Agent

An AI-assisted analytics web application that allows users to ask natural-language product analytics questions and receive answers generated directly from a SQLite database.

Example questions:

* “What was our DAU last week?”
* “Show MAU”
* “How many US users do we have?”
* “Revenue this month”
* “This week vs last week”

The system converts natural-language questions into SQL queries, executes them on a local analytics database, and displays:

* Query results
* Generated SQL
* Visualizations

---

# 🚀 Project Objective

The goal of this project is to simulate how internal product teams interact with analytics systems using conversational interfaces.

Instead of manually writing SQL, users can ask questions in natural language and get analytics insights instantly.

This project was intentionally designed to work:

* fully locally
* without paid APIs
* without external LLM providers

---

# 🧠 High-Level Architecture

```text
User Question
↓
Intent Detection
↓
SQL Template Generation
↓
SQLite Query Execution
↓
Results + Visualization
```

The application uses deterministic NLP logic instead of generative AI models to ensure:

* reliability
* transparency
* deployability
* low cost

---

# ⚙️ Technologies Used

| Technology                    | Purpose                        |
| ----------------------------- | ------------------------------ |
| Python                        | Core programming language      |
| Streamlit                     | Web application framework      |
| SQLite                        | Lightweight analytics database |
| Pandas                        | Data querying & processing     |
| Faker                         | Synthetic dataset generation   |
| Matplotlib / Streamlit Charts | Data visualization             |

---

# 📂 Project Structure

```text
analytics-qa-agent/
│
├── app.py
├── generate_data.py
├── database.py
├── query_engine.py
├── analytics.db
├── requirements.txt
└── README.md
```

---

# 📄 File Responsibilities

---

## `app.py`

Main Streamlit application.

Responsibilities:

* User interface
* Natural-language question input
* Display generated SQL
* Display analytics results
* Render charts and visualizations
* Handle ambiguity errors

This file controls the frontend experience.

---

## `generate_data.py`

Synthetic dataset generator.

Responsibilities:

* Create mock analytics tables
* Generate realistic synthetic users/sessions/revenue data
* Populate SQLite database

Generated tables:

* `users`
* `sessions`
* `transactions`

The Faker library was used to simulate realistic production-like data.

---

## `database.py`

Database execution layer.

Responsibilities:

* Connect to SQLite database
* Execute generated SQL
* Return results as Pandas DataFrames

This separates database logic from frontend logic.

---

## `query_engine.py`

Natural-language → SQL conversion engine.

Responsibilities:

* Detect user intent
* Match keywords
* Generate safe SQL templates

Examples:

* DAU queries
* MAU queries
* Revenue queries
* Weekly comparisons
* Retention queries

This is the core “AI-assisted” logic layer.

---

## `analytics.db`

SQLite database file containing synthetic analytics data.

Stores:

* user activity
* session history
* transaction records

---

# 🧪 Dataset Design

Synthetic analytics data was generated using:

* random user activity
* multiple countries
* signup dates
* sessions
* transactions

Approximate dataset size:

* 5,000 users
* 50,000 sessions
* 10,000 transactions

This simulates a realistic product analytics environment.

---

# 🧠 Why SQLite Was Chosen

SQLite was selected because:

* lightweight
* easy deployment
* no server required
* beginner-friendly
* ideal for prototypes

For interview/demo projects, SQLite provides sufficient realism without infrastructure complexity.

---

# 🧠 NLP / Query Generation Strategy

Instead of using a Large Language Model (LLM), the system uses:

* keyword matching
* intent classification
* SQL template mapping

Example:

```text
“What was our DAU?”
```

maps to:

```sql
SELECT session_date,
COUNT(DISTINCT user_id) as dau
FROM sessions
GROUP BY session_date
```

---

# ❓ Why NOT Use LLMs?

Initially, an LLM-based approach was considered.

However, deterministic query generation was intentionally chosen because it offers several advantages for analytics systems.

---

# ✅ Advantages Over LLM-Based SQL Generation

| Deterministic SQL | LLM SQL              |
| ----------------- | -------------------- |
| Reliable          | Can hallucinate      |
| Safe              | Risk of invalid SQL  |
| Fast              | Higher latency       |
| Cheap             | API cost             |
| Easy deployment   | Heavy dependencies   |
| Explainable       | Black-box generation |

---

# ⚠️ Problems With Local LLMs

In previous experiments with local transformer models:

* PyTorch DLL errors occurred
* deployment became unstable
* startup time increased
* memory usage became high
* free hosting became difficult

The deterministic approach solved these issues completely.

---

# 🧠 Hallucination Prevention

One major challenge in AI analytics systems is hallucinated or unsafe SQL.

This project avoids that problem by:

* generating only pre-approved SQL templates
* limiting accessible tables
* avoiding arbitrary SQL execution

This guarantees:

* valid SQL
* safe execution
* predictable behavior

---

# ❓ Handling Ambiguous Questions

If the system cannot confidently determine intent, it asks the user for clarification instead of guessing.

Example:

```text
“How are users doing?”
```

Response:

```text
Please clarify which metric you mean:
- DAU
- MAU
- Revenue
- Retention
```

This improves trust and avoids misleading analytics answers.

---

# 📊 Supported Analytics Queries

Currently supported:

* DAU (Daily Active Users)
* MAU (Monthly Active Users)
* Revenue
* US-only users
* Weekly comparisons
* Retention-style queries

---

# 📈 Visualization Layer

The app automatically visualizes results using:

* line charts
* tables
* metrics

This improves readability and makes the system feel closer to real analytics platforms.

---

# 🎨 UI Design Decisions

The UI was designed using:

* light SaaS-style theme
* glassmorphism cards
* animated transitions
* clean dashboard layout

Goals:

* modern appearance
* interview-ready presentation
* improved usability

---

# 🚀 Deployment

The application is deployed using:

* GitHub
* Streamlit Cloud

Advantages:

* free hosting
* automatic redeployment
* easy sharing

---

# 📦 Installation & Local Setup

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Generate database

```bash
python generate_data.py
```

---

## Run application

```bash
python -m streamlit run app.py
```

---

# 🧠 Evaluation Strategy

The system can be evaluated on:

## 1. Query Accuracy

Did the correct SQL get generated?

## 2. Result Accuracy

Does the returned result match expected analytics values?

## 3. Ambiguity Detection

Did the system correctly request clarification when needed?

## 4. SQL Safety

Did the system avoid invalid or unsafe SQL?

---

# 📈 Production Scaling Strategy

For production systems with:

* 100+ tables
* millions of rows

future improvements would include:

## Semantic Layer

Business metric definitions.

## Schema Metadata Indexing

Understanding relationships between tables.

## Query Planner

Selecting optimal tables automatically.

## Embeddings / Vector Search

Semantic query understanding.

## Warehouse Integration

Snowflake / BigQuery / Redshift support.

## Caching Layer

Reuse answers for repeated queries.

---

# ⚠️ Current Limitations

The current version:

* uses rule-based NLP
* supports limited analytics intents
* does not understand highly complex questions
* requires predefined SQL templates

However, this tradeoff was intentionally made to prioritize:

* reliability
* explainability
* deployment stability

---

# 🧠 Key Engineering Decision

The most important engineering decision was:

> prioritizing deterministic analytics query generation over generative AI.

This improved:

* correctness
* safety
* deployment simplicity
* user trust

---

# 🎯 Future Improvements

Possible future enhancements:

* Dynamic SQL planning
* Multi-table joins
* Better NLP understanding
* Conversational analytics memory
* Dashboard generation
* Export to CSV/Excel
* Role-based access control
* Real warehouse integration

---

# 👨‍💻 Final Outcome

The final application demonstrates:

* natural-language analytics interfaces
* SQL generation pipelines
* analytics system design
* ambiguity handling
* safe query execution
* modern web app deployment

while remaining:

* lightweight
* fully local
* API-free
* deployable on free infrastructure.
