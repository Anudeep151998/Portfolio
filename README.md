# 📊 Data Engineering & Analytics Portfolio Hub

A production-grade, interactive portfolio ecosystem built using **Streamlit** and styled with custom CSS to showcase end-to-end data pipelines, analytics frameworks, and cloud infrastructure monitoring systems. 

**🔗 Live Portfolio Link:** [Replace with your live Streamlit URL once deployed]

---

## 🎯 Profile Executive Summary
* **Name:** Anudeep Burra
* **Target Roles:** Junior Data Engineer | Junior Data Analyst | Graduate Software Engineer
* **Location:** Sheffield, UK (Eligible to start immediately — **UK Graduate Route Visa**, No Sponsorship Required)
* **Core Stack:** Python, SQL, PostgreSQL, Pandas, SQLAlchemy, AWS (EC2, CloudWatch, SNS, boto3), Streamlit, Selenium, pytest

---

## 🚀 Featured Projects Deployed Within This Ecosystem

### 1. 📊 Automated Job Market Intelligence Pipeline
* **Category:** Data Engineering
* **Core Architecture:** Medallion Architecture (Bronze $\rightarrow$ Silver $\rightarrow$ Gold layers)
* **Infrastructure:** Serverless cron scheduling on Render Cloud connecting to a cloud PostgreSQL (Supabase) warehouse.
* **Key Feature:** Implemented a custom circuit breaker pattern to prevent data corruption during schema drift or empty API payloads. It leverages idempotent SQLAlchemy upserts to avoid primary key conflicts.

### 2. 🏏 IPL Data Analysis Dashboard
* **Category:** Data Analytics
* **Dataset:** 260,000+ ball-by-ball records processed via Pandas and SQLite.
* **Insights:** Powered by 6 complex analytical SQL queries focusing on team win-rates, performance metrics, and KPI tracking through an interactive multi-chart Streamlit interface.

### 3. ☁️ AWS CloudWatch EC2 Monitoring System
* **Category:** Cloud & Infrastructure
* **Implementation:** Provisioned an EC2 Ubuntu instance and built a custom automation pipeline using Python (`boto3`) to pull live metrics and route threshold alerts through AWS SNS to email handlers.

### 4. 🧪 Selenium Automation Framework
* **Category:** QA & Test Automation
* **Design Pattern:** Object-oriented testing built using the **Page Object Model (POM)** pattern, utilizing `pytest` and `pytest-html` reporting to mirror enterprise testing architectures.

---

## 📂 Project Repository Structure

```text
├── app.py              # Main multi-page Streamlit application & interactive routing
├── data.py             # Centralized structured data dictionary containing profile details & metrics
├── requirements.txt    # Application dependencies for cloud deployment
└── README.md           # Technical documentation and repository overview