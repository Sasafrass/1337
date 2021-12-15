import os
import matplotlib.pyplot as plt
import seaborn as sns
from ranking import Ranking1337, Plotter

sns.set()
sns.set_style('darkgrid')

data_folder = "data"
filename = os.path.join(data_folder, "fullvax_chat.txt")

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

ranker = Ranking1337()
normal_ranking, cheat_ranking = ranker.generate_ranking1337(
    lines=lines,
    display_messages=False,
    display_cheat_messages=True
)

plotter = Plotter()

plotter.barplot(normal_ranking, fig_name="normal")

plotter.barplot(cheat_ranking, fig_name="cheat")