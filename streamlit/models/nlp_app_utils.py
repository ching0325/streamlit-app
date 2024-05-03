# Load NLP Pkgs
## for dowload spacy and 文字包
# 1. pip install spacy
# 2. from spacy import dowload
# 3. dowload("en_core_web_sm")
# then run the code below, it suppose to work
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy
from textblob import TextBlob
import pandas as pd 
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit  as st


# Fxns
def convert_to_df(sentiment):
	sentiment_dic = {'Polarity':sentiment.polarity, 'Subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dic.items(), columns = ['metrics', 'value'])
	return sentiment_df

def text_analyzer(my_text):
	docx = nlp(my_text)
	allData = [(token.text,token.shape_,token.pos_,token.tag_,token.lemma_,token.is_alpha,token.is_stop) for token in docx]
	df = pd.DataFrame(allData,columns=['Token','Shape','PoS','Tag','Lemma','IsAlpha','Is_Stopword'])
	return df 	

def get_entities(my_text):
	docx = nlp(my_text)
	entities = [(entity.text,entity.label_) for entity in docx.ents]
	return entities

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
@st.cache_data
def render_entities(rawtext):
	docx = nlp(rawtext)
	html = displacy.render(docx,style="ent")
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	return result


# Fxn to get most common tokens
def get_most_common_tokens(my_text,num=5):
	word_tokens = Counter(my_text.split())
	most_common_tokens = dict(word_tokens.most_common(num))
	return most_common_tokens

# Fxn to Get Sentiment
def get_sentiment(my_text):
	blob = TextBlob(my_text)
	sentiment = blob.sentiment
	return sentiment

def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in docx.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			pos_list.append(res)
		elif res <= -0.1:
			neg_list.append(i)
			neg_list.append(res)
		else:
			neu_list.append(i)
	result = {'Positive':pos_list, 'Negative':neg_list, 'Neutral':neu_list}
	return result


# Fxn to Read PDF
from PyPDF2 import PdfReader
import pdfplumber


def read_pdf(file):
	pdfReader = PdfReader(file)
	count = len(pdfReader.pages)
	all_page_text = ""
	for i in range(count):
		page = pdfReader.pages[i]
		all_page_text += page.extract_text()

	return all_page_text

def read_pdf2(file):
	with pdfplumber.open(file) as pdf:
	    page = pdf.pages[0]
	return page.extract_text()
	