import streamlit as st
import io
from streamlit_option_menu import option_menu
import webbrowser

st.set_option('deprecation.showfileUploaderEncoding', False)

with open('favicon.png', 'rb') as f:
    favicon = io.BytesIO(f.read())

st.set_page_config(page_title='REAMS_APIs',
                   page_icon=favicon, 
                   layout='wide', 
                   initial_sidebar_state='expanded')

st.title('Asset Management')
with st.sidebar:    
    st.sidebar.image("./siemens_logo.png", width = 300)
    st.markdown(""" #### Please click on the menu to see demos of different use-cases
    Note: The demos will open up in different tabs
    """)
# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Reliability Modelling','Spares forecasting',\
#         'Predictive Maintenance','Economic Optimal Life','Renewal Option Analysis','AHP'], 
#         icons=['house', 'calendar3','bar-chart',\
#         'tools','currency-exchange','cart2','diagram-3'], menu_icon="cast", default_index=0)

selected = option_menu("", ["Menu", 'Reliability Modelling','Spares forecasting',\
        'Predictive Maintenance','Economic Optimal Life','Renewal Option Analysis','AHP'], 
        icons=['house', 'calendar3','bar-chart',\
        'tools','currency-exchange','cart2','diagram-3'],
    menu_icon="cast", default_index=0, orientation="vertical",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"10px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

dict_links = {'AHP':'https://share.streamlit.io/shoebntu/ahp/main/Apps/app.py', \
    'Reliability Modelling':'https://share.streamlit.io/msundarv/rel_pm/main/shift_pm_app.py', \
     'Spares forecasting':'https://share.streamlit.io/ppplalala-wh/streamlit_app/main/resrcOpt.py',\
       'Predictive Maintenance':'https://share.streamlit.io/dhesru/condition_monitoring/main.py', \
           'Renewal Option Analysis':'https://share.streamlit.io/shoebntu/scheduling/moo_ahp.py', \
               'Economic Optimal Life':'https://share.streamlit.io/shoebntu/eol/main/EOL.py'
               }
if 'Menu' not in selected:
    try:
        webbrowser.open_new_tab(dict_links[selected])
    except:
        pass



# if selected == "Upload Data":
#     webbrowser.open_new_tab('https://share.streamlit.io/shoebntu/ahp/main/Apps/app.py')
    