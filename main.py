import time
import datetime
import os
from screen_capture import capture_screen
from detector import is_ai_generated

def show_warning():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] 🚨 AI 생성물 또는 딥페이크 이미지 감지됨!")

    try:
        if os.name == 'nt':  # Windows 팝업
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, "AI 생성 이미지가 감지되었습니다!", "경고", 0x30)
        else:
            print("🔔 팝업 알림은 현재 OS에서 지원되지 않음")
    except Exception as e:
        print(f"팝업 오류: {e}")

if __name__ == "__main__":
    print("🔍 실시간 화면 감시 시작 (3초 간격)")
    while True:
        screen = capture_screen()
        if is_ai_generated(screen):
            show_warning()
        time.sleep(3)
