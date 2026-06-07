import streamlit as st
from services.persistence.exercise_repository import get_or_create_user

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🏋️‍♂️ Apna AI Coach</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888; font-size: 1.1rem; margin-bottom: 2rem;'>Your form analyzed and corrected in milliseconds.</p>", unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            st.markdown("### Ready to train?")
            username = st.text_input("Athlete Name", placeholder="e.g. John Doe", label_visibility="collapsed")
            
            st.markdown("<br>", unsafe_allow_html=True)
            submit_button = st.form_submit_button("⚡ START SESSION", width="stretch")

        if submit_button:
            if not username:
                st.error("Please enter an athlete name to begin.")
                return False
            
            user = get_or_create_user(username)
        
            st.session_state["user_id"] = user["id"]
            st.session_state["username"] = user["username"]

            st.rerun()

    return False