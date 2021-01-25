"""
ploting when add new point (Stay view)
x, y, z (yaw, pitch)
serial
"""

import pptk     # Code hồi nhận ra là module này lỗi vl
import time

class Plotting:

    def __init__(self):
        self.v = None
        self.points = []

    def set_points(self, points):
        self.points = points

    def render(self):
        self.v = pptk.viewer(self.points)
        self.v.set(point_size = 0.01)

    def add_point(self, point):
        self.points.append(point)

        # phi_t = self.v.get('phi')
        # theta_t = self.v.get('theta')

        self.v.clear()
        self.v.load(self.points)
        # self.v.set(phi = phi_t, theta = theta_t)

if __name__ == "__main__":
    """plt = Plotting()
    plt.set_points([[1, 1, 1]])

    plt.render()
    time.sleep(3)
    for i in range(100):
        plt.add_point([i, i, i])
        time.sleep(1)"""

    




    