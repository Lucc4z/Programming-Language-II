import streamlit as st
import pandas as pd

class Matriz:
    def __init__(self, datos):
        self.__datos = pd.DataFrame(datos)

    def save_and_show(self, data, title, filename):
        st.write(title)
        st.write(data)
        data.to_csv(f'{filename}.txt', index=False, sep='\t')

    def show_matriz(self):
        self.save_and_show(self.__datos, "Matriz Original:", 'matriz_original')

    def diagonal(self):
        diag = pd.DataFrame([[self.__datos.iat[i, j] 
            if i == j else 0 for j in range(len(self.__datos.columns))] 
                for i in range(len(self.__datos))])
        self.save_and_show(diag, "Matriz Diagonal:", 'matriz_diagonal')

    def triangular_superior(self):
        tri_sup = pd.DataFrame([[self.__datos.iat[i, j] 
            if i <= j else 0 for j in range(len(self.__datos.columns))] 
                for i in range(len(self.__datos))])
        self.save_and_show(tri_sup, "Matriz Triangular Superior:", 'matriz_triangular_superior')

    def triangular_inferior(self):
        tri_inf = pd.DataFrame([[self.__datos.iat[i, j] 
            if i >= j else 0 for j in range(len(self.__datos.columns))] 
                for i in range(len(self.__datos))])
        self.save_and_show(tri_inf, "Matriz Triangular Inferior:", 'matriz_triangular_inferior')

    def transpuesta(self):
        transp = self.__datos.transpose()
        self.save_and_show(transp, "Matriz Transpuesta:", 'matriz_transpuesta')

def main():
    st.title("Transformaciones de Matrices")
    uploaded_file = st.file_uploader("Cargar archivo de texto", type=["txt"])
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        data = [list(map(int, row.split())) for row in content.strip().split('\n')]
        m = Matriz(data)
        buttons = {
            "Mostrar Matriz Original": m.show_matriz,
            "Mostrar Diagonal": m.diagonal,
            "Mostrar Triangular Superior": m.triangular_superior,
            "Mostrar Triangular Inferior": m.triangular_inferior,
            "Mostrar Transpuesta": m.transpuesta
        }
        for label, action in buttons.items():
            if st.button(label):
                action()

if __name__ == "__main__":
    main()