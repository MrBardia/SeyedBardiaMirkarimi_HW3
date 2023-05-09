#! usr/bin/python3

def apply_discount(price: int, discount: float = 0.0) -> int:
    final_price = int(price*(1 - discount))
    try:
        assert(
            0 < final_price <= price
        )
    except AssertionError:
        print("Discount should be less than 1")

    return final_price

apply_discount(1000, 1.5)

"""
    assertion error niaz be handle shodan dasht va baiad ba try...except error uno hal kard.
"""

