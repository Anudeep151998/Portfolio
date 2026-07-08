PROFILE = {
    "name": "Anudeep Burra",
    "title": "Data Analyst | Data Engineer | python · SQL · ETL Pipelines · Cloud (AWS)",
    "tagline": "MSc Computing (Merit) · 2+ Years Enterprise Experience · Sheffield, UK",
    "phone": "+44 7587 975094",
    "summary": (
    "Data Engineer & Analyst with 2+ years of professional IT experience and an MSc in Computing "
    "(Merit) from Sheffield Hallam University. Designed and deployed a production-style end-to-end "
    "ETL pipeline in Python using Medallion Architecture (Bronze/Silver/Gold), ingesting live job "
    "market data via REST API, validating it through a custom circuit breaker, and loading it into "
    "a cloud PostgreSQL database on a fully automated daily schedule via SQLAlchemy. "
    "Skilled in SQL, Pandas, and data modelling — built a Streamlit analytics dashboard processing "
    "260,000+ records with 6+ analytical SQL queries for KPI reporting and trend analysis. "
    "Strong foundation in SQL-based data validation and quality assurance from enterprise banking/CRM "
    "systems at Infosys, where 50+ data discrepancies were identified and resolved. "
    "Comfortable across the full data lifecycle — ingestion, transformation, warehousing, and "
    "visualisation — with hands-on AWS cloud experience (EC2, CloudWatch, boto3). "
    "UK Graduate Route Visa holder — eligible to start immediately, no sponsorship required."
),
    "location": "Sheffield, UK",
    "email_gmail": "anudeepburra18@gmail.com",
    "email_outlook": "anuburra18@outlook.com",
    "linkedin": "https://linkedin.com/in/anudeepburra",
    "github": "https://github.com/Anudeep151998",
    "visa": "UK Graduate Route Visa — No Sponsorship Required",
}

CVS = [
    {"label": "📊 Data Engineer CV",  "file": "Anudeep_DE.pdf",                        "description": "ETL · Python · SQL · PostgreSQL · AWS"},
    {"label": "🧪 Data Analyst CV",    "file": "Anudeep_Burra_DataAnalyst_CV.pdf", "description": "Selenium · pytest · SQL · Jira · HP ALM"},
]

STATS = [
    ("2+",    "Years Enterprise\nExperience", "@ Infosys"),
    ("5",     "Projects\nDeployed",           "Live & on GitHub"),
    ("260K+", "Records\nAnalysed",            "IPL Dataset"),
    ("100%",  "Selenium\nPass Rate",          "20+ Test Cases"),
]

PROJECTS = [
    {
        "emoji": "📊",
        "title": "Automated Job Market Intelligence Pipeline",
        "category": "Data Engineering",
        "status": "🟢 Live",
        "impact": "Fully automated — runs daily, zero manual intervention",
        "description": (
            "Production-style ETL pipeline that ingests live job postings daily from the Adzuna REST API, "
            "transforms nested JSON with Pandas, and loads clean structured data into a cloud PostgreSQL "
            "database (Supabase) via SQLAlchemy. Runs on a serverless cron schedule on Render Cloud."
        ),
        "highlights": [
            "Medallion Architecture — Bronze (raw ingestion), Silver (cleaning), Gold (production load)",
            "Custom circuit breaker — auto-halts on schema drift, empty payloads or API failures",
            "Idempotent SQLAlchemy upserts — re-runs update records without primary key conflicts",
            "Serverless cron on Render Cloud — zero idle hosting cost",
            "CI/CD via GitHub to Render — pushes to main trigger automatic redeployment",
            "100% secure — all credentials in environment variables, zero hardcoded secrets",
        ],
        "tech": ["Python", "Pandas", "SQLAlchemy", "PostgreSQL", "Supabase", "Render", "CI/CD", "REST API"],
        "live_url": "https://job-market-intelligence-pipeline-ceutn5wjpjh5yzxabjpabf.streamlit.app/",
        "github_url": "https://github.com/Anudeep151998/job-market-intelligence-pipeline",
    },
    {
        "emoji": "🏏",
        "title": "IPL Data Analysis Dashboard",
        "category": "Data Analytics",
        "status": "🟢 Live",
        "impact": "260,000+ records analysed across 13 IPL seasons",
        "description": (
            "End-to-end data analytics project on 260,000+ ball-by-ball IPL records (2008-2020). "
            "Ingested into SQLite, analysed with 6 deep SQL queries, and visualised in a 4-chart "
            "interactive Streamlit dashboard with season filters and KPI cards."
        ),
        "highlights": [
            "260,000+ ball-by-ball records ingested and processed with Python and Pandas",
            "6 analytical SQL queries covering team performance, top batsmen/bowlers, toss decisions",
            "Win-rate analysis: batting first vs chasing, player-of-the-match leaderboards",
            "4-chart Streamlit dashboard with Matplotlib/Seaborn deployed on Streamlit Cloud",
        ],
        "tech": ["Python", "SQL", "SQLite", "Pandas", "Matplotlib", "Seaborn", "Streamlit"],
        "live_url": "https://ipl-data-analysis-dashboard.streamlit.app/",
        "github_url": "https://github.com/Anudeep151998",
    },
    {
        "emoji": "☁️",
        "title": "AWS CloudWatch EC2 Monitoring System",
        "category": "Cloud & Infrastructure",
        "status": "✅ Complete",
        "impact": "Full end-to-end cloud alerting pipeline on AWS",
        "description": (
            "Built from scratch on AWS — provisioned an EC2 Ubuntu instance, configured IAM credentials "
            "and AWS CLI, then wrote Python (boto3) scripts to monitor CloudWatch CPU metrics every "
            "5 minutes and trigger SNS email alerts above 70% utilisation."
        ),
        "highlights": [
            "Provisioned EC2 Ubuntu instance — IAM credentials, AWS CLI and security groups configured",
            "Python (boto3) scripts listing running instances and pulling live CloudWatch CPU metrics",
            "SNS email alerts auto-triggered above 70% CPU — full end-to-end alerting pipeline",
            "Demonstrates production monitoring pattern used in real cloud operations roles",
        ],
        "tech": ["AWS EC2", "CloudWatch", "SNS", "Python", "boto3", "IAM", "Linux"],
        "live_url": None,
        "github_url": "https://github.com/Anudeep151998/cloudwatch-monitor",
    },
    {
        "emoji": "🧪",
        "title": "Selenium Automation Framework",
        "category": "QA & Test Automation",
        "status": "✅ Complete",
        "impact": "20+ tests — 100% pass rate",
        "description": (
            "Enterprise-grade Selenium/Python automation framework covering 20+ automated scenarios "
            "(login, products, checkout) with 100% pass rate. Structured with Page Object Model for "
            "clean separation of test logic; integrated with pytest and pytest-html for reporting."
        ),
        "highlights": [
            "20+ automated test cases — 100% pass rate on every run",
            "Page Object Model (POM) — clean separation of test logic and page interactions",
            "pytest with pytest-html reporting for stakeholder visibility",
            "Mirrors the Selenium WebDriver work that cut regression effort ~30% at Infosys",
        ],
        "tech": ["Python", "Selenium", "pytest", "Page Object Model", "pytest-html", "Java", "TestNG"],
        "live_url": None,
        "github_url": "https://github.com/Anudeep151998/selenium-automation-framework",
    },
    {
        "emoji": "🛠️",
        "title": "IT Support Toolkit",
        "category": "IT Support",
        "status": "🟢 Live",
        "impact": "Full 1st/2nd/3rd line support dashboard — live on Streamlit Cloud",
        "description": (
            "Live multi-tier IT support dashboard covering 1st, 2nd, and 3rd line support. "
            "Features a helpdesk ticketing system with SQLite backend, real-time network diagnostics, "
            "and live system health monitoring via psutil."
        ),
        "highlights": [
            "Helpdesk ticketing system with full ticket lifecycle management in SQLite",
            "Network diagnostics: ping, port scanning, DNS lookup in real-time",
            "Live system health: CPU, RAM, disk usage alerts via psutil",
            "Deployed live on Streamlit Community Cloud — accessible from any browser",
        ],
        "tech": ["Python", "Streamlit", "SQLite", "psutil", "socket", "DNS"],
        "live_url": "https://it-support-toolkit-automation.streamlit.app",
        "github_url": "https://github.com/Anudeep151998",
    },
]

SKILLS = {
    "📊 Data Engineering": {
        "items": ["Python", "Pandas", "NumPy", "SQLAlchemy", "PostgreSQL", "MySQL",
                  "SQLite", "ETL/ELT Pipelines", "REST API Ingestion", "Supabase",
                  "Render Cloud", "Cron Scheduling", "CI/CD", "python-dotenv"],
    },
    "📈 Analytics & Visualisation": {
        "items": ["SQL", "Matplotlib", "Seaborn", "Plotly", "Streamlit",
                  "Data Modelling", "Schema Design", "KPI Dashboards"],
    },
    "☁️ Cloud & Infrastructure": {
        "items": ["AWS EC2", "AWS IAM", "CloudWatch", "SNS", "S3",
                  "Linux (Ubuntu)", "Nginx", "Gunicorn", "Django",
                  "SSH", "Security Groups", "boto3", "Bash"],
    },
    "🧪 QA & Test Automation": {
        "items": ["Selenium WebDriver", "pytest", "TestNG", "JUnit",
                  "Page Object Model", "HP ALM", "Jira",
                  "Postman", "API Testing", "Java"],
    },
    "🔧 Tools & Workflow": {
        "items": ["Git", "GitHub", "GitHub Actions", "VS Code",
                  "Agile / Scrum", "SDLC", "STLC", "Linux CLI"],
    },
}

