import streamlit as st

st.title("QUER CASAR COMIGO IZA? 💍")

st.write("")

col1, col2 = st.columns(2)

with col1:
    sim = st.button("SIM, ACEITO 💍")

with col2:
    nao = st.button("NÃO, VSFDR 🖕🏻")

if sim:
    st.success("EU SABIA KKKK 💍")
    st.balloons()
    st.markdown(
        "[💖 Clique aqui para ver o vídeo 💖](https://youtu.be/flgwJBAimzg?si=A0Lgza5KV8nzB4yt)",
        unsafe_allow_html=True
    )

elif nao:
    st.error("Resposta errada 😡")
    st.markdown(
        "[😤 Clique aqui 😤](https://youtube.com/shorts/ZYZeL1OXnPE?si=EGD2GwZZsXcaoH6U)",
        unsafe_allow_html=True
    )

st.write("---")
st.subheader("DE: Cayo (seu amor) 🤍")
st.subheader("PARA: Izabelly (meu amor) 🤍")
