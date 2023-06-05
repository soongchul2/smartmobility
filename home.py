import streamlit as st
from PIL import Image

#Calculate BMI APP
#INPUT (Weight, Height)

def bmi_range(bmi):
    if bmi >= 25:
        st.error('HOLY MOLY~!! FAT')
    elif bmi >= 23:
        st.warning('Oops...A Little Fat')
    elif bmi >= 18.5:
        st.success('HOW GOOD~!')
    else:
        st.warning('Oops...TOO THIN')


st.write('# Calculate BMI!!')
st.subheader('자신의 몸무게(kg)를 키의 제곱(m)으로 나눈 값으로 계산합니다.')

height = st.number_input('height (cm)', 100, 200, 170, 5)
st.write('Your height :', height, 'cm')

weight = st.number_input('weight (kg)', value = 50, step = 5)
st.write('Your weight :',weight, 'kg')

bmi = weight/((height/100)**2)

if st.button('Calculate'):
    st.write('Your BMI is', round(bmi,2),', HOHO~')
    bmi_range(bmi)
    st.balloons()

image = Image.open('vegies.jpg')

st.image(image, caption = 'Vegitables with Paprika!')