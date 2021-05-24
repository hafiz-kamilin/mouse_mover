# M²: Mouse Mover

<p align = "center">
  <img src = "https://raw.githubusercontent.com/hafiz-kamilin/mouse_mover/main/demonstration.jpg" width = "341" height = "203"/>
</p>

M²: Mouse Mover is a software created to keeps your online status on Team, Skype, Discord, and any other applications that monitor the mouse movement. 

It works by moving or scrolling the mouse at randomized time range specified by the user. To make sure the mouse input looks believable (without any repetition), the moving and scroling action also randomizeed.

## Test run

1. Assuming Python 3 programming environment already configured by the user; execute `pip install pynput pyqt5` to install the required dependencies.
2. cd the console to the current directory and execute `python mouseMover.py`.

## Note

This program is tested only one Windows 10, it might or might not work on Linux and Mac OS. Especially on `python mouseMover.py` lines 19-22, this code snippet is used to properly display the application's icon on the Windows taskbar.
