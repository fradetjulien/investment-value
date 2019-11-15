import click

def set_interest_rate():
    '''
    Recover the interest rate applied to the investment in the CLI
    '''
    while True:
        try:
            interest_rate = float(input('Enter the interest rate applied to the investment :\n'))
            if interest_rate <= 0:
                print('Error, the value must be a float.\n')
                continue
        except ValueError:
            print("Error, enter a float number please.\n")
            continue
        else:
            break
    return interest_rate

def set_characteristic(instruction):
    '''
    Recover a characteristic in the CLI
    '''
    while True:
        try:
            characteristic = int(input(instruction))
            if characteristic <= 0:
                print("Error, the value can't be equal or inferior to zero.\n")
                continue
        except ValueError:
            print("Error, enter a number please.\n")
            continue
        else:
            break
    return characteristic

def set_investment_characteristics(item, value):
    '''
    Insert the investment characteristics inside a dictionnary
    '''
    investment_characteristics = {
        "FV": None,
        "PV": None,
        "r": None,
        "n": None
    }
    investment_characteristics[item] = set_characteristic('Enter the {} value :\n'.format(value))
    investment_characteristics["r"] = set_interest_rate()
    investment_characteristics["n"] = set_characteristic('Enter the number of years :\n')
    return investment_characteristics

def compute_future_value():
    '''
    Compute the futur value thanks to the investment characteristics
    '''
    investment_characteristics = set_investment_characteristics("PV", "present")
    try:
        investment_characteristics["FV"] = investment_characteristics["PV"] \
                                           * ((1 + investment_characteristics["r"]) \
                                           **investment_characteristics["n"])
    except:
        print("Sorry, we were unable to compute the Future Value.")
    return investment_characteristics["FV"]

def compute_present_value():
    '''
    Compute the present value thanks to the investment characteristics
    '''
    investment_characteristics = set_investment_characteristics("FV", "future")
    try:
        investment_characteristics["PV"] = investment_characteristics["FV"] \
                                            / ((1 + investment_characteristics["r"]) \
                                            **investment_characteristics["n"])
    except:
        print("Sorry, we were unable to compute the Present Value.")
    return investment_characteristics["PV"]

@click.group()
def cli():
    '''
    Compute Future or Present investment value
    '''

@cli.command('future')
def get_future_value():
    '''
    Recover the Future Value and then display it
    '''
    future_value = compute_future_value()
    if future_value:
        print("Future value = {}".format(future_value))

@cli.command('present')
def get_present_value():
    '''
    Recover the Present Value and then display it
    '''
    present_value = compute_present_value()
    if present_value:
        print("Present Value = {}".format(present_value))

if __name__ == '__main__':
    cli()
