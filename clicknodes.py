'''
Created on 2012/02/05

@author: utisam
'''
from javax.swing import JFrame
from java.awt.event import MouseListener, WindowListener
import sys

class ImageFrame(JFrame, MouseListener, WindowListener):
	def __init__(self):
		self.setSize(640, 480)
		self.img = self.getToolkit().getImage(raw_input("input image path: "))
		self.points = []
		self.addMouseListener(self)
		self.addWindowListener(self)
		self.setVisible(True)
	def paint(self, g):
		g.drawImage(self.img, 0, 0, self)
		for x, y in self.points:
			g.fillOval(x - 2, y - 2, 4, 4)
	def mouseClicked(self, e):
		self.points.append((e.getX(), e.getY()))
		self.repaint();
	def windowClosing(self, e):
		f = file("points.txt", "w")
		f.write(str(self.points))
		f.close()
		f = file("map.gml", "w")
		f.write(points2gmlnodes(self.points))
		f.close()
		sys.exit(0)
	def windowActivated(self, e):
		pass
	def windowClosed(self, e):
		pass  
	def windowDeactivated(self, e):
		pass
	def windowDeiconified(self, e):
		pass 
	def windowIconified(self, e):
		pass 
	def windowOpened(self, e):
		pass 
	def mouseReleased(self,e):
		pass
	def mousePressed(self, e):
		pass
	def mouseEntered(self, e):
		pass
	def mouseExited(self, e):
		pass

def points2gmlnodes(points):
	return """<?xml version="1.0" encoding="UTF-8"?>

<rcr:map xmlns:rcr="urn:roborescue:map:gml" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:gml="http://www.opengis.net/gml">
  <rcr:nodelist>
""" + "\n".join(["""	<gml:Node gml:id="%d">
      <gml:pointProperty>
        <gml:Point>
          <gml:coordinates>%s</gml:coordinates>
        </gml:Point>
      </gml:pointProperty>
    </gml:Node>""" % ((i + 1), str(pt)[1:-1]) for i, pt in enumerate(points)]) + """
  </rcr:nodelist>
</rcr:map>"""

if __name__ == "__main__":
	f = ImageFrame()
