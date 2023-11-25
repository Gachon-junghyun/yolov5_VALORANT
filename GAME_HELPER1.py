import tkinter as tk
import pyautogui



root = tk.Tk()
root.overrideredirect(True)  # 기본 창 테두리 및 타이틀바 숨기기
root.wm_attributes("-topmost", True)  # 항상 위에 유지
root.wm_attributes("-transparentcolor", "black")  # 투명 배경 설정
root.wm_attributes("-alpha", 0.1)  # 투명 배경 설정
# 창 크기와 위치 설정
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# 텍스트 레이블 생성
label = tk.Label(root, text="내용을 입력하세요.", font=("Arial", 24), fg="white", bg="black")
label.pack(pady=100)

def close_window():
    root.destroy()

# 닫기 버튼 생성
close_button = tk.Button(root, text="창 닫기", command=close_window)
close_button.pack()

root.mainloop()