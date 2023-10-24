class Bill:

    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period


class FlatMate:

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        ratio = self.days_in_house / \
                (self.days_in_house + flatmate.days_in_house)
        to_pay = round(bill.amount * ratio, 2)

        return to_pay
