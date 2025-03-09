# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import time

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.42?")
st.divider()

with st.sidebar:
    st.logo(path_cda + '\\logo.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: st.login')

    st.code('''
    if not st.experimental_user.is_logged_in:
        if st.button("Log in :material/login:"):
            st.login()
    else:
        if st.button("Log out :material/logout:"):
            st.logout()
        st.markdown(
            f"<p style='font-size: 20pt;'>Hello <img src='{st.experimental_user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.experimental_user.name}</b>,</p>"
            f"<p style='font-size: 20pt;'>You have successfully logged in with <b>{st.experimental_user.email}</b>.</p>",
            unsafe_allow_html=True
        )
    ''')
    if not st.experimental_user.is_logged_in:
        if st.button("Log in :material/login:"):
            st.login()
    else:
        if st.button("Log out :material/logout:"):
            st.logout()
        st.markdown(
            f"<p style='font-size: 20pt;'>Hello <img src='{st.experimental_user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.experimental_user.name}</b>,</p>"
            f"<p style='font-size: 20pt;'>You have successfully logged in with <b>{st.experimental_user.email}</b>.</p>",
            unsafe_allow_html=True
        )

def page2():
    st.header(':two: st.table and st.image markdown')

    cols = st.columns(2)

    with cols[0]:
        st.subheader('Streamlit 1.41')

        st.code('''
            data = {
            "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
            "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
            st.table(df)
        ''', height=240)

        data = {
            "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
            "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
            "Open": np.random.uniform(100, 300, 10).round(2),
            "Close": np.random.uniform(100, 300, 10).round(2)
        }
        df = pd.DataFrame(data)
        st.table(df)

        st.code('''
            st.image('image.png', caption='Curiosity Data Analytics')
        ''')
        st.image(path_cda + '\\0_Branding\\logo.png', width=400, caption='Curiosity Data Analytics')

    with cols[1]:
        st.subheader('Streamlit 1.42')

        st.code('''
            data = {
                "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
                "Sector": [":blue[Tech] 💻", ":green[Automotive] 🚗'", ":blue[Tech] 💻", ":red[E-commerce] 🛒", ":blue[Tech] 💻", ":orange[Entertainment] 🎬", ":blue[Tech] 💻", ":blue[Tech] 💻", ":blue[Tech] 💻", ":blue[Tech] 💻"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
            df['Stock'] = '**:blue-background[' + df.Stock + ']**'
            st.table(df)
        ''', height=240)

        data = {
            "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
            "Sector": [":blue[Tech] 💻", ":green[Automotive] 🚗'", ":blue[Tech] 💻", ":red[E-commerce] 🛒", ":blue[Tech] 💻", ":orange[Entertainment] 🎬", ":blue[Tech] 💻", ":blue[Tech] 💻", ":blue[Tech] 💻", ":blue[Tech] 💻"],
            "Open": np.random.uniform(100, 300, 10).round(2),
            "Close": np.random.uniform(100, 300, 10).round(2)
        }
        df = pd.DataFrame(data)
        df['Stock'] = '**:blue-background[' + df.Stock + ']**'
        st.table(df)
    
        st.code('''
            st.image('image.png', caption=":star:*Curiosity Data Analytics*:star:")
        ''')
        st.image(path_cda + '\\logo.png', width=400, caption=":star:*Curiosity Data Analytics*:star:")


def page3():
    st.header(':three: st.spinner time')

    cols = st.columns(2)

    with cols[0]:
        st.subheader('Streamlit 1.41')

        st.code('''
        import time

        if st.button("Run Task"):
            with st.spinner("Running Task..."):
                time.sleep(4)
                st.success("Task completed!")


        ''')
        if st.button("Run Task", key='t2'):
            with st.spinner("Running Task..."):
                time.sleep(5)
                st.success("Task completed!")

    with cols[1]:
        st.subheader('Streamlit 1.42')

        st.code('''
        import time

        if st.button("Run Task"):
            with st.spinner("Running Task...", show_time=True):
                time.sleep(4)
                st.success("Task completed!")
        ''')

    
        if st.button("Run Task", key='t'):
            with st.spinner("Running Task...", show_time=True):
                time.sleep(5)
                st.success("Task completed!")
    


def page4():
    st.header(':four: st.code height')


    cols = st.columns(2)

    with cols[0]:
        st.code('''
        st.code(\"\"\"
            data = {
                "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
                "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
        \"\"\")
        ''')
        st.code('''
            data = {
                "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
                "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
        ''')

    with cols[1]:
        st.code('''
        st.code(\"\"\"
            data = {
                "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
                "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
        \"\"\", height=100)
        ''')
        st.code('''
            data = {
                "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
                "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
                "Open": np.random.uniform(100, 300, 10).round(2),
                "Close": np.random.uniform(100, 300, 10).round(2)
            }
            df = pd.DataFrame(data)
        ''', height=100)

def page5():
    st.header(':five: st.dataframe changes')

    data = {
        "Stock": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "NFLX", "NVDA", "META", "IBM", "AMD"],
        "Sector": ["Tech", "Automotive", "Tech", "E-commerce", "Tech", "Entertainment", "Tech", "Tech", "Tech", "Tech"],
        "Open": np.random.uniform(100, 300, 10).round(2),
        "Close": np.random.uniform(100, 300, 10).round(2)
    }
    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)


pg = st.navigation([st.Page(page1, title='st.login'),
                    st.Page(page2, title='st.table and st.image markdown'),
                    st.Page(page3, title='st.spinner time'),
                    st.Page(page4, title='st.code height'),
                    st.Page(page5, title='st.dataframe changes')])
pg.run()