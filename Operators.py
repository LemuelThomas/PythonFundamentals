def main():
    """Assignment operators"""
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1
    eligible_items = 'orange banana carrot'
    item_price = 2  # USD

    """Arithmetic Operators"""
    subtotal = item_price * quantity
    print(f"item_name: {item_name}, subtotal: {subtotal}")
    discount = 0
    """Membership Operators"""
    if item_name in eligible_items:  # 'if the value of item name is in eligible items then run the command.'
        discount = subtotal * discount_rate

    print(f"discount: {discount}")
    was_discount_applied = discount > 0  # 'This will give me a boolean value of true.'
    print(f"Was the discount applied? {was_discount_applied}")

    """Logical Operators"""
    does_free_shipping_apply = quantity >= 5 and item_name == 'banana'
    print(f"Is this item eligible for free shipping? {does_free_shipping_apply}")


if __name__ == '__main__':
    #  '__name__ is used to determine whether the python script is being run as the main method'
    #  'or if it's being imported from another script.'
    #  'This code block will execute when the script is run as the main program.'
    main()
