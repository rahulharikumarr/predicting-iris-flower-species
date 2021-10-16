import streamlit as st
st.title("Enter the attributes of your flower and find out what species of Iris it is")



# Webpage
sl = st.slider('Sepal Length', 4.3, 7.9, 5.1)
sw = st.slider('Sepal Width', 4.5, 3.5, 2.2)
pl = st.slider('Petal Length', 1.0, 6.9, 5.5)
pw = st.slider('Petal Width', 0.1, 2.5, 2.2)



# Model
from sklearn.datasets import load_iris
iris=load_iris()
# iris.keys()
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(iris.data,iris.target)
output=model.predict([[sl,sw,pl,pw]])
output=iris.target_names[output[0]]
st.title(f'The flower species is {output}')
