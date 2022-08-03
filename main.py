import cash_on_hand, profit_loss, api, overheads
def main():
    forex = api.api()
    overheads.overheads(forex)
    cash_on_hand.cash(forex)
    profit_loss.profitloss(forex)
    print(forex)
print(main())