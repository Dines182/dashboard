import streamlit as st

def about_us():
    st.title("👥 About Us")
    st.markdown("---")

    # Supervisor section
    st.subheader("👨‍🏫 Supervisor")
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("https://via.placeholder.com/120", width=100)  # AI face or placeholder
        with col2:
            st.markdown("""
            **Name:** Dr. Alex Johnson  
            **Email:** alex.johnson@university.edu  
            **Role:** Project Supervisor  
            **Affiliation:** Department of Data Science, XYZ University  
            """)
    st.markdown("---")

    # Team Members
    st.subheader("👨‍💻 Team Members")
    team = [
        {
            "name": "Sonish Khanal",
            "email": "sonish.khanal@email.com",
            "role": "Dashboard Developer",
            "img": "https://via.placeholder.com/120"
        },
        {
            "name": "Dinesh Karki",
            "email": "Dinesh@email.com",
            "role": "Data Analyst",
            "img": "https://via.placeholder.com/120"
        },
        {
            "name": "Ibhramin Khan",
            "email": "Ibhramin@email.com",
            "role": "Model Trainer",
            "img": "https://via.placeholder.com/120"
        },
        {
            "name": "Sailesh Kc",
            "email": "Sailesh@email.com",
            "role": "Research & Report",
            "img": "https://via.placeholder.com/120"
        },
    ]

    cols = st.columns(4)
    for i, member in enumerate(team):
        with cols[i]:
            st.image(member["img"], width=100)
            st.markdown(f"""
            **{member['name']}**  
            *{member['role']}*  
            📧 [{member['email']}](mailto:{member['email']})
            """)

    st.markdown("---")
    st.info("Thank you for exploring our Diabetes Visualization Project!")

