import streamlit as st
import requests
#page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎬",
    layout="centered")

st.title("Product review sentiment analyzer")
st.write("enter a product review and get instant sentiment prediction!")
#input box
review=st.text_area("enter your product review here:",height=150)
#predict button
if st.button("analyze sentiment"):
    if review.strip() == "":
        st.warning("pleace enter a review first!")
    else:
        with st.spinner("analyzing.."):
            #call your flask backend
            response=requests.post("https://sentiment-ana-gztb.onrender.com/predict",
                                   json={"reviews":review})
            result=response.json()
        #display result
        sentiment=result['prediction']
        #confidence=result['confidence']
        if "positive"in sentiment or "negative" in sentiment:
            st.success(f"Sentiment:{sentiment}")
        else:
            st.error(f"Sentiment:{sentiment}")
            #st.metric(label="confidence",value=confidence)
