import mss
import numpy as np

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 첫 번째 전체 화면
        sct_img = sct.grab(monitor)
        img_np = np.array(sct_img)
        # BGRA → RGB 변환
        img_np = img_np[..., :3][..., ::-1]
        return img_np
