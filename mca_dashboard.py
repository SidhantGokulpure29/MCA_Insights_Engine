
import pandas as pd
import streamlit as st
import plotly.express as px

def generate_daily_summary(change_log_path):
    df = pd.read_csv(change_log_path)

    new_incos = df[df['Change_Type'] == 'New Incorporation'].shape[0]
    removals = df[df['Change_Type'] == 'Deregistered'].shape[0]
    updates = df[df['Change_Type'] == 'Field Update'].shape[0]

    summary = f"📋 Daily Summary\nNew incorporations: {new_incos}\nDeregistered: {removals}\nUpdated records: {updates}"
    return summary


# Load datasets
change_log = pd.read_csv('daily_change_log.csv')
enriched_df = pd.read_csv('mca_enriched_dataset.csv')

st.title("📊 MCA Insights Dashboard")
st.markdown("Explore company changes and enriched metadata")

st.subheader("🧠 AI-Generated Daily Summary")
summary_text = generate_daily_summary("daily_change_log.csv")
st.text(summary_text)

# 🔍 Search
search_input = st.text_input("Search by CIN or Company Name")
if search_input:
    enriched_match = enriched_df[
        enriched_df['COMPANY_NAME'].str.contains(search_input, case=False, na=False) |
        enriched_df['CIN'].str.contains(search_input, case=False, na=False)
    ]
    st.subheader("🔎 Search Results")
    st.dataframe(enriched_match)

# 🧭 Filters
year_filter = st.selectbox("Filter by Year", options=sorted(change_log['Date'].unique()))
state_filter = st.multiselect("Filter by State", options=enriched_df['STATE'].unique(), default=enriched_df['STATE'].unique())
status_filter = st.multiselect("Filter by Status", options=enriched_df['STATUS'].unique(), default=enriched_df['STATUS'].unique())

filtered_df = enriched_df[
    (enriched_df['STATE'].isin(state_filter)) &
    (enriched_df['STATUS'].isin(status_filter))
]

# 📈 Change History
change_counts = change_log.groupby(['Date', 'Change_Type']).size().reset_index(name='Count')
fig = px.bar(change_counts, x='Date', y='Count', color='Change_Type', title='Change History Over Time')
st.plotly_chart(fig)

# 🧠 Enriched Info
st.subheader("📋 Enriched Company Records")
st.dataframe(filtered_df)

# 🔗 Source URLs
st.subheader("🔗 Source Links")
for _, row in filtered_df.iterrows():
    st.markdown(f"[{row['COMPANY_NAME']}]({row['SOURCE_URL']})")
