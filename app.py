import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt

st.sidebar.title('Whatsapp chat analyser')

uploaded_file = st.sidebar.file_uploader("Select a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocessor(data)
    
    st.dataframe(df)

    #select a specific user
    user_list = df['user'].unique().tolist()
    if('group_notification' in user_list):
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox('select user',user_list)

    if(st.sidebar.button('Show Analysis')):

        #Basic stats
        num_messages,words,gif_count,link_count = helper.fetch_stats(selected_user,df)
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Gif count")
            st.title(gif_count)
        with col4:
            st.header("Link count")
            st.title(link_count)         

        if(selected_user == 'Overall'):
            st.title('Most busy users')
            x = helper.most_busy_users(df)
            col1,col2 = st.columns(2)
            fig,ax = plt.subplots()
            
            with col1:
                ax.bar(x.index,x.values)
                st.pyplot(fig)