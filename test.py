df = pd.read_csv("university_student_dashboard_data.csv")

# Title
st.title("University Student Dashboard \U0001F393📊")

# Sidebar Filters
st.sidebar.header("Filters")
selected_term = st.sidebar.selectbox("Select Term", df["Term"].unique())
selected_year = st.sidebar.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].max()))

# Filter data
filtered_df = df[(df["Term"] == selected_term) & (df["Year"] == selected_year)]

# KPIs
st.subheader("Key Metrics")
total_apps = filtered_df["Applications"].sum()
total_admissions = filtered_df["Admitted"].sum()
total_enrollments = filtered_df["Enrolled"].sum()
retention_rate = filtered_df["Retention Rate (%)"].mean()
satisfaction_score = filtered_df["Student Satisfaction (%)"].mean()

st.metric("Total Applications", total_apps)
st.metric("Total Admissions", total_admissions)
st.metric("Total Enrollments", total_enrollments)
st.metric("Avg Retention Rate", f"{retention_rate:.2f}%")
st.metric("Avg Satisfaction Score", f"{satisfaction_score:.2f}%")

# Enrollment by Department
st.subheader("Enrollment Breakdown by Department")
dept_counts = filtered_df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
fig, ax = plt.subplots(figsize=(8, 4))
dept_counts.plot(kind="bar", color=["skyblue", "orange", "green", "purple"], ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Department")
plt.ylabel("Enrollments")
plt.title("Enrollments by Department")
st.pyplot(fig)

# Retention Rate Trends
st.subheader("Retention Rate Over Time")
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(data=df, x="Year", y="Retention Rate (%)", hue="Term", marker="o", ax=ax)
plt.xlabel("Year")
plt.ylabel("Retention Rate (%)")
plt.title("Retention Rate Trends Over Time")
st.pyplot(fig)

# Satisfaction Score Comparison
st.subheader("Satisfaction Score: Spring vs Fall")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x="Term", y="Student Satisfaction (%)", ax=ax)
plt.xlabel("Term")
plt.ylabel("Satisfaction Score (%)")
plt.title("Comparison of Student Satisfaction (Spring vs Fall)")
st.pyplot(fig)

# Conclusion
st.write("### Key Findings & Insights")
st.write("- Enrollment trends vary by department, with Engineering and Business leading.")
st.write("- Retention rates have been improving over the years.")
st.write("- Students report slightly higher satisfaction in Fall compared to Spring.")

# Run this script using: `streamlit run script.py`
