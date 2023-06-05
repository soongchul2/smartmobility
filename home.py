import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


add_selectbox = st.sidebar.selectbox(
    "*** LIST ***",
    ("BMI Calculator", "Gapminder", "My page")
)

if add_selectbox == "BMI Calculator" :


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
    st.info('자신의 몸무게(kg)를 키의 제곱(cm)으로 나눈 값으로 계산합니다.')

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




elif add_selectbox == "Gapminder" :
    st.write("# This is the Gapminder page.")

    data = pd.read_csv('gapminder.csv')

    '''
    st.write(data)

    
    year = st.slider('Select the Year.', 1952, 2007, 1952, step = 5)
    st.write("Year :  ", year)

    data = data[data['year'] == year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'])
    st.pyplot(fig)
    
    '''
    
    st.write(data)

    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x == 'Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x == 'America':
            colors.append('green')
        else :
            colors.append('orange')
    
    data['colors'] = colors

    year = st.slider('Selec a Year', 1952, 2007, 1952, step = 5)
    st.write('##', year, 'Year')

    data = data[data['year'] == year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Expectancy?')
    ax.set_xlabel("Gdp per Capital")
    ax.set_ylabel('Life Expectancy')
    st.pyplot(fig)
    



else :
    st.write("# This is my page.")