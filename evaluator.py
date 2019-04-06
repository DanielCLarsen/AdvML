from odd_one_out_loader import load_odd_one_out


def evaluate(model):
    odd_one_out = load_odd_one_out()

    correct = 0
    know = 0
    dont_know = 0
    total = 0
    for row in odd_one_out[1:]:
        total += 1
        try:
            index = model.predict(row)
            know += 1
            if index == 3:
                correct += 1
        except Exception as e:
            print(e)
            dont_know += 1
            continue

    print("acc", correct / total)
    print("know", know)
    print("dont_know", dont_know)
