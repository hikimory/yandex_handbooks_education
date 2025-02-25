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