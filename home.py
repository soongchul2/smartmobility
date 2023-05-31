import streamlit as st

st.write('# Hi! Welcome to My App!')

st.write('Nice to meet you. Welcome to My App~!')


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


option = st.selectbox(
    'Which animal do you like?',
    ('Dog', 'Cat', 'Horse' , 'Rabbit' , 'Elephant'))

st.write('My favorite animal is', option , ', Yeah~')
st.write(f'My favorite animal is {option}, Yeah~')

txt = st.text_area('Please Introduce yourself.', '''
    
    ''')

st.write('Contents :', txt)

age = st.slider('Choose your age.', 0, 130, 22)
st.write("I'm ", age, 'years old')