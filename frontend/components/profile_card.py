# app/frontend/components/profile_card.py

import streamlit as st

def profile_card(user_data: dict):
    """
    Renders a profile summary card on the frontend using Streamlit.

    Parameters:
    - user_data (dict): Dictionary containing user details like name, email, skills, etc.
    """

    # Card container with stylized background
    with st.container():
        st.markdown("""
            <style>
                .profile-card {
                    background-color: #f0f2f6;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }
                .profile-title {
                    font-size: 22px;
                    font-weight: 700;
                    color: #262730;
                }
                .profile-label {
                    font-weight: 600;
                    color: #40444b;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="profile-card">', unsafe_allow_html=True)

        st.markdown(f"""
            <div class="profile-title">👤 {user_data.get('name', 'N/A')}</div>
            <p><span class="profile-label">📧 Email:</span> {user_data.get('email', 'N/A')}</p>
            <p><span class="profile-label">🎓 Qualification:</span> {user_data.get('qualification', 'N/A')}</p>
            <p><span class="profile-label">🛠️ Skills:</span> {', '.join(user_data.get('skills', []))}</p>
            <p><span class="profile-label">📂 Domain Interest:</span> {', '.join(user_data.get('interests', []))}</p>
            <p><span class="profile-label">🌐 Experience Level:</span> {user_data.get('experience', 'N/A')}</p>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
