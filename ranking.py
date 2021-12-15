import os
import seaborn as sns
import matplotlib.pyplot as plt

class Ranking1337:
    def __init__(self):
        self.score_dict = dict()
        self.cheat_dict = dict()
    
    def display_message(self,
        name,
        time,
        msg,
        is_cheater=False,
    ):
        if is_cheater:
            print("CHEATER")
        print(f'{name} @ {time}:')
        print(msg)
        print("")
        
    def logic(self, name, time, date, msg, display_messages, display_cheat_messages):
        self.legal_logic(name, time, date, msg, display_messages)
        self.cheat_logic(name, time, msg, display_cheat_messages)
        
    def legal_logic(self, name, time, date, msg, display_messages):
        if time == "13:37" and msg == "1337":
            self.score_dict[name] = self.score_dict.get(name, 0) + 1
            if name.lower() == "quinten":
                print(f"Orig time: {date}")
            if display_messages:
                self.display_message(name, time, msg)
    
    def cheat_logic(self, name, time, msg, display_cheat_messages):
        if msg == "1337" and time != "13:37":
            time_int = time.replace(":", "")
            if abs(int(time_int) - 1337) > 1:
                self.cheat_dict[name] = self.cheat_dict.get(name, 0) + 1
                if display_cheat_messages:
                    self.display_message(name, time, msg)

    def generate_ranking1337(
        self,
        lines,
        display_messages = False,
        display_cheat_messages = False
    ):

        for i, line in enumerate(reversed(lines)):
            split = line.split(" ")
            time = ""
            if len(split) >= 4:
                date = split[0]
                time = split[1][0:5]
                name = split[2].replace(":","")
                msg = split[3].strip()
                if name.lower() == "nick": # Nick is called Nick S. on whatsapp
                    msg = split[4].strip()
                    
                self.logic(name, time, date, msg, display_messages, display_cheat_messages)

        ranking = {k: v for k, v in sorted(self.score_dict.items(), key=lambda item: item[1], reverse=True)}
        cheat_ranking = {k: v for k, v in sorted(self.cheat_dict.items(), key=lambda item: item[1], reverse=True)}
        
        return ranking, cheat_ranking


class Plotter:
    def __init__(self):
        pass
    
    def barplot(self, ranking: dict, fig_name):
        keys = list(ranking.keys())
        values = list(ranking.values())

        bar_plot = sns.barplot(keys, values)
        img_dir = "img"
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        file_name = os.path.join(img_dir, f"{fig_name}.png")
        plt.savefig(file_name)

        # fig = bar_plot.get_figure()
        # fig.savefig(fig)