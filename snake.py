from turtle import Turtle, Screen
import time

segments = []


class Snake:

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)

    def move(self):
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)