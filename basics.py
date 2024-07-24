import streamlit as st

st.set_page_config(page_icon="😊",page_title="My Portfolio",layout="wide")

st.title("Varshini",anchor=False)

st.subheader("Web Developer") 

with st.container(border=True):
    st.info("Hiii")

col1,col2,col3 =st.columns(3)
with col1:
    with st.expander(label="Know me more",expanded=False):
            st.title("EEEEEEEEEEE")
            st.image("ruturaj_gaikwad.webp")

with col2:
    with st.expander(label="lalalalalla",expanded=False):
            st.title("EEEEEEEEEEE")
with col3:
    with st.expander(label="heheheheh",expanded=False):
            st.title("EEEEEEEEEEE")

