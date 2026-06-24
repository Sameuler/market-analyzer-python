
# Real-Time Stock Market Data Pipeline & Analytics Dashboard

## Project Status: Phase 1 MVP Complete (Paused in June 2026)
This repository represents a fully functional, end-to-end local Minimum Viable Product (MVP). The core engineering objectives of Phase 1—automated ingestion, relational database caching, and responsive user-controlled UI filtering—have been successfully met and tested. 

* **Current Status:** Stable local deployment. 
* **Next Planned Milestone:** Phase 2 (Time-Series Feature Engineering & Rolling Moving Averages) is scheduled for end of July 2026.
---

##  Tech Stack
* **Language:** Python
* **Database:** MySQL 
* **Data Libraries:** Pandas
* **Visualization:** Plotly Express
* **Frontend Framework:** Streamlit

---

##  Key Features Implemented

### 1. Robust Ingestion Loop
* Implemented a 60 seconds rate limit to respect target API endpoints.
* Script interruption allowing data streams to close cleanly without leaving open connections.
---
