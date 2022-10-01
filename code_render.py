from manim import *
from nn_manim import NeuralNetworkMobject
from screens import GrowArrowCustom
import os

config.ffmpeg_executable = r"C:\Program Files\FFMPEG\bin\ffmpeg.exe"


class Testing(Scene):
    def construct(self):
        title = Text("Exploration vs Exploitation")
        title.set_x(-2)
        title.set_y(3)

        q_values = Tex(r"Q Learning introduces ", "Q values", ". For each state,\\there is a Q value for every action.",
                       font_size=46)
        q_values.set_color_by_tex("Q values", ORANGE)
        q_values.set_y(.4)

        perfect_text = Tex(r"In a perfect solution, the greatest Q value represents\\the best action for the state.",
                           font_size=46)
        perfect_text.set_y(-1.1)

        self.play(
            Write(q_values),
            Write(perfect_text)
        )


"""
class AnimateCode(Scene):
    def construct(self):
        code = '''
# hyperparameters copied from global settings
self.learning_rate = gs.LEARNING_RATE
self.discount_rate = gs.DISCOUNT_RATE
self.exploration_probability = gs.EXPLORATION_PROBABILITY
self.exploration_decay = gs.EXPLORATION_DECAY
self.network_copy_steps = gs.TARGET_NET_COPY_STEPS
'''

        listing = Code(
            code=code,
            background_stroke_width=2,
            background_stroke_color=ORANGE,
            background=BLACK,
            language="Python",
            font="Consolas",
            font_size=24,
            style="gruvbox-dark"
        )
        self.add(listing)
"""

if __name__ == "__main__":
    os.system("pipenv run manim render code_render.py -qm -t")
