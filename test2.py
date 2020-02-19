from pymouse import PyMouse

mouse = PyMouse()

class Coordinates:
	def get_position(self):
	  print(self.position)
        def click_position(self, x, y):
           print(self.click)

coor = Coordinates()

coor.position = mouse.position()
coor.click = mouse.click()
coor.get_position()
coor.click_position()
