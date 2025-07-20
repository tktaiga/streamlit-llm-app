import streamlit as st

# OpenAI APIキーが自動で参照
from dotenv import load_dotenv
load_dotenv()

# ライブラリのインポート
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# アプリの説明
st.title("サンプルアプリ: 旅行と食べ物についての質問回答Webアプリ")

st.write("##### 動作モード1: 旅行に関する専門家への質問")
st.write("入力フォームに場所名を入力し、実行ボタンを押すことで有名観光地を回答します")
st.write("##### 動作モード2: 食べ物に関する専門家への質問")
st.write("入力フォームに食べ物の名前を入力し、実行ボタンを押すことでその食べ物を使った料理名を回答します")


# ラジオボタンで動作モードを選択
selected_item = st.radio(
    "動作モードを選択してください。",
    ["旅行に関する専門家への質問", "食べ物に関する専門家への質問"]
)

st.divider()

# メッセージ入力
if selected_item == "旅行に関する専門家への質問":
    input_msg = st.text_input(label="旅行先の場所を入力してください。")
else:
    input_msg = st.text_input(label="食べ物の名前を入力してください。")

# LLMからの回答を取得する関数
def get_llm_response(input_text: str, mode: str) -> str:
    if mode == "旅行に関する専門家への質問":
        messages = [
            SystemMessage(content="場所の名前から有名な観光地を３つ回答します"),
            HumanMessage(content=input_text),
        ]
    else:
        messages = [
            SystemMessage(content="食べ物の名前からその食べ物を使った料理名を３つ回答します"),
            HumanMessage(content=input_text),
        ]
    result = llm(messages)
    return result.content

# 実行ボタンを押下
if st.button("実行"):
    st.divider()
    response = get_llm_response(input_msg, selected_item)
    st.write(response)