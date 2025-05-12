import streamlit as st
import pandas as pd
import plotly.express as px

def visual():

    # Load your cleaned diabetes dataset
    df = pd.read_csv('cleaned_diabetes_data.csv')

    # Preprocessing
    # Step 1: Ensure the 'Sex' column is numeric and fix any values greater than 0.5
    df['Sex'] = df['Sex'].apply(lambda x: 1 if x > 0.5 else 0)  # Binarizing

    # Step 2: Map to readable labels
    df['Sex_Label'] = df['Sex'].map({0: 'Female', 1: 'Male'})  # Mapping to 'Female' and 'Male'

    # Check the unique values to ensure the mapping is applied correctly
    df['Diabetes_Status'] = df['Diabetes_012'].map({0: 'No Diabetes', 1: 'Pre-Diabetes', 2: 'Diabetes'})
    df['Income_Label'] = df['Income'].map({
        1: '< $10k', 2: '$10-15k', 3: '$15-20k', 4: '$20-25k',
        5: '$25-35k', 6: '$35-50k', 7: '$50-75k', 8: '> $75k'
    })

    st.title("📊 Visualisation of Diabetes Analysis")

    # --- Filters on Main Page ---
    st.markdown("### 🔍 Filters")
    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        sex_filter = st.selectbox("Sex", options=["All"] + df['Sex_Label'].unique().tolist())
    with filter_col2:
        income_filter = st.selectbox("Income Group", options=["All"] + df['Income_Label'].dropna().unique().tolist())
    with filter_col3:
        age_range = st.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (5, 20))

    # Apply filters
    filtered_df = df.copy()
    if sex_filter != "All":
        filtered_df = filtered_df[filtered_df['Sex_Label'] == sex_filter]
    if income_filter != "All":
        filtered_df = filtered_df[filtered_df['Income_Label'] == income_filter]
    filtered_df = filtered_df[(filtered_df['Age'] >= age_range[0]) & (filtered_df['Age'] <= age_range[1])]

    # --- Visualizations ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("BMI vs Age")
        st.plotly_chart(
            px.scatter(filtered_df, x="BMI", y="Age", color="Diabetes_Status"),
            use_container_width=True
        )
    with col2:
        st.subheader("HighBP vs BMI")
        st.plotly_chart(
            px.scatter(filtered_df, x="HighBP", y="BMI", color="Diabetes_Status"),
            use_container_width=True
        )
    with col3:
        st.subheader("Diabetes Status Pie")
        st.plotly_chart(
            px.pie(filtered_df, names="Diabetes_Status"),
            use_container_width=True
        )

    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("BMI Histogram")
        st.plotly_chart(
            px.histogram(filtered_df, x="BMI", color="Diabetes_Status", nbins=30),
            use_container_width=True
        )
    with col5:
        st.subheader("Income vs Diabetes Status")
        st.plotly_chart(
            px.box(filtered_df, x="Diabetes_Status", y="Income", color="Diabetes_Status"),
            use_container_width=True
        )
    with col6:
        st.subheader("Correlation Heatmap")
        st.plotly_chart(
            px.imshow(
                filtered_df.select_dtypes(include=['int64', 'float64']).corr(),
                text_auto=True,
            ),
            use_container_width=True
        )
    
        # --- New Row: Full Width Gender vs Diabetes Status ---
    st.subheader("Male vs Female Distribution")
    gender_diabetes_df = df.groupby(['Sex_Label', 'Diabetes_Status']).size().reset_index(name='Count')

    fig_gender = px.bar(
        gender_diabetes_df,
        x='Sex_Label',
        y='Count',
        color='Diabetes_Status',
        barmode='group',
    )

    st.plotly_chart(fig_gender, use_container_width=True)
