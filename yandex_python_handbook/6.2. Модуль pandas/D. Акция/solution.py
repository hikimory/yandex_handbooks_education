import pandas as pd


def cheque(price_list, **order):
    price, number, cost = [], [], []

    for i in order.keys():
        price.append(price_list[i])
        number.append(order[i])
        cost.append(price_list[i] * order[i])

    product_dict = {
        'product': order.keys(),
        'price': price,
        'number': number,
        "cost": cost
    }

    df = pd.DataFrame(product_dict)
    return df.sort_values("product").reset_index(drop=True)


def discount(cheque):
    with_discount = cheque.copy()
    with_discount['cost'] = with_discount['cost'].astype(float)
    with_discount.loc[with_discount['number'] > 2, 'cost'] *= 0.5
    return with_discount


def discount2(cheque):
    with_discount = cheque.copy()
    with_discount['cost'] = with_discount['cost'].astype(float)
    condition = with_discount['number'] > 2
    with_discount.loc[condition, 'cost'] = with_discount.loc[condition, 'cost'] * 0.5
    return with_discount