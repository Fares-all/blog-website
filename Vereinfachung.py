def boolean_expression(a, b, c):
    term1 = (a and b)
    term2 = (a and c)
    term3 = (b and (not c))

    result = term1 or term2 or term3
    return result
a = True
b = False
c = True

result = boolean_expression(a, b, c)
print(f"Ergebnis für a={a}, b={b}, c={c}: {result}")

def boolean_expression(a, b, c):

    term1 = (a and b)
    term2 = (a and c)
    term3 = (b and (not c))
    
    # Neue Variable
    new_variable = True

    # Neuer Term
    term4 = (a or new_variable)

    result = term1 or term2 or term3 or term4
    return result
