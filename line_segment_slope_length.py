'''
Author name: Jeremiah E. Ochepo
last Edited: 3/1/2020 (10PM)
Description: Line Segment Information GUI
'''

from graphics import*
import math

def main():
    win = GraphWin('Shapes', 400, 400, autoflush=False)

    # Program Status Message
    msg = Text(Point(200.0, 20.0), 'Line Segment')
    msg.setFace('helvetica')
    msg.setStyle('bold')
    msg.setSize(12)
    msg.draw(win)

    color_list = ['black', 'yellow', 'red', 'blue', 'white']

    def draw_line():
        a_line = Line(Point(50, 200), Point(350, 200))
        a_line.setFill(color_list[0])
        a_line.setOutline(color_list[0])
        a_line.draw(win)

    draw_line()

    # Get Points
    p1 = win.getMouse().draw(win)
    p2 = win.getMouse().draw(win)

    def draw_line_segment():
        a_segment = Line(p1, p2)
        a_segment.setFill(color_list[1])
        a_segment.setOutline(color_list[1])
        a_segment.draw(win)

    draw_line_segment()

    def slope_and_length():
        try:
            x1, x2 = p1.getX(), p2.getX()
            dx = x2 - x1

            y1, y2 = p1.getY(), p2.getY()
            dy = y2 - y1

            # Slope
            slope = dy / dx
            print(f'Slope: {round(slope, 2)}')

            # Length
            dx = dx ** 2
            dy = dy ** 2
            length = math.sqrt(dx + dy)
            print(f'Length: {round(length, 2)} Pixel')

        except ZeroDivisionError:
            print('Error: Division by zero (vertical line)')

    slope_and_length()

    msg.setText('Click any point to quit')
    pt = win.getMouse()
    win.close()

try:
    main()
except Exception as e:
    print(f'An error occurred: {e}')
