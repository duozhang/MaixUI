import math, image
from ui_maix import ui

from button import cube_button

class icon:

  x, y, w, h, img = 0, 0, 0, 0, None

  def __init__(self, x, y, path):
    self.img = image.Image(path)  # 60ms ~ 90ms
    self.x, self.y = x, y
    self.w, self.h = self.img.width(), self.img.height()

  def checked(self, color=(255, 0, 0)):
    ui.img.draw_rectangle(self.x - 2, self.y - 2, self.w + 4, self.h + 4, color, thickness=1)

  def draw(self, is_check = False, alpha = 0, color=(255, 255, 255)):
    tmp = self.img.copy()  # 1ms
    if is_check:
      self.checked(color)
    ui.img.draw_image(tmp, self.x, self.y, alpha=int(alpha))  # 4ms
    del tmp

  def title(self, string, color=(255, 255, 255)):
    ui.img.draw_string(self.x, self.y, string)

class launcher:

  alpha = 0
  app_select = 0
  app_sets = [
        icon(40, 50, "/sd/res/icons/app_camera.bmp"),
        icon(140, 50, "/sd/res/icons/app_settings.bmp"),
        icon(140, 150, "/sd/res/icons/app_explorer.bmp"),
        icon(40, 150, "/sd/res/icons/app_system_info.bmp")
    ]

  cube_btn = cube_button()

  def draw():
    value = math.cos(math.pi * launcher.alpha / 12) * 50 + 200
    launcher.alpha = (launcher.alpha + 1) % 24

    if launcher.cube_btn.back() == 1:
        launcher.app_select -= 1
    elif launcher.cube_btn.next() == 1:
        launcher.app_select += 1
    elif launcher.cube_btn.home() == 1:
        print('start', launcher.app_select)
        # ui.img.draw_string(15, 120, '(%s)' % launcher.app_sets[launcher.app_select])

    launcher.app_select = launcher.app_select % 4 # lock pos

    for pos in range(0, 4):
        checked = (pos == launcher.app_select)
        launcher.app_sets[pos].draw(checked, value if checked else 255)

if __name__ == "__main__":
  from ui_maix import ui
  from ui_taskbar import taskbar

  @ui.warp_template(ui.bg_draw)
  @ui.warp_template(taskbar.time_draw)
  def unit_test():
    launcher.draw()
    ui.display()
  import time
  while True:
      unit_test()
      launcher.cube_btn.event()