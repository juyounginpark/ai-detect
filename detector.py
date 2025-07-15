import random

def is_ai_generated(img_np):
    """
    실제 AI 모델이 연결되기 전, 임시로 10% 확률로 AI 이미지라고 판단
    """
    return random.random() < 0.1
