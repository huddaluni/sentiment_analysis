import gradio as gr
from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
def get_sentiment(input_text):
    return sentiment(input_text)

iface7 = gr.Interface(get_sentiment, inputs= "text", outputs= "text", title="Sentiment Analysis")

iface7.launch(inline=False)