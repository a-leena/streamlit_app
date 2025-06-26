import streamlit as st
import os
import pandas as pd

# Texts
st.title("Super Simple Web App!")
st.header("This here is a header.")
st.subheader("This, on the other hand, is a subheader.")
st.markdown("This is a bold **Markdown**.")
st.caption("This right here is a caption.")

# render codes
code_example = """
# See that's a Python Code
def greet(name):
    print('Hello,', name)
"""
st.code(code_example, language="python")

# Horizontal dividing line
st.divider()

# Images
"""
Make a new folder, in the same directory as the python 
file, named 'static'. Inside that folder add the images you
want.
Import the os module to define the path to the images.
"""
st.image(os.path.join(os.getcwd(), "static", "trees.jpg"),caption="A beautiful green forest.")
# os.getcwd(): gets the path of the current working directory

# Data Elements
st.subheader("Data Elements")
df = pd.DataFrame(data={
    'Name': ['Alvin', 'Billie', 'Camille', 'David', 'Elaine'],
    'Age': [25, 28, 32, 49, 31],
    'Occupation': ['Singer', 'Director', 'Doctor', 'Lawyer', 'Chef']
})
st.markdown("A dataframe with which you can interact --")
st.dataframe(df)

st.markdown("A dataframe which you can edit --")
editable_df = st.data_editor(df)
print(editable_df)

st.markdown("A dataframe that you can only view (static table) --")
st.table(df)

st.markdown("Metrics --")
st.metric(label="Number of Records", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(),1))

dict = {
    "name": "Aimee",
    "age": 25,
    "skills": ['Python', 'Machine Learning', 'Data Visualization']
}

st.json(dict)
# st.write(dict)

st.divider()