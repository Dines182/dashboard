import streamlit as st
import pandas as pd

def statis():
    # Load dataset
    df = pd.read_csv("cleaned_diabetes_data.csv")

    # Check for required column
    if 'Diabetes_012' not in df.columns:
        st.error("Dataset must include a 'Diabetes_012' column to use this dashboard.")
        return

    # Sidebar: Diabetes status selector
    st.sidebar.markdown("### Data by Diabetes Status")
    diabetes_labels = {
        0: "No Diabetes",
        1: "Pre-diabetic",
        2: "Diabetic"
    }

    selected_status = st.sidebar.selectbox(
        "Select Diabetes Status",
        sorted(df["Diabetes_012"].unique()),
        format_func=lambda x: diabetes_labels.get(x, str(x))
    )

    # Filter data for the selected diabetes status
    filtered_df = df[df["Diabetes_012"] == selected_status]

    st.markdown("## 📊 Summary Statistics by Diabetes Status")
    st.markdown(f"### Status: {diabetes_labels[selected_status]}")

    # Columns to summarize
    binary_cols = [
        "HighBP", "HighChol", "CholCheck", "Smoker", "Stroke",
        "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
        "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "DiffWalk"
    ]
    numeric_cols = [
        "BMI", "GenHlth", "MentHlth", "PhysHlth", "Age", "Education", "Income"
    ]

    # Calculate means for all columns
    binary_means = filtered_df[binary_cols].mean().multiply(100).round(2)
    numeric_means = filtered_df[numeric_cols].mean().round(2)

    # Combine and rename for clarity
    summary = pd.concat([binary_means, numeric_means]).rename({
        "HighBP": "% with High Blood Pressure",
        "HighChol": "% with High Cholesterol",
        "CholCheck": "% Had Cholesterol Check",
        "Smoker": "% Smokers",
        "Stroke": "% with Stroke History",
        "HeartDiseaseorAttack": "% with Heart Disease or Attack",
        "PhysActivity": "% Physically Active",
        "Fruits": "% Eat Fruits Daily",
        "Veggies": "% Eat Veggies Daily",
        "HvyAlcoholConsump": "% Heavy Alcohol Consumers",
        "AnyHealthcare": "% with Any Healthcare",
        "NoDocbcCost": "% Skipped Doctor Due to Cost",
        "DiffWalk": "% Have Walking Difficulty",
        "BMI": "Average BMI",
        "GenHlth": "Average General Health (1=Excellent to 5=Poor)",
        "MentHlth": "Avg Mental Health Days (Last 30 Days)",
        "PhysHlth": "Avg Physical Health Days (Last 30 Days)",
        "Age": "Average Age",
        "Education": "Average Education Level (1–6)",
        "Income": "Average Income Level (1–8)"
    })

    # Format for display
    summary_df = pd.DataFrame(summary).reset_index()
    summary_df.columns = ["Metric", "Value"]

    st.dataframe(summary_df, use_container_width=True)
