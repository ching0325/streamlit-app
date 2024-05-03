import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache_data
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	st.subheader("EDA Section")
	df = load_data("data/diabetes_data_upload.csv")
	df_clean = load_data("data/diabetes_data_upload_clean.csv")
	freq_df = load_data("data/freqdist_of_age_data.csv")

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		st.success("Description")
		st.dataframe(df) #display data

		with st.expander("Data Types Summary"):
			st.dataframe(df.dtypes)

		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
	else:
		st.success("Plots")

		# Layouts
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Dist Plot of Gender"):
				## 長條圖
				# fig = plt.figure()
				# sns.countplot(df['Gender'])
				# st.pyplot(fig)

				## 圓餅圖
				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df) -> 寫下來的話會在同一個格子裡顯示這個dataframe
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Dist Plot of Class"):
				#fig = plt.figure()
				#sns.countplot(df['class'])
				#st.pyplot(fig)
				class_df = df['class'].value_counts().to_frame()
				class_df = class_df.reset_index()
				class_df.columns = ['Class Type','Counts']
				p2 = px.bar(class_df, x='Counts', y='Class Type', orientation='h')
				st.plotly_chart(p2, use_container_width=True)

		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.expander("Frequency Dist Plot of Age"):
			# fig,ax = plt.subplots()
			# ax.bar(freq_df['Age'],freq_df['count'])
			# plt.ylabel('Counts')
			# plt.title('Frequency Count of Age')
			# plt.xticks(rotation=45)
			# st.pyplot(fig)

			p = px.bar(freq_df,x='Age',y='count')
			st.plotly_chart(p)

			#p2 = px.line(freq_df,x='Age',y='count')
			#st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			# outlier_df = 
			#比較陽春的盒形圖
			#fig = plt.figure()
			#sns.boxplot(df['Age'])
			#st.pyplot(fig)

			#比較fancy的盒形圖
			p3 = px.box(df,x='Age',color='Gender')
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			#heat map
			#陽春版
			corr_matrix = df_clean.corr()
			#fig = plt.figure(figsize=(20,10))
			#sns.heatmap(corr_matrix,annot=True)
			#st.pyplot(fig)
            
			#fancy版
			p4 = px.imshow(corr_matrix)
			st.plotly_chart(p4)


	







