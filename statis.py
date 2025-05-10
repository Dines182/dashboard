import streamlit as st
import pandas as pd

def statis():
    # Load dataset
    df = pd.read_csv("cleaned_diabetes_data.csv")

    # Check for required column
    if 'Diabetes_012' not in df.columns:
        st.error("Dataset must include a 'Diabetes_012' column to use this dashboard.")
        return

    st.markdown("## 📊 Summary Statistics by Diabetes Status")
    # Diabetes status mapping
    diabetes_labels = {
        0: "No Diabetes",
        1: "Pre-diabetic",
        2: "Diabetic"
    }

    # Main area selector instead of sidebar
    selected_status = st.selectbox(
        "Select Diabetes Status",
        sorted(df["Diabetes_012"].unique()),
        format_func=lambda x: diabetes_labels.get(x, str(x)),
        index=0
    )

    # Filter data
    filtered_df = df[df["Diabetes_012"] == selected_status]

    # Define columns
    binary_cols = [
        "HighBP", "HighChol", "Smoker", "Stroke",
        "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
        "HvyAlcoholConsump", "DiffWalk"
    ]
    numeric_cols = [
        "BMI", "GenHlth", "Age", "Education", "Income"
    ]

    # Calculate stats
    binary_means = filtered_df[binary_cols].mean().multiply(100).round(2)
    numeric_means = filtered_df[numeric_cols].mean().round(2)

    # Rename and merge
    summary = pd.concat([binary_means, numeric_means]).rename({
        "HighBP": "% with High Blood Pressure",
        "HighChol": "% with High Cholesterol",
        "Smoker": "% Smokers",
        "Stroke": "% with Stroke History",
        "HeartDiseaseorAttack": "% with Heart Disease or Attack",
        "PhysActivity": "% Physically Active",
        "Fruits": "% Eat Fruits Daily",
        "Veggies": "% Eat Veggies Daily",
        "HvyAlcoholConsump": "% Heavy Alcohol Consumers",
        "DiffWalk": "% Have Walking Difficulty",
        "BMI": "Average BMI",
        "GenHlth": "Average General Health (1=Excellent to 5=Poor)",
        "Age": "Average Age",
        "Education": "Average Education Level (1–6)",
        "Income": "Average Income Level (1–8)"
    })

    # Display table within a container with a fixed height
    summary_df = pd.DataFrame(summary).reset_index()
    summary_df.columns = ["Metric", "Value"]
    # Adjust index to start from 1
    summary_df.index = summary_df.index + 1  # Shift the index by 1

    # Use a container for the table
    with st.container():
        # Set the table to be scrollable by defining a fixed height
        st.dataframe(summary_df, use_container_width=True, height=353)  # Adjust the height as needed
