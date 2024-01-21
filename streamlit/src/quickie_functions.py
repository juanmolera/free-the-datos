# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)
import numpy as np

# Data visualization
import plotly.express as px

# Pepinillo
import pickle

def eda(db_to_explore, data_to_explore):

    st.markdown('####  Here it is a quick EDA of it:')

    with open(f'../data/{db_to_explore}/{db_to_explore}.pkl', 'rb') as fp:
        db_cols_info = pickle.load(fp)

    df = data_to_explore

    st.markdown(f'## {db_to_explore.capitalize()} columns information:')
    st.table(db_cols_info)

    # df head
    st.markdown('## Dataframe head:')
    st.table(df.head(1))

    # df tail
    st.markdown('## Dataframe tail:')
    st.table(df.tail(1))

    col1, col2= st.columns(2)

    # nulls
    with col1:
        st.markdown('## Nulls:')
        nulls = df.isnull().sum()
        st.table(nulls)

    # duplicates
    with col2:
        st.markdown('## Duplicates:')
        duplicated = df.duplicated().sum()
        st.metric(label='', value=duplicated)

    # describe numerical vars
    st.markdown('## Describe of numerical variables:')
    describe_num = df.select_dtypes(include=np.number).describe().T
    st.table(describe_num)

    # describe categorical vars
    st.markdown('## Describe of categorical variables:')
    describe_cat = df.describe(include='object').T
    st.table(describe_cat)

    # countplots
    st.markdown('## Distribution of each variable:')
    for c in df.drop(['name','insert_date'], axis=1).columns:

        fig = px.histogram(df, x=df[c])
        fig.update_xaxes(categoryorder = 'total descending')
        st.plotly_chart(fig, use_container_width=True)

    '''# outliers
    st.markdown('## Outliers:')
    df_num = df.select_dtypes(include=np.number)
    for n in df_num.columns:

        fig = px.box(df_num, x=df_num[n])
        st.plotly_chart(fig, use_container_width=True)'''
    