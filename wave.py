import sys
import math
from PySide2.QtWidgets import QApplication, QOpenGLWidget
from PySide2.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *

class GradientWave(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)
        self.time = 0.0

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def paintGL(self):
        self.time += 0.016
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_QUADS)
        
        r, g, b = self.get_color(-1.0, 1.0, self.time)
        glColor3f(r, g, b)
        glVertex2f(-1.0, 1.0)
        
        r, g, b = self.get_color(1.0, 1.0, self.time)
        glColor3f(r, g, b)
        glVertex2f(1.0, 1.0)
        
        r, g, b = self.get_color(1.0, -1.0, self.time)
        glColor3f(r, g, b)
        glVertex2f(1.0, -1.0)
        
        # Левый нижний угол (X=-1, Y=-1)
        r, g, b = self.get_color(-1.0, -1.0, self.time)
        glColor3f(r, g, b)
        glVertex2f(-1.0, -1.0)
        
        glEnd()

    def get_color(self, x, y, t):
        wave = math.sin(x * 5.0 + t) * 0.5 + 0.5
      
        r = wave * 0.5 + 0.5
        g = wave * 0.2
        b = wave * 0.8 + 0.2
        
        return r, g, b

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    window = GradientWave()
    window.setWindowTitle("Milinate Gradient Wave")
    window.resize(screen.size().width(), screen.size().height())
    window.show()
    sys.exit(app.exec_())
