import charts


class Female():
    def __init__(self, bmi):
        self.bmi = bmi

    def print_gender(self):
        return "Female"

    def make_bar_chart(bmi, screen2):
        charts.risk_bar_chart("female.csv", bmi, screen2)

    def make_hori_bar_chart(bmi, screen2):
        charts.hori_bar_chart("male.csv", bmi, screen2)
