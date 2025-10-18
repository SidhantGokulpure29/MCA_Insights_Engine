# ✨ MCA Insights Engine  
**Track company evolution with intelligence. No spreadsheets. No guesswork. Just clarity.**  
_Built with Python • pandas • Streamlit • Plotly • Markdown_

**Tags:**  
`Python` `3.9+` `Streamlit` `Change Detection` `Metadata Enrichment` `AI Summary` `Dashboard` `Search` `Chatbot`

---

## 🚀 Deliverables Overview

### 1. ✅ Source Code Repository

This GitHub repo contains:
- `mca_dashboard.py`: Streamlit dashboard with search, filters, and AI summary
- `summary_generator.py`: Optional module for generating daily summaries
- `data_processing/`: Scripts for snapshot comparison and enrichment
- `daily_change_log.csv`: Output of change detection logic
- `mca_enriched_dataset.csv`: Final enriched dataset
- `README.md`: This documentation
- `requirements.txt`: Python dependencies

> 📁 All scripts are modular, well-commented, and ready for deployment or extension.

---

### 2. 🧼 Processed and Cleaned MCA Dataset

Raw MCA snapshots were normalized and cleaned:
- Column names standardized across days
- Missing values handled
- Duplicates removed
- Output: `mca_master_dataset.csv` and `mca_enriched_dataset.csv`

> ✅ Ready for analysis, enrichment, and dashboard integration.

---

### 3. 📅 Daily Change Logs

Three snapshots (`Day 1`, `Day 2`, `Day 3`) were compared to detect incremental changes:
- Field-level updates (e.g., capital, status)
- New incorporations
- Deregistrations

Generated logs:
- `daily_change_log.csv`: Contains `CIN`, `Change_Type`, `Field_Changed`, `Old_Value`, `New_Value`, `Date`

> 🔍 Enables time-based tracking and auditability.

---

### 4. 🌐 Enriched Dataset with Public Info

Merged MCA data with publicly available metadata:
- Added `STATE`, `STATUS`, `INDUSTRY_TAG`
- Constructed `SOURCE_URL` links to ZaubaCorp for each company
- Output: `mca_enriched_dataset.csv`

> 🧠 Enrichment logic is rule-based and extensible for future sources.

---

### 5. 🤖 AI Summary Reports

Automatically generated daily summaries using:
```python
def generate_daily_summary(change_log_path):
    ...
    return summary
```
---

## 6. 🌐 Streamlit Dashboard

Interactive dashboard features:

- 🔍 Search by CIN or Company Name  
- 🧠 AI-generated daily summary  
- 📊 Change history visualization (Plotly)  
- 📋 Enriched company records  
- 🔗 Source links to ZaubaCorp  
- 💬 Chatbot interface (rule-based or LLM-ready)

Run locally:

```bash
streamlit run mca_dashboard.py
```
<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/811d7626-0b35-4a34-a84b-2184a804db99" />
<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/c855d7cd-2d97-4fbe-8cd2-4d21db899ad9" />
<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/406f8301-f5f5-418d-bf9b-e01cd69ba1ed" />
<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/ef0b621d-9f6e-4873-9ee3-932d93bb0d14" />

--- 

## 🏗️ Architecture Overview


Each stage represents a modular component of the pipeline:

- **Raw MCA Snapshots**: Daily CSVs from MCA portal
- **Preprocessing**: Column normalization, deduplication, missing value handling
- **Change Detection**: Field-level comparison across snapshots
- **Enrichment**: Metadata tagging, ZaubaCorp linking, industry classification
- **Dashboard**: Streamlit interface with search, filters, summaries, and chatbot

---

## 💡 Future Enhancements

Planned improvements to extend functionality and impact:

- 🚀 Deploy dashboard to Streamlit Cloud
- 🧠 Add LLM-powered chatbot for natural language queries
- 🔄 Integrate with real-time MCA feeds
- 📈 Build summary archive and trend analytics
