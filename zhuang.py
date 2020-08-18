class account(object):
    """class,amount is us dollars"""
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """class,sum dollars"""
        return self.__amt

    @property
    def cny(self):
        """china renmingbi"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("sorry,no negative amount in the account.")
            return
        self.__amt = value
if __name__ == "__main__":
    acc = account(rate=6.6)
    acc.amount = 20
    print("dollar amount:", acc.amount)
    print("in cny:", acc.cny)
    acc.amount = -100
    print("dollar amount:", acc.amount)
