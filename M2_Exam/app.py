import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import got 
import community.community_louvain as community_louvain

# page config

st.set_page_config(page_title='Streamlit - Network analysis app')

st.title('M2 Network Analysis')
st.header("Twitter network of congressmen interactions")
#st.sidebar.header("Filters 📊")

# Introduction

st.markdown("""
            Twitter congress network analysis on US Congress
""")
"""

"""

HtmlFile = open("M2_Exam/nx.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 700,width=700)
