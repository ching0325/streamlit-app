import streamlit as st 
import streamlit.components.v1 as stc 
# import sys
# sys.path.append(r"C:\Users\elean\Desktop\作品集\streamlit\models")
from models.eda_app import run_eda_app
from models.ml_app import run_ml_app

html_temp = """
		<div style="background-color:#A9B7AA;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Diabetes </h4>
		</div>
		"""

desc_temp = """
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.

			#### App Content
				- EDA：資料探索
				- ML：結果預測

			"""

def main():
	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)

	menu = ["Intro","EDA","ML"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Intro":
		st.subheader("Introduction")
		#st.write(desc_temp)
		st.markdown(desc_temp, unsafe_allow_html = True)
	elif choice == "EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()


if __name__ == '__main__':
	main()