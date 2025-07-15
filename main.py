import time
from screen_capture import capture_screen
from detector import is_ai_generated

print("🟢 실시간 화면 감시 시작 (3초 간격)")
while True:
    img_np = capture_screen()
    if is_ai_generated(img_np):
        print("⚠️ AI 생성 이미지 발견!")
    else:
        print("정상 화면.")
    time.sleep(3)
