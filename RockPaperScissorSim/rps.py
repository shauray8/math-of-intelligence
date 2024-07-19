from manim import *
import numpy as np
import random

class RPSTriangleSystemWithGraph(Scene):
    def construct(self):
        # Create and add the triangle
        triangle = Triangle().scale(2.5).shift(LEFT * 3)
        self.add(triangle)

        # Define labels
        vertex_labels = ["Rock", "Paper", "Scissors"]

        # Label the vertices of the triangle
        vertex_text_labels = VGroup()
        for i, vertex in enumerate(triangle.get_vertices()):
            label = Text(vertex_labels[i], font_size=20)
            label.move_to(vertex + 0.4 * normalize(vertex))
            vertex_text_labels.add(label)
        self.add(vertex_text_labels)

        # Create the dot and its path
        dot = Dot(color=RED)
        path = VMobject(color=YELLOW)
        path.set_points_as_corners([triangle.get_center(), triangle.get_center()])

        # Initialize dot position
        dot.move_to(triangle.get_center())

        # Create bar graph
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[-100, 100, 50],
            axis_config={"color": BLUE},
            x_axis_config={"include_numbers": False},
        ).scale(0.5).shift(RIGHT * 3 + DOWN * 0.5)

        x_labels = ["R", "P", "S"]
        for i, label in enumerate(x_labels):
            text = Text(label, font_size=20).next_to(axes.x_axis.number_to_point(i + 0.5), DOWN)
            self.add(text)

        bars = VGroup(*[Rectangle(width=0.5, height=0.001, fill_opacity=1) for _ in range(3)])
        bars[0].set_color(RED)
        bars[1].set_color(GREEN)
        bars[2].set_color(BLUE)

        for i, bar in enumerate(bars):
            bar.next_to(axes.x_axis.number_to_point(i + 0.5), UP, buff=0)

        self.add(axes, bars)

        total_scores = {"rock": 0, "paper": 0, "scissors": 0}

        def play_rps_round(n_players=100):
            scores = {"rock": 0, "paper": 0, "scissors": 0}
            for _ in range(n_players):
                choices = random.choices(['rock', 'paper', 'scissors'], k=2)
                if choices[0] == choices[1]:  # Tie
                    scores[choices[0]] += 0.8
                elif (choices[0] == 'rock' and choices[1] == 'scissors') or \
                     (choices[0] == 'paper' and choices[1] == 'rock') or \
                     (choices[0] == 'scissors' and choices[1] == 'paper'):
                    scores[choices[0]] += 1.5
                    scores[choices[1]] -= 1
                else:
                    scores[choices[1]] += 1.5
                    scores[choices[0]] -= 1
            return scores

        def update_scene(dt):
            nonlocal total_scores
            scores = play_rps_round()
            
            vertices = triangle.get_vertices()
            current_pos = dot.get_center()
            new_pos = current_pos
            
            for i, choice in enumerate(['rock', 'paper', 'scissors']):
                new_pos += scores[choice] * 0.01 * (vertices[i] - current_pos)
                total_scores[choice] += scores[choice]
            
            dot.move_to(new_pos)
            path.add_points_as_corners([new_pos])
            
            # Update bar heights
            for i, choice in enumerate(['rock', 'paper', 'scissors']):
                new_height = total_scores[choice] * 0.01
                bars[i].stretch_to_fit_height(abs(new_height))
                bars[i].next_to(axes.x_axis.number_to_point(i + 0.5), UP if new_height > 0 else DOWN, buff=0)
            
            # Check if dot has reached a vertex
            for vertex in vertices:
                if np.linalg.norm(new_pos - vertex) < 0.1:
                    return False
            return True

        # Add dot and path to scene
        self.add(dot, path)
        
        # Run the animation
        self.add(AnimationGroup(
            UpdateFromFunc(dot, lambda m: m),
            UpdateFromFunc(path, lambda m: m),
            UpdateFromFunc(bars, lambda m: m)
        ))
        
        self.wait(30)

# If running this script directly
if __name__ == "__main__":
    from manim.cli.render.commands import render
    render(RPSTriangleSystemWithGraph(), "RPSTriangleSystemWithGraph", quality="l", preview=True)
