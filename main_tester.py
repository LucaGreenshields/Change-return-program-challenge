import random

uk_denom_list = [("pound", 100), ("50p", 50), ("20p", 20), ("10p", 10), ("5p", 5), ("2p", 2), ("1p", 1)]

def divide(change, coin):
    return change//coin, change % coin

def change_list(amount, denom_list):
    remainder = amount
    result_list = []
    for name, value in denom_list:
        count, new_remainder = divide(remainder, value)
        result_list.append((name, value, count))
        remainder = new_remainder
    return result_list

def remove_zero_denom(change_list):
    return [denom_tuple for denom_tuple in change_list if denom_tuple[2] != 0]

def format_list(change_list):
    string_list = [f"{name} x {count}" for name, value, count in change_list]
    return "\n".join(string_list)

def get_cost_and_money():
    cost = random.randint(200, 1000) / 100
    amount = cost + random.randint(200, 1000) / 100
    return int(cost * 100), int(amount * 100)

def sum_change_list(change_list):
    value_list = [value * count for name, value, count in change_list]
    return sum(value_list) / 100





def main():
    cost, amount = get_cost_and_money()
    print(f"Cost of item is {cost / 100}")
    print(f"Money offered is {amount / 100}")
    change = amount - cost
    result_list = remove_zero_denom(change_list(change, uk_denom_list))
    result = format_list(result_list)
    print("The change is: ")
    print(result)
    sum_of_change = sum_change_list(result_list)
    print(f"The sum of the change is: {sum_of_change}")
    print(f"Change + cost is: {sum_of_change + cost/100}")
    print(f"Money offered is {amount / 100}")
    
main()
