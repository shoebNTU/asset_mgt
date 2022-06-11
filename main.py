import streamlit as st
import io
from streamlit_option_menu import option_menu

st.set_option('deprecation.showfileUploaderEncoding', False)

with open('favicon.png', 'rb') as f:
    favicon = io.BytesIO(f.read())

st.set_page_config(page_title='REAMS_APIs',
                   page_icon=favicon, 
                   initial_sidebar_state='expanded')

st.title('Asset Management Analytics')

with st.expander('Application Summary',expanded=False):

    st.markdown("""
    
    #### DATA SCIENCE CAPABILITIES TO SUPPORT ASSET MANAGEMENT 

Rail assets are capital intense and are operated and maintained over decades. Therefore, rail assets are ideally positioned to benefit from the implementation of an asset management system based on best practices. Across the life cycle, rail asset management systems have opportunities to continuously improve, sustain and mature using innovative IT technologies which improve the decision making and provide leadership and stakeholders to meet the bottom line, i.e., cost, risk, and performance management.

To address these challenges, a holistic optimisation of operations, maintenance and renewal planning of rail assets is necessary for the Asset Owner, Operator and Maintainer by developing the REAMS platform. 

REAMS is a software platform that houses and analyses data from Rail asset maintenance management system across systems that are crucial to deliver better Rail reliability for Commuters in Singapore. REAMS is equipped with data analytics capabilities to monitor asset performance, identify potential faults before they occur, so that assets can be repaired or renewed pre-emptively. This will enable stakeholders to shift towards data-driven just-in-time predictive maintenance thereby optimizing overall lifecycle cost of their assets. 

For railways, the main impact of digitalization is on the model of operation. Technologies like artificial intelligence, big data and cloud computing, connectivity and autonomous driving will impact the industry. These technologies are creating a new environment in which rail operators will need to be more agile, to act more quickly and to change continuously to succeed in their mission. In this article we share how we are using AI and Data science capabilities to drive digital transformation in Rail. 

The key for Asset Management for rail systems is artificial intelligence based on the relevant data like asset configuration data, asset condition data, maintenance data and financial data. The AI suite of solutions and capabilities addresses all relevant stakeholders of a rail system. Additionally, it addresses all mission-critical asset classes like rolling stock (RSC), signaling system (SIG), Platform screen doors (PSD) power supply systems and their interdependencies. Furthermore, it covers all decision support levels and horizons. Lastly and most importantly, it uses AI-based models on a massive scale to support human decision making.
""")

    cc1,cc2,cc3 = st.columns([0.1,0.8,0.1])
    with cc2:
        st.image('Picture3.svg',caption='Analytics Portfolio framework to support Digital Asset Management')

    st.markdown("""
    These demos are to illustrate the business model of AIaaS. For companies that cannot or are unwilling to build their own clouds and build, test, and utilize their own artificial intelligence systems, AIaaS is the solution. This is the biggest draw: the opportunity to take advantage of data insights without needing the massive up-front investment in talent and resources.
    """)

    cc1,cc2,cc3 = st.columns([0.1,0.8,0.1])
    with cc2:
        st.image('pic2.png',caption='Portfolio as a Micro-Service: AI as a Service (AIaaS)')

    st.markdown("""
    Demand for AIaaS is growing as businesses increasingly see the value it is creating for competitors. Industry figures suggest that the global market of AI as a service will hit US\\$10.88 billion by 2023, up from US\\$1.13 billion in 2017. However, it could potentially be much higher as it becomes more available.    
        """)

st.markdown(""" #### Please click on the side-bar menu to get links of demos associated with different use-cases
Note: The demos will open up in different tabs, after you click on the respective links
""")
# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Reliability Modelling','Spares forecasting',\
#         'Predictive Maintenance','Economic Optimal Life','Renewal Option Analysis','AHP'], 
#         icons=['house', 'calendar3','bar-chart',\
#         'tools','currency-exchange','cart2','diagram-3'], menu_icon="cast", default_index=0)

dict_links = {'AHP':'https://share.streamlit.io/shoebntu/ahp/main/Apps/app.py', \
    'Reliability Modelling':'https://share.streamlit.io/msundarv/rel_pm/main/shift_pm_app.py', \
     'Spares forecasting':'https://share.streamlit.io/ppplalala-wh/streamlit_app/main/resrcOpt.py',\
       'Predictive Maintenance':'https://share.streamlit.io/dhesru/condition_monitoring/main.py', \
           'Renewal Option Analysis':'https://share.streamlit.io/shoebntu/scheduling/moo_ahp.py', \
               'Economic Optimal Life':'https://share.streamlit.io/shoebntu/eol/main/EOL.py',\
               'Smart Diagnostics':'https://share.streamlit.io/shoebntu/smart_rulemining/main/app_v2.py'
               }

col1,col2 = st.columns([0.6,0.4])
st.sidebar.image("./siemens_logo.png", width = 300)
with st.sidebar:
    
    selected = option_menu("", ["Menu", 'Reliability Modelling','Smart Diagnostics','Spares forecasting',\
            'Predictive Maintenance','Economic Optimal Life','Renewal Option Analysis','AHP'], 
            icons=['house', 'calendar3','thermometer-sun','bar-chart',\
            'tools','currency-exchange','cart2','diagram-3'],
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    st.markdown("#### **Copyright &copy; 2022 DA REAMS, Siemens Mobility**")


if 'Menu' not in selected:
    try:
        st.markdown("""<a style='display: block; text-align: left;' href=""" + dict_links[selected] + f"""> \
            <font size="5"> Please click here to access {selected} app</font> </a>
    """,unsafe_allow_html=True)
    except:
        pass




# if selected == "Upload Data":
#     webbrowser.open_new_tab('https://share.streamlit.io/shoebntu/ahp/main/Apps/app.py')
    