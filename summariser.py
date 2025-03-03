import streamlit as st
from together import Together

API_KEY = "e5c2d2c7eaa5ac32607844af81fa5c93fb4f2deae87beadbd79b86ee2108dcdd"
client = Together(api_key=API_KEY)

def generate_summary(text, num_sentences):
    prompt = f"Summarise this text in {num_sentences} sentences using British English: {text}"
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

st.title("Smart Text Summariser")
st.write("Paste your text and choose how short you want the summary.")

if 'text' not in st.session_state:
    st.session_state.text = ""
text = st.text_area("Enter your text here:", value=st.session_state.text, height=200)
st.session_state.text = text

num_sentences = st.slider("Number of sentences in summary:", 1, 5, 3)

if st.button("Summarise"):
    if st.session_state.text.strip():
        with st.spinner("Summarising..."):
            summary = generate_summary(st.session_state.text, num_sentences)
            st.write("**Summary:**")
            st.write(summary)
    else:
        st.write("Please enter some text first!")

st.sidebar.title("Sample Texts")
if st.sidebar.button("Sample 1"):
    st.session_state.text = "Artificial intelligence is transforming industries by automating tasks and providing insights from data. It’s a broad field, including machine learning, natural language processing, and computer vision. Recent advances in large language models, like the one powering this tool, have made AI more accessible and powerful."
if st.sidebar.button("Sample 2"):
    st.session_state.text = "Climate change is a pressing global issue, with rising temperatures and extreme weather impacting ecosystems. Scientists urge immediate action, such as reducing carbon emissions and adopting renewable energy. Governments and individuals both play a role in addressing this challenge."