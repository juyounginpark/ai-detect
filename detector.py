from transformers import pipeline
from PIL import Image
import numpy as np
import easygui

# 모델 준비
detector = pipeline(
    "image-classification", 
    model="haywoodsloan/ai-image-detector-deploy"
)

def is_ai_generated(img_np):
    img = Image.fromarray(img_np)
    results = detector(img)
    print("[AI 감지 결과]", results)
    # "artificial" 라벨 스코어가 0.7 이상이면 AI 생성물로 판정
    for r in results:
        if r['label'].lower() == 'artificial' and r['score'] > 0.7:
            easygui.msgbox("⚠️ AI 생성 이미지 감지됨!", "경고")
            return True
    return False
