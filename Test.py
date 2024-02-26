import pyautogui

# #1.화면 크기
# print(pyautogui.size())

# #2.마우스 위치 출력
# print(pyautogui.position())

#3.마우스 이동
#Mac = 손쉬운 사용 vscode 사용 권한 설정
# pyautogui.moveTo(41,442)
# pyautogui.moveTo(41,442,3)

#4.마우스 클릭

# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleclick()
# pyautogui.click(click=3, interval=1)#3번 클릭할건데 1초마다 하셈

#5.마우스 드레그
#1261,99-> 704,93
#816.81 ->539.80
pyautogui.moveTo(1261,99, 3)
pyautogui.dragTo(704,93, 3)