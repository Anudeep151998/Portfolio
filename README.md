# 👨‍💻 Personal Portfolio: Data Engineer & Data Analyst

An interactive, responsive, and modern portfolio web application built with **Streamlit** and styled with custom **CSS/HTML**. This application showcases my professional journey, technical projects, skills, education, and credentials in the fields of Data Engineering and Data Analytics.

---

## 🚀 Live Demo

You can view the live, fully interactive application here:
👉 **[Live Portfolio Link](https://portfolioanu.streamlit.app/)** *(Streamlit Community Cloud)*

---

## 🛠️ Tech Stack & Tools

* **Frontend:** Streamlit, Custom CSS Injection, HTML5
* **Language:** Python 3.x
* **Core Libraries:** Pandas, NumPy
* **Hosting & Deployment:** Streamlit Community Cloud / Render
* **Infrastructure Monitoring:** Cron-job.org (Keep-alive pinging)

---

## 🌟 Key Features

* **Dynamic Navigation:** Smooth tab switching (`Home`, `About`, `Projects`, `Skills`, `Experience`, `Education`, `Achievements`, `Contact`).
* **Visual Polish:** Customized dark-mode theme featuring glowing visual elements, sleek cards, and a modern layout.
* **Resume Access:** Direct download buttons for specialized resumes (e.g., Data Engineer CV, Data Analyst CV).
* **Interactive Contact Portal:** Direct links to email clients (Gmail/Outlook) and social profiles.
* **Responsive Layout:** Optimized to look great on desktop monitors, tablets, and mobile devices.

---

## 📁 Repository Structure

```text
├── .github/workflows/
│   └── keep_alive.yml     # Automated workflow to keep Streamlit awake
├── app.py                  # Main Streamlit application and layout logic
├── data.py                 # Centralized portfolio data dictionary (PROFILE)
├── requirements.txt        # Production dependencies
├── render.yaml             # Render deployment blueprint (Free tier)
└── README.md               # Project documentation (this file)