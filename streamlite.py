import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
st.title('Bienvenue sur mon application!')
st.write('Ici nous allons visualiser une étude sur les voitures')
link='https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
voiture=pd.read_csv(link,sep=',')
st.write('Nous allons voir un heatmap de corrélation de notre database!')
voiture=voiture.sort_values('year',ascending=True)
voiture.reset_index()
voiture.year=voiture.year.astype(str)
fig_corr=sns.heatmap(data=voiture.corr(),cmap='cool',center=0,annot=True)
st.pyplot(fig_corr.figure)
st.write('Nous pouvons voir sur notre heatmap que beaucoup de colonne sont correlés entre elle')
st.write('Nous allons voir un nuage de points entre cylinders et cubicinches')
st.line_chart(data=voiture,x='cylinders',y='cubicinches')
fig1=px.bar(voiture,x="continent",y="weightlbs",animation_frame="year")
st.plotly_chart(fig1, use_container_width=True)
cond=voiture.continent.str.contains('Japan')
dfjapan=voiture[cond]
cond1=voiture.continent.str.contains('US')
dfus=voiture[cond1]
cond2=voiture.continent.str.contains('Europe')
dfEU=voiture[cond2]
st.write("Appuyer sur l'un des trois boutons pour filtrer la base de données selon le continent")
if st.button('Japan'):
    dfjapan
elif st.button('US'):
    dfus
elif st.button('Europe'):
    dfEU
