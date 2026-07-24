import streamlit as st
import requests

#Page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="Amazon🛒🛍",
    layout="centered"
)

st.title("Amazon Reviews Sentiment Analyzer")
st.write("Enter a product review and get instant sentiment prediction!")

#Input box
review = st.text_area("Enter your product review here:",height=150)

#PRediction  button
if st.button("Sentiment Analyzer"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing...."):
            #Call your Flash backend
            response = requests.post(
                "https://amazon-review-analysis-1.onrender.com/predict", #your render link
                json={"reviews": review}
            )
            result = response.json()

            #Display result
            sentiment = result['prediction']
            #confidence = result['confidence']

            if "pos" in sentiment or "neg" in sentiment:
                st.success(f"Sentiment : {sentiment}")
            else:
                st.error(f"Sentiment : {sentiment}")