from manim import *
import numpy as np

class RandomDotInLabeledTriangle(Scene):
    def construct(self):
        # Create and add the triangle
        triangle = Triangle().scale(3)
        self.add(triangle)

        vertex_labels = ["Rock", "Paper", "Scissors"]

        # Label the vertices of the triangle
        vertex_text_labels = VGroup()
        for i, vertex in enumerate(triangle.get_vertices()):
            label = Text(vertex_labels[i], font_size=24)
            label.move_to(vertex + 0.4 * normalize(vertex))
            vertex_text_labels.add(label)
        self.add(vertex_text_labels)

        # Create the dot and its path
        dot = Dot(color=RED)
        path = VMobject(color=YELLOW)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        # Function to check if a point is inside the triangle
        def is_inside_triangle(point):
            vertices = triangle.get_vertices()
            a, b, c = vertices
            v0, v1, v2 = b - a, c - a, point - a
            d00 = np.dot(v0, v0)
            d01 = np.dot(v0, v1)
            d11 = np.dot(v1, v1)
            d20 = np.dot(v2, v0)
            d21 = np.dot(v2, v1)
            denom = d00 * d11 - d01 * d01
            v = (d11 * d20 - d01 * d21) / denom
            w = (d00 * d21 - d01 * d20) / denom
            return v >= 0 and w >= 0 and v + w <= 1

        # Initialize dot position
        dot.move_to(triangle.get_center())

        # Animation function for dot movement
        def update_dot(dot, dt):
            current_pos = dot.get_center()
            direction = np.random.uniform(-1, 1, 3)
            direction[2] = 0  # Ensure movement is in 2D
            direction = direction / np.linalg.norm(direction)
            new_pos = current_pos + direction * 0.1
            
            if is_inside_triangle(new_pos):
                dot.move_to(new_pos)
                path.add_points_as_corners([new_pos])

        # Add dot and path to scene and start the animation
        self.add(dot, path)
        dot.add_updater(update_dot)
        
        # Run the animation for 10 seconds
        self.wait(10)

# If running this script directly
if __name__ == "__main__":
    from manim.cli.render.commands import render
    render(RandomDotInLabeledTriangle(), "RandomDotInLabeledTriangle", quality="l", preview=True)
