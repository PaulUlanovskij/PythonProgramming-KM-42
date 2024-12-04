def binomial_quotients(n):
    previous_layer = [1]
    yield previous_layer
    layer = []
    for layer_index in range(1, n+1):
        layer.append(1)
        for i in range(0, len(previous_layer)-1):
            layer.append(previous_layer[i] + previous_layer[i + 1])
        layer.append(1)
        previous_layer = layer
        layer = []
        yield previous_layer


s_input = ''
power = 0
try:
    s_input = input("Enter integer power of binomial: ")
    while s_input.isdigit() is False or int(s_input) <= 0:
        s_input = input("Enter integer power of binomial that is bigger than 0: ")
    power = int(s_input)
except KeyboardInterrupt:
    pass
else:
    gen = binomial_quotients(power)
    for i in gen:
        print(*i)
