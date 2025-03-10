# Loading dataset
data = pd.read_csv("university_student_dashboard_data.csv")

# Title of the dashboard
st.title("University Admissions, Retention, and Satisfaction Dashboard")

# Sidebar for filters
st.sidebar.header("Filters")
year_selected = st.sidebar.selectbox("Select Year", data['Year'].unique())
term_selected = st.sidebar.selectbox("Select Term", data['Term'].unique())

# Filter data based on selection
filtered_data = data[(data['Year'] == year_selected) & (data['Term'] == term_selected)]

# Display key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", filtered_data['Applications'].sum())
col2.metric("Total Admitted", filtered_data['Admitted'].sum())
col3.metric("Total Enrolled", filtered_data['Enrolled'].sum())

# Retention Rate and Satisfaction
st.header("Satisfaction and Retention")
fig1 = px.line(data, x='Year', y='Retention Rate (%)', color='Term', title='Retention Rate Over Time')
st.plotly_chart(fig1)

fig2 = px.line(data, x='Year', y='Student Satisfaction (%)', color='Term', title='Student Satisfaction Over Time')
st.plotly_chart(fig2)

# Departmental Enrollment
st.header("Departmental Enrollment")
department_data = filtered_data.melt(
    id_vars=['Year', 'Term'], 
    value_vars=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled'], 
    var_name='Department', 
    value_name='Students Enrolled'  # Changed value_name to avoid conflict
)
fig3 = px.bar(department_data, x='Department', y='Students Enrolled', color='Department', title='Enrollment by Department')
st.plotly_chart(fig3)

# Spring vs. Fall Comparison
st.header("Spring vs Fall Comparison")
term_comparison = data.groupby(['Year', 'Term']).agg({'Applications': 'sum', 'Admitted': 'sum', 'Enrolled': 'sum', 'Retention Rate (%)': 'mean', 'Student Satisfaction (%)': 'mean'}).reset_index()
fig4 = px.bar(term_comparison, x='Year', y='Applications', color='Term', barmode='group', title='Applications: Spring vs. Fall')
st.plotly_chart(fig4)

# Key Insights
st.header("Key Insights")
st.write("""
- **Engineering** has the highest enrollment compared to other departments or fields.
- Over the years **Retention rates** have been steadily increasing.
- In Fall terms **Student satisfaction** is slightly higher compared to Spring terms.
""")
