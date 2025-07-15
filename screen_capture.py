from PIL import ImageGrab
import numpy as np

def capture_screen():
    """현재 화면을 numpy 배열로 캡처"""
    img = ImageGrab.grab()
    return np.array(img)
