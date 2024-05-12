import pickle
import numpy as np
import streamlit as st

file = open("pickle_553243_ives_202401_CP2.pickle", 'rb')
model = pickle.load(file)


def main():
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">
    Classification Model Penguin Sizes</h2>
    <p>Dataset: <a>https://www.kaggle.com/datasets/amulyas/penguin-size-dataset</a></p> 
    <p>GitHub: <a>https://github.com/IvesJc/cp6-chatbot</p>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    parametro1 = st.number_input('tamanho_peng')
    parametro2 = st.number_input('profund_peng')
    parametro3 = st.number_input('nadadeira_peng')
    parametro4 = st.number_input('peso_peng')

    entrada = np.array([[parametro1, parametro2, parametro3, parametro4]])
    resultado = model.predict(entrada)

    st.success(resultado)

    return resultado


if __name__ == '__main__':
    main()
