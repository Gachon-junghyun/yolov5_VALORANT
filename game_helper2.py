import tkinter as tk

root = tk.Tk()
root.overrideredirect(True)  # 기본 창 테두리 및 타이틀바 숨기기
root.wm_attributes("-topmost", True)  # 항상 위에 유지
root.wm_attributes("-transparentcolor", "black")  # 투명 배경 설정
root.wm_attributes("-alpha", 0.1)  # 투명 배경 설정

# 화면 크기와 위치 설정
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 오른쪽에 1/4 크기의 창 설정
window_width = screen_width // 4
window_height = screen_height
root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+0")

# 텍스트 레이블 생성
label = tk.Label(root, text="내용을 입력하세요.", font=("Arial", 24), fg="white", bg="black")
label.pack(pady=100)

def close_window():
    root.destroy()

# 닫기 버튼 생성
close_button = tk.Button(root, text="창 닫기", command=close_window)
close_button.pack()

# 왼쪽에 1/4 크기의 창 생성
left_window = tk.Toplevel(root)
left_window.overrideredirect(True)
left_window.wm_attributes("-topmost", True)
left_window.wm_attributes("-transparentcolor", "black")
left_window.wm_attributes("-alpha", 0.1)
left_window_width = screen_width // 4
left_window_height = screen_height
left_window.geometry(f"{left_window_width}x{left_window_height}+0+0")

left_label = tk.Label(left_window, text="왼쪽 창", font=("Arial", 24), fg="white", bg="black")
left_label.pack(pady=100)

root.mainloop()