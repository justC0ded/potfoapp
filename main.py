import streamlit as st
st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Prosper Ifeanyi")
    content = """
    afakljfdla;jf;ajfajf;lajfdja;djfa;jfa;jd;fja;jf;ajf;ajfa;f
    alfj;ajk;dfja;kdjfa;js;fja;sfja;jf;ajs;lfja;fj;a
    ;ajkfaj;sdfja;lalfa;dlskdfsdflsflsfslfjlslfjsljflssfsfksfls
    slfskjflsjddlsjlfjsljflsjflsjdfjsljflsjflsjflsksjfllsfjlsls

    """
    st.info(content)
