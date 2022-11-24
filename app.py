#-------------------#
# SETUP
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

#-------------------#
#Obtain home path

#home_path = str(Path.home)

# Data import
df = pd.read_csv("/Users/juliamatesic/Documents/BigData_WS22:23/git-github-fundamentals-juliamatesic/Homework1_GroupJ/data/external/data.csv")

#---------------------#
#Header

st.title('Herzlich Willkommen auf dem Dashboard von Gruppe J')

st.subheader('Analyse der WNBA Predictions')

st.image('/Users/juliamatesic/Documents/BigData_WS22:23/git-github-fundamentals-juliamatesic/Homework1_GroupJ/dashboard/streamlit/img/Pic_WNBA.png')

#Sidebar
st.sidebar.header('WNBA Rating')

#Make a slider
satisfaction = st.sidebar.slider('How much do you like to watch WNBA?', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("My MOOD to watch NBA is around ", satisfaction, 'points')

# BODY

#st.write("Take a look at my chart")
# Make a chart with altair
#c = alt.Chart(df).mark_bar().encode(
    # x=alt.X('date',
   # sort='-y'),
  #  y=alt.Y('count(playoff)')
#)
#c.properties(
 #   title= 'WNBA Teams',
 #   width= 1200,
   # heigth=300
#)


st.subheader('Take a look at my chart')
st.write('The chart shows, how many playoff games the home teams had.')
#Make a chart with altair

c = alt.Chart(df).mark_bar().encode(
    x=alt.X('home_team',
    sort='-y',
    axis=alt.Axis(title="Home Team",
                  labelAngle=10,
                  titleAnchor="start")),
    y=alt.Y('count(home_team)',
    axis=alt.Axis(title="Count",
                  titleAnchor="end")),
).properties(
    title= 'WNBA Teams',
    width= 1200,
    height= 400
).configure_title(
    fontSize=35,
    font='Times',
    color= 'purple',
    anchor= 'start'
).interactive()

st.altair_chart(c, use_container_width=True)

st.subheader('Take a look at my next chart')
st.write('This one shows, how many home team scores the home team made in their season. Use your mouse and hover on the points to see,on which day which team has scored how many points.')

c=alt.Chart(df).mark_point().encode(
    x=alt.X('date', 
    axis=alt.Axis(title="Datum",
    )),
    y=alt.Y('home_team',
    axis=alt.Axis(title="Home Team",
    )),
    tooltip=['home_team_score', 'date', 'home_team']
).properties(
    title= 'WNBA Home Scores',
    width= 1400,
    height= 400
).configure_title(
    fontSize=40,
    font='Arial',
    color= 'red',
    anchor= 'start'
).interactive()

st.altair_chart(c, use_container_width=True)

st.subheader('Take a look on the WNBA pregame rating')
st.write('This one shows, how the pregame rating of the home teams looked like. The higher the rating the better.')

c=alt.Chart(df).mark_line().encode(
    x=alt.X('home_team',
    axis=alt.Axis(title="Home Team",
    )),
    y=alt.Y('home_team_pregame_rating',
    axis=alt.Axis(title="Pregame-Rating",
    )),
    tooltip=['date','home_team_pregame_rating','away_team'],
).properties(
    title= 'WNBA Pregame Rating',
    width= 900,
    height= 500
).configure_title(
    fontSize=40,
    font='Arial',
    color= 'green',
    anchor= 'start',
)

st.altair_chart(c, use_container_width=True)

st.subheader('Take a look on the WNBA games')
st.write('This one shows, how many playoff games (orange) and how many normal games the last season had. 23 games have been playoffs and 217 other games.')

c = alt.Chart(df).encode(
    theta=alt.Theta("value:Q", stack=True), 
    color=alt.Color("category:N", legend=None),
).properties(
    title= 'WNBA Playoffs',
    width= 400,
    height= 200,
)

pie = chart.mark_arc(outerRadius=140)
text = chart.mark_text(radius=160, size=20).encode(text="category:N")

pie + text


st.altair_chart(c, use_container_width=True)

###-------------------###
# END OF APP




