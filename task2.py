def card_gen():
    suits = ("diamonds", "spades", "hearts", "clubs")
    values = tuple(["A"]) + tuple(str(i) for i in range(2, 11)) + tuple(["J", "Q", "K"])
    for s in suits:
        for v in values:
            yield f"{v} {s}"


gen = card_gen()
while True:
    i = next(gen)
    print(i)
