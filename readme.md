# 🚀 Brazilian CEP Data Engineering ETL Project

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-24.0+-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A beginner-friendly ETL (Extract, Transform, Load) pipeline that fetches Brazilian address data (CEP - Postal Code) from ViaCEP API, normalizes it, and stores it in PostgreSQL using Docker.

---
## 📊 Project Overview

This project demonstrates a complete data engineering workflow:

- **Extract**: Fetch address data from ViaCEP API based on user CEPs  
- **Transform**: Clean, normalize, and deduplicate data  
- **Load**: Store processed data into PostgreSQL database  

### What You'll Learn

- How to build an ETL pipeline from scratch  
- Working with APIs and data extraction  
- Data cleaning and normalization techniques  
- Database design and operations  
- Docker containerization for databases  
- Using DBeaver for database management  

---

## 🏗️ Architecture

```
📁 project-root/
│
├── 📁 1-bronze-raw/              # Raw data (CSV, JSON)
│   ├── 📄 users.csv             # Input user data with CEPs
│   └── 📄 cep_info.csv          # Raw API responses
│
├── 📁 2-silver-validated/       # Cleaned & normalized data
│   └── 📄 *.parquet             # Deduplicated data
│
├── 📁 3-gold-enriched/          # Final enriched data
│   └── 📄 query.sql             # SQL queries for analysis
│
├── 🐍 get_data.py               # Extract: Fetches data from API
├── 🐍 normalize-data.py         # Transform: Cleans and normalizes
├── 🐍 app.py                    # Load: Inserts data into DB
├── 🐍 db.py                     # Database wrapper class
├── 📓 data-view.ipynb           # Jupyter notebook for analysis
├── 🐳 docker-compose.yml        # Docker configuration
│
└── 🗄️ PostgreSQL Database      # Final data storage
    └── 📊 Tables from Parquet files
```

---

## 🛠️ Technology Stack

| Category              | Technology            | Purpose                        |
|----------------------|----------------------|--------------------------------|
| **Language**         | Python 3.9+          | Core ETL logic                |
| **Database**         | PostgreSQL 16        | Data warehouse               |
| **Containerization** | Docker & Compose     | Containerized database       |
| **Database GUI**     | DBeaver              | Database management          |
| **Data Processing**  | Pandas               | Data manipulation            |
| **DB Adapter**       | Psycopg2             | PostgreSQL connection        |
| **SQL Toolkit**      | SQLAlchemy           | SQL operations               |
| **Storage Format**   | Apache Parquet       | Efficient storage            |
| **API Client**       | Requests             | HTTP requests (ViaCEP)       |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [x] **Docker Desktop** - For running PostgreSQL container  
- [x] **DBeaver** (or any PostgreSQL client) - For database management  
- [x] **Python 3.9+** with pip - For running ETL scripts  
- [x] **Git** - For version control  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/tomilico/cep-etl.git
cd cep-etl

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the ETL Pipeline

```bash
# Step 1: Extract data
python get_data.py

# Step 2: Transform data
python normalize-data.py

# Step 3: Load into PostgreSQL
python app.py
```

---

## 🗄️ Database Management with DBeaver

1. Open DBeaver  
2. Create new PostgreSQL connection  
3. Use credentials from `docker-compose.yml`  
4. Explore tables and run SQL queries  

---

## 📁 File Structure Explained

- **Bronze Layer** → Raw API + user data  
- **Silver Layer** → Cleaned and validated data  
- **Gold Layer** → Analytics-ready data  

---

## 🔍 Sample Queries

```sql
-- Count users per city
SELECT cidade, COUNT(*)
FROM users
GROUP BY cidade;

-- Top states by number of users
SELECT estado, COUNT(*)
FROM users
GROUP BY estado
ORDER BY COUNT(*) DESC;
```

---

## 🚀 Next Steps & Learning Path

- Add logging (logging module)
- Implement Airflow for orchestration
- Add data validation with Great Expectations
- Deploy to cloud (AWS/GCP)

---

- 📺 Tutorial completo do projeto:  
  https://www.youtube.com/watch?v=VuizzwyjEU4
