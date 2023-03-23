import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

def check(text_input, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']

st.title("AQM with GPT3.5")

option = st.selectbox(
    "自动质检点类型:",
    ("不良用语", "负面情绪", "投诉")
)

text_input = st.text_input("")

if st.button("提交", use_container_width=True):
    if option == "不良用语":
        prompt = "你是一个客户服务质检员，判断输入的文字是否有不良用语，有就回答“是”，没有就回答“否”，不要给出任何多余的答复和标点。"
    elif option == "负面情绪":
        prompt = "你是一个客户服务质检员，判断输入的文字是否有负面情绪，有就回答“是”，没有就回答“否”，不要给出任何多余的答复和标点。"
    elif option == "投诉":
        prompt = "你是一个客户服务质检员，判断输入的文字是否提到投诉，必须是明确提到投诉才算，有就回答“是”，没有就回答“否”，不要给出任何多余的答复和标点。"
        
    response = check(text_input, prompt)

    if "是" in response:
        st.write("有不良用语")
    elif "否" in response:
        st.write("没有不良用语")
    else:
        st.write("无法识别")
