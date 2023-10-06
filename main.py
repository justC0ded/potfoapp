import streamlit as st
import pandas
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

content2 = """
            i lovaldjflajfdlajfkjaldfjaljfdajldfjaldjflajldfjlajdflajdlfjaljdfakd
            aldajfljaldfjlajdfkajldfja;ldjf;ajdf;aj;dfjaldjfaljdflajdlfjaljfdlajf

           """
st.write(content2)
df = pandas.read_csv("data.csv",sep=";")
col3,emptycol,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[source code] {row['url']} ")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")