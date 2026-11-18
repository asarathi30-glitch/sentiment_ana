import streamlit as st
import requests

# page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

st.title("Product review sentiment analyzer")
st.write("Enter a product review and get instant sentiment prediction!")

# input box
review = st.text_area("Enter your product review here:", height=150)

# predict button
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first!")

    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "https://sentiment-ana-gztb.onrender.com/predict",
                    json={"reviews": review},
                    timeout=60
                )

                if response.status_code == 200:
                    result = response.json()
                    sentiment = result["prediction"]

                    # display result
                    if "positive" in sentiment.lower():
                        st.success(f"Sentiment: {sentiment}")

                    elif "negative" in sentiment.lower():
                        st.error(f"Sentiment: {sentiment}")

                    else:
                        st.info(f"Sentiment: {sentiment}")

                else:
                    st.error(f"API Error: {response.status_code}")
                    st.code(response.text)

            except requests.exceptions.JSONDecodeError:
                st.error("Server returned invalid JSON.")
                st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
