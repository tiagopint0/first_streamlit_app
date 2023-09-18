import streamlit
import pandas

#Window title
streamlit.title('My parents new healthy diner!')

#Header 1
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Header 2
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Create Dataframe from CSV
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#Create multiple selection so users can pick the fruit they want
fruits_selected = streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table
streamlit.dataframe(my_fruit_list)
