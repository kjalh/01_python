from dotenv import load_dotenv  # 아마 FastAPI에 같이 있을 거임
import os
from openai import OpenAI # pip install openai
import gradio as gr # pip install gradio
from pymongo import MongoClient # pip install pymongo


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client_gpt = OpenAI(api_key = api_key)

# 몽고 디비 관련
uri = "mongodb+srv://gmltmd:Z7NeBuqEqiLCUbGb@cluster0.bavei4g.mongodb.net/"
client_mongo = MongoClient(uri)
# db = client_mongo['my_database']



example = {
    "제품명":[
        "연필", "스마트폰" #,"필통", "컴퓨터", "시계"
    ],
    "제품 주요 내용":[
        "흠", "뭘 써야 하나"
    ]

}

def build_fewshot(src_lang, trg_lang):
    src_examples = example[src_lang]
    trg_examples = example[trg_lang]
    fewshot_message = []

    for src_text, trg_text in zip(src_examples, trg_examples):
        fewshot_message.append({
            "role": "user",
            "content":src_text
        })

        fewshot_message.append({
            "role": "assitant",
            "content": trg_text
        })

    return fewshot_message

def ad_text_chatgpt(text, src_lang, trg_lang):
    system_instruction=(
        "당신은 전문 광고 문구 제작자입니다.\n",
        f"입력된 {src_lang}라는 제품을 {trg_lang} 넣어 문구를 만드세요.\n"
        "설명, 부연 설명, 따옴표, 제목을 추가하지 마세요.\n"
        "제품 이름, 제품 주요 내용, 광고 문구 스타일, 생성된 광고 문구만 보여주세요."
    )

    fewshot_messages = bulid_fewshot(
        src_lang=src_lang, trg_lang=trg_lang
    )

    messages = [
        {"role": "developer", "content": system_instruction},
        *fewshot_messages,
        {"role":"user", "content": text}
    ]

    try:
        response = client_gpt.reponse.create(
            model="gpt-5-nano",
            input = messages,
            reasoning = {"effort":"high"},
            max_output_toekns = 500
        )