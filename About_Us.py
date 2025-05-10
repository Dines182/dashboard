import streamlit as st

def about_us():
    st.title("👥 About Us")
    st.markdown("---")

    # Supervisor section
    st.subheader("👨‍🏫 Supervisor")
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("image.jpg", width=100)  # AI face or placeholder
        with col2:
            st.markdown("""
            **Name:** Md Rafiqul Islam  
            **Email:** mdrafiqul.islam@cdu.edu.au
            
            **Affiliation:** Department of Information Technology, CDU University  
            """)
    st.markdown("---")

    # Team Members
    st.subheader("👨‍💻 Team Members")
    team = [
        {
            "name": "Sonish Khanal",
            "email": "sonish.khanal@students.cdu.edu.au",
            "role": "Dashboard Developer",
            "img": "image.jpg"
        },
        {
            "name": "Dinesh Karki",
            "email": "dinesh.karki@students.cdu.edu.au",
            "role": "Data Analyst",
            "img": "image.jpg"
        },
        {
            "name": "Ibhramin Khan",
            "email": "ibrahim.salman@students.cdu.edu.au",
            "role": "Model Trainer",
            "img": "image.jpg"
        },
        {
            "name": "Sailesh Kc",
            "email": "sailesh.kc@students.cdu.edu.au",
            "role": "Research & Report",
            "img": "image.jpg"
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

