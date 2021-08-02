
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
import bcrypt
from functions import check_email,make_password,check_hashes,GETCoefficients,remove_duplicates
from database import create_usertable,add_user_data,check_double_email,check_double_username,login_user,check_userdatatable
import datetime
#from data_functions_clubs import*
#from data_functions_league import*
import matplotlib
matplotlib.use('Agg')
from League_functions.avg_Income_for_player_Departures import  BATCH_for_GetAVGExpendFORplayerArrivals
from functions import DataFrameFunc,NumberOfRows
from League_functions.EFPA_func import*
#    import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import altair as alt
import duckdb
import streamlit.components.v1 as components
coef = 'file.txt'

def app():
    st.subheader("Home") 
    DFrame = DataFrameFunc('Ligaska_KONACAN_STAS.csv')
    df = EFPA_MAIN(DFrame)
    st.write(df)

    col1, col2 = st.beta_columns(2)

    col1, col2 = st.beta_columns(2)

    with col1:
        with st.form('Form1'):
            st.selectbox('Select flavor', ['Vanilla', 'Chocolate'])
            st.slider(label='Select intensity', min_value=0, max_value=100)
            submitted1 = st.form_submit_button('Submit 1')

    if submitted1:
        st.write("SUccesfuly ab",b)

    #dframe = pd.DataFrame(df['   Year of Season |  '],columns= ['    Expend by player|  ', '  Expend + Inflation by player|  '])
    #dframe.bar()
    #st.pyplot()

    # st.bar_chart(dframe)
    # dframe["    Expend by player|  "].value_counts().plot(kind='bar')
    # st.pyplot()
    # st.title("Let's create a table!")
    # DFrame = DataFrameFunc('Ligaska_KONACAN_STAS.csv')
    # df = EFPA_MAIN(DFrame)
    # st.write(df)
    # df = pd.DataFrame(
    #     np.random.randn(200, 3),
    #     columns=['a', 'b', 'c'])

    # base = alt.Chart(df, 
    #              title='ROC Curve of KNN'
    #             ).properties(width=300)
    
    # a = df['   Year of Season |  ']
    # b = df['    Expend by player|  ']
    # d = df['  Expend + Inflation by player|  ']

    # c = alt.Chart(df).mark_circle().encode(

    #     x=a, y='Expend', size='c', color='c', tooltip=[ b, d])

    # st.altair_chart(c, use_container_width=True)

    # chart_data = pd.DataFrame(df,
    #                       columns=['    Expend by player|  ', '  Expend + Inflation by player|  '])
    # st.bar_chart(chart_data)
    # line_chart = alt.Chart(df).mark_line(interpolate='basis').encode(
    #     alt.X(df['   Year of Season |  '],title='Year'),
    #     alt.Y(df['    Name of League |  '], title='League'),
    #     color='category:N'
    # ).properties(
    #     title='Sales of consumer goods'
    # )  

    #       '   Year of Season |  '         '    Expend by player|  '
    from vega_datasets import data

    source = data.iowa_electricity()

    # st.dataframe(source)
    # source = data.iowa_electricity()

    # altara  = alt.Chart(source).mark_area(opacity=0.3).encode(
    #     x="year:T",
    #     y=alt.Y("", stack=None),
    #     color="    Expend by player|  "
    # )
    # st.altair_chart(altara)
    #df['DataFrame Column'] = pd.to_datetime(df['DataFrame Column'], format=specify your format)
    colls = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]
    dat = pd.read_csv('test_data.csv',header = None , names = colls)
    dat['Year'] = pd.to_datetime(dat['Year'], format='%Y')
    c_line = alt.Chart(dat).mark_line(point=True).encode(
        x = "Year",
        y=alt.Y("Expend_by_player", stack=None),
        color="Nationality"

    ).properties(

        width=1200,
        height=500 
    )


    st.altair_chart(c_line)
    #st.write("type source",type(source['year']))

    # df_date = pd.to_datetime(df['   Year of Season |  '])
    # st.write("type ",type(df['   Year of Season |  ']))
    # # st.altair_chart(line_chart)
    # c_line = alt.Chart(df).mark_bar().encode(
    # x = '   Year of Season |  ',
    # y = alt.Y('    Expend by player|  ', title=''),
    # column= alt.Column('   Year of Season |  ',
    #     title="",
    #     header=alt.Header(labelAngle=90)
    # ), 
    # ).properties(
    # width=600,
    # height=300
    # )
    



    # #source = data.stocks()

    # alt_line = alt.Chart(df).transform_filter(
    #     'datum.symbol==="GOOG"'
    # ).mark_area(
    #     line={'color':'darkgreen'},
    #     color=alt.Gradient(
    #         gradient='linear',
    #         stops=[alt.GradientStop(color='white', offset=0),
    #            alt.GradientStop(color='darkgreen', offset=1)],
            
    #         x1=1,
    #         x2=1,
    #         y1=1,
    #         y2=0
    #     )
    # ).encode(
    #     alt.X('date:T'),
    #     alt.Y('price:Q')
    # )
    # st.altair_chart(alt_line)
    #st.write(" : ",duckdb.query("SELECT * FROM df WHERE '' ").to_df())
    # for i in range(1, 10):
    #     cols = st.beta_columns(4)
    #     cols[0].write(f'{i}')
    #     cols[1].write(f'{i * i}')
    #     cols[2].write(f'{i * i * i}')
    #     cols[3].write('x' * i)
#     st.title('Streamlit Components')
#     components.html(
#     """
     
#     <div class="container">
#   <h2>HackerShrine</h2>
 
#     <div class="card" style="width:400px">
     
#     <div class="card-body ">
#       <form action="/upload" method="post" enctype="multipart/form-data">
#       <p class="card-text">Custom HTML </p>
#         <input type="file" name="file" value="file">
#         <hr>
#       <input type="submit" name="upload" value="Upload" class="btn btn-success">
#       </form>
     
#     </div>
#   </div>
#   <br>
# </div>
#     """,
#     height=600,
#     width=200,
# )