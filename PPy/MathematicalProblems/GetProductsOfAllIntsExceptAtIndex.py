def get_products_of_all_ints_except_at_index(int_list):
    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

  
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    print(products_of_all_ints_except_at_index)

int_list = [2, 4, 5, 6]
get_products_of_all_ints_except_at_index(int_list)