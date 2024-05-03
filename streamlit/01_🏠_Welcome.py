import streamlit as st 
import streamlit.components.v1 as stc

html_temp = """
		<div style="background-color:#A9B7AA;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Python與Streamlit網頁App建置 </h1>
		<h4 style="color:white;text-align:center;">NLP and Machine Learning </h4>
		</div>
		"""

desc_temp1 = """
### NlP自然語言處理
- 資料：txt、word及pdf
- 模型：文字情緒分析、文字雲等
"""
            
desc_temp2 = """
### 機器學習模型
- 資料：從UCI Machine learning網站所選取的[糖尿病資料集](https://archive.ics.uci.edu/dataset/34/diabetes)
- 模型：Logistic Regression, Decision Tree

			"""
            
st.set_page_config(
    # 網頁標題
    page_title="網頁應用",
    # 網頁圖標
    page_icon="🖥", # st.image / random / emoji ("🐧" or ":penguin:")
    # 網頁介面的佈局寬度
    layout="wide", # centered
    # 側邊欄的顯示狀態
    initial_sidebar_state="expanded", # expanded or auto(預設)
)


def main():
    stc.html(html_temp)
    st.header("")
    st.markdown(desc_temp1, unsafe_allow_html = True)
    st.markdown(desc_temp2, unsafe_allow_html = True)


if __name__ == '__main__':
    main()










































