import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px 

#%%
# 設定頁面顯示
## 請用st.set_page_config()來設定頁面顯示
## 若忘記可參考單元6
st.set_page_config(
    # 網頁標題
    page_title="Steve的第一個Streamlit Web App",
    # 網頁圖標
    page_icon="🌐", # st.image / random / emoji ("🐧" or ":penguin:")
    # 網頁介面的佈局寬度
    layout="centered", # centered or wide
    # 側邊欄的顯示狀態
    initial_sidebar_state="auto", # expanded or auto(預設) or collapsed
)

#%%
# 設定左側邊欄選單頁面
menu = st.sidebar.selectbox("Menu",["Home","Plot"])

## 請於Home頁面設定title為"我的第一個Streamlit Web App"
if menu == "Home":
    
    st.title("Steve的第一個Streamlit Web App")

## 請將Home裡面放入「assignment_home.py」的內容
## 並將'常用streamlit基礎功能'、'終端機Streamlit指令'、'Streamlit的動態視覺圖'分為三欄作呈現
## 提示: 利用st.columns()及with col1, with col2...
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('常用streamlit基礎功能')
        st.write('1. Streamlit的動態視覺圖')
        st.write('2. Streamlit的文字輸入')
        st.write('3. Streamlit的文字呈現')
        st.write('4. Streamlit的互動式工具')
        st.write('5. Streamlit的介面排版')
        st.write('6. Streamlit的上傳方法')
        st.write('7. Streamlit的下載方法')
        st.write('8. Streamlit的多頁面功能')

    with col2:
        st.subheader('終端機Streamlit指令')
        # Display Code
        mycode = """
        # Command line
        $ streamlit --help
        $ streamlit --version
        $ streamlit hello
        $ streamlit config show
        $ streamlit cache clear
        $ streamlit docs
        $ streamlit run your_script.py
        """
        st.code(mycode, language = 'terminal')
        
    with col3:
        st.subheader('Streamlit的動態視覺圖')
        newcode = """
        import streamlit as st 

        # 載入探索式分析(EDA)相關套件 
        import pandas as pd 
        import numpy as np 

        # 載入資料視覺化相關套件 
        import plotly.express as px 


        def main():
            st.title("Streamlit的動態視覺圖")
            st.subheader("用Streamlit 呈現 Plotly")
            
            df = pd.read_csv("data/sales_data_sample.csv")
            df = df.iloc[0:10, ::]
            
            
            st.dataframe(df)
            
            # 圓餅圖 Pie Chart
            fig = px.pie(df, values='單價',names='系列',
                         title='Pie Chart of Series')
            st.plotly_chart(fig)

            st.title('系列單價圓餅圖')
            fig_new = px.pie(df, values='單價',names='系列'
                         )
            st.plotly_chart(fig_new)
            


            # 長條圖 Bar Chart
            st.title('系列單價長條圖')
            fig2 = px.bar(df,x='系列',y='單價')
            st.plotly_chart(fig2)

            

        if __name__ == '__main__':
            main()
        """
        st.code(newcode, language = 'python')
        
## 請將Plot裡面放入「02_app_plotly.py」的內容
## 提示：利用if, else來作設定
else:
    st.title("Streamlit的動態視覺圖")
    st.subheader("用streamlit呈現plotly")
    df = pd.read_csv("sales_data_sample.csv")
    df = df.iloc[0:10, ::]
    st.dataframe(df)
    
    # 圓餅圖 Pie Chart
    st.title("系列單價圓餅圖")
    fig = px.pie(df, values='單價',names='系列',
                 title='Pie Chart of Series')
    st.plotly_chart(fig)

    
    fig_new = px.pie(df, values='單價',names='系列'
                 )
    st.plotly_chart(fig_new)
    # 長條圖 Bar Chart
    st.title('系列單價長條圖')
    fig2 = px.bar(df,x='系列',y='單價')
    st.plotly_chart(fig2)

