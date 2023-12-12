import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Visualization")

st.header("Upload data")
data_file = st.file_uploader("choose a csv file")

if data_file is not None:
     df = pd.read_csv(data_file)

     st.header("Show data")
     st.dataframe(df)

     st.header("Des")
     st.table(df.describe())

     st.header("Infor")
     buffer = io.StringIO()
     df.info(buf=buffer)
     st.text(buffer.getvalue())

     st.header("Visualize each header")
     for col in list(df.columns):
          fig, ax = plt.subplots()
          ax.hist(df[col], bins=20)
          plt.xlabel(col)
          plt.ylabel("num")
          st.pyplot(fig)

     st.header("Show corr")
     fig, ax = plt.subplots()
     sn = sns.heatmap(df.corr(method='pearson'), ax=ax, vmax=1, square=True, annot=True, cmap='Reds')
     st.write(fig)

     output = st.radio("choose a dependent var", df.columns)

     st.header("show relation")
     for col in list(df.columns):
          if col != output:
               fig, ax = plt.subplots()
               ax.scatter(x=df[col], y=df[output])
               plt.xlabel(col)
               plt.ylabel("num")
               st.pyplot(fig)



