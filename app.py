import streamlit as st
import openai
openai.api_key = "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"

def check_bad_language(text):
    prompt_for_bad_words = "你是一个客户服务质检员，判断输入的文字是否有不良用语，有就回答“是”，没有就回答“否”，不要给出任何多余的答复和标点。"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": prompt_for_bad_words},
            {"role": "user", "content": text}
        ]
    )
    
    return response['choices'][0]['message']['content']

st.title("AQM with GPT3.5")
st.subheader("判断是否有不良用语")

text_input = st.text_input("请输入文本")
response = check_bad_language(text_input)

if "是" in response:
    st.write("有不良用语")
elif "否" in response:
    st.write("没有不良用语")
else:
    st.write("无法识别")
