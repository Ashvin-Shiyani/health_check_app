import charts


class Male():
    def __init__(self, bmi):
        self.bmi = bmi

    def print_gender(self):
        return "Male"

    def make_bar_chart(bmi, screen2):
        charts.risk_bar_chart("male.csv", bmi, screen2)
