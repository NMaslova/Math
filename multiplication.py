def multiply_two(x, y):
    """
    Returns product of x times y

    :param x: first integer as a seq of chars
    :param y: second integer as a seq of chars
    :rtype: integer
    """

    def karatsuba(x, y, start, end):
        """
        Multiplies two integers with Karatsuba algo:

        x = 10^(n/2) * a + b
        y = 10^(n/2) * c + d

        x * y = 10^n*a*b + 10^(n/2)*(a*d+b*c) + b*d ,
        where ad + bc = (a+b)(c+d) - ac - bd

        :param start:
        :param end:
        :return:
        """

        depth = end - start + 1

        if depth == 2:

            a = int(x[start])
            b = int(x[end])
            c = int(y[start])
            d = int(y[end])

            ac = a*c
            bd = b*d
            gauss_trick = (a+b)*(c+d) - ac - bd

            product = ac*100 + gauss_trick*10 + bd
            return product

        left_start = start
        left_end = int(depth/2)
        right_start = left_end + 1
        right_end = end

        left_depth = left_end - left_start + 1
        right_depth = right_end - right_start + 1

        a = int(x[left_start:left_end])
        b = int(x[right_start:right_end])
        c = int(y[left_start:left_end])
        d = int(y[right_start:right_end])

        if left_depth != 1 and right_depth != 1:
            ac = karatsuba(x, y, left_start, left_end)
            bd = karatsuba(x, y, right_start, right_end)
        else:
            ac = a*c
            bd = b*d

        gauss_trick = multiply_two(str(a+b), str(c+d)) - ac - bd



    y_len = len(y)
    x_len = len(x)

    if y_len == 1 or x_len == 1:
        return int(int(x)*int(y))

    diff = abs(y_len - x_len)
    general_len = max(y_len, x_len)
    zeros_str = ''

    if diff != 0:

        for i in range(diff):
            zeros_str += '0'

        if y_len < x_len:
            y = zeros_str + y
        else:
            x = zeros_str + x

    result = karatsuba(0, general_len-1)
    return result