PROFICIENCIES = [
    ("Python",                  92),
    ("SQL / PostgreSQL",        88),
    ("Pandas / Data Wrangling", 88),
    ("ETL Pipeline Design",     85),
    ("Streamlit",               85),
    ("Selenium / pytest",       82),
    ("SQLAlchemy",              80),
    ("AWS EC2 / IAM / CW",      75),
]

EXPERIENCE = [
    {
        "role": "Test Engineer — QA & Application Support",
        "company": "Infosys Ltd",
        "period": "Apr 2022 – Dec 2023",
        "duration": "22 months",
        "location": "India",
        "type": "Full-time",
        "points": [
            "Delivered end-to-end QA for enterprise CRM and core banking applications across 5+ production releases",
            "Designed and executed 200+ structured test cases per release using HP ALM — maintained zero critical-defect escape rate across 3 consecutive releases",
            "Built Selenium WebDriver (Java) regression automation, cutting manual regression effort by ~30% per sprint",
            "Performed backend SQL data validation and migration testing — identified and resolved 50+ data discrepancies",
            "Owned the full defect lifecycle in Jira, collaborating cross-functionally with developers and BAs in Agile teams",
            "Awarded Best Performer on the DDO Project for quality and delivery",
        ],
    },
    {
        "role": "Systems Engineer (Training)",
        "company": "Infosys Ltd",
        "period": "Jan 2022 – Mar 2022",
        "duration": "3 months",
        "location": "India",
        "type": "Full-time",
        "points": [
            "Completed structured training in SDLC, STLC, Agile, Java SE 8 and Selenium WebDriver",
            "Certified in Agile Developer and Java SE 8 — both issued by Infosys",
        ],
    },
    {
        "role": "Data Science Intern",
        "company": "Innomatics Research Labs",
        "period": "Aug 2021 – Dec 2021",
        "duration": "5 months",
        "location": "India",
        "type": "Internship",
        "points": [
            "Completed data science internship focused on Python, data analysis and visualisation using NumPy, Pandas, Matplotlib and Seaborn",
            "Built interactive dashboards with Streamlit and a web app with Flask",
        ],
    },
]

EDUCATION = [
    {
        "degree": "MSc Computing",
        "institution": "Sheffield Hallam University",
        "location": "Sheffield, United Kingdom",
        "grade": "Merit",
        "period": "2024 – 2025",
        "highlights": [
            "Specialised in  cloud computing, and software engineering",
            "3rd Place — Cloud Computing Hackathon, Sheffield Hallam University",
            
        ],
    },
    {
        "degree": "B.Tech — Electronics & Communication Engineering",
        "institution": "Guru Nanak Institutions Technical Campus",
        "location": "India",
        "grade": "First Class",
        "period": "2016 – 2020",
        "highlights": [
            "Core foundation in electronics, computer science, algorithms, and software development",
            "Developed programming skills in Java, c, and SQL",
        ],
    },
]

CERTIFICATIONS = [
    ("☁️", "Skills & Best Practices for Cloud Support Associates", "Coursera"),
    ("🗄️", "Introduction to SQL", "SimpliLearn (SkillUp)"),
    ("☁️", "Introduction to Information Technology & AWS Cloud", "Coursera"),
    ("🏗️", "Cloud Platform Job Simulation", "Forage"),
    ("🏃", "Agile Developer Certification", "Infosys"),
    ("☕", "Java SE 8 Certification", "Infosys"),
    ("🧪", "Selenium Automation Testing", "Infosys"),
    ("🐍", "Crash Course on Python", "Coursera"),
]

ACHIEVEMENTS = [
    ("🏆", "Best Performer Award", "Infosys — DDO Project", "Zero-defect delivery and outstanding cross-functional collaboration"),
    ("🥉", "3rd Place — Cloud Computing Hackathon", "Sheffield Hallam University", "Competed against MSc peers in a live cloud infrastructure challenge"),
    ("✅", "Zero Critical Defect Escape Rate", "Infosys", "Maintained across 3 consecutive production releases for enterprise banking client"),
    ("📊", "200+ Test Cases Per Release", "Infosys", "Designed and executed structured test suites across 5+ production releases"),
]

OPEN_TO = [
    ("📊", "Junior Data Engineer"),
    ("📈", "Junior Data Analyst"),
    ("💻", "Graduate Software Engineer"),
]