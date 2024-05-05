import pyautogui
import numpy
import time

def main():
  pyautogui.FAILSAFE = True;
  time.sleep(3);
  pyautogui.typewrite(['win', 'c', 'h', 'r', 'o', 'm', 'e', 'enter'], interval=0.2);
  time.sleep(3);
  pyautogui.typewrite('maroonstudios.hrhub.ph\n', interval=0.02);
  time.sleep(5);
  login_coordinate = pyautogui.locateCenterOnScreen('login_button.jpg');
  pyautogui.leftClick(login_coordinate);
  time.sleep(10);
  clockin_dropdown_coordinate = pyautogui.locateCenterOnScreen('clockin_dropdown.jpg');
  pyautogui.leftClick(clockin_dropdown_coordinate);
if __name__ == "__main__":
  main();