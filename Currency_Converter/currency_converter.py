from Currency_Converter.exchange_rates import GBP_TO_EUR, GBP_TO_USD, GBP_TO_BGN

def convert_to_eur(amount):
    as_eur = amount * GBP_TO_EUR
    print(f"{amount:.2f} GBP = {as_eur:.2f} EUR ")


def convert_to_usd(amount):
    as_eur = amount * GBP_TO_USD
    print(f"{amount:.2f} GBP = {as_eur:.2f} USD ")


def convert_to_bgn(amount):
    as_eur = amount * GBP_TO_BGN
    print(f"{amount:.2f} GBP = {as_eur:.2f} BGN ")


def main():
    amount = float(input("Input the amount you want to convert: "))
    currency = str(input("Choose a currency to convert to (USD,EUR,BGN): ")).upper()

    if currency == "EUR":
        convert_to_eur(amount)
    elif currency == "USD":
        convert_to_usd(amount)
    elif currency == "BGN":
        convert_to_bgn(amount)
    else:
        print("We don't support this currency!")



main()




