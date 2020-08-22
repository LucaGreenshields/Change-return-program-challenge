uk_denom_list = [("dollar", 100), ("quarter", 25), ("dime", 10), ("nickel", 5), ("penny", 1)]

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
    cost = float(input("What is the cost of the item: "))
    amount = float(input("What is the amount of money offered: "))
    return int(cost * 100), int(amount * 100)

def main():
    cost, amount = get_cost_and_money()
    change = amount - cost
    result = format_list(remove_zero_denom(change_list(change, uk_denom_list)))
    print("The change is: ")
    print(result)

main()
