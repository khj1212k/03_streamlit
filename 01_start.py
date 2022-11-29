import streamlit as st

st.title('title')
st.header('header')
st.subheader('subheader')
st.text('text')

code = 'print(\'hello python\')'

st.code(code)
st.markdown('''
# markdown
**big**
''')