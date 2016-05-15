from PyMoneyOrga.account import Account


if __name__ == '__main__':
    acc_daniel = Account('Acc_Daniel',1000)
    acc_daniel.add_cash(100)
    print(acc_daniel.get_cash())