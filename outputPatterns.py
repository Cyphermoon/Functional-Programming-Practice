# Write a problem to produce a hash symbols shaped like half of a perfect 5 *5

def produceHalfSquareOutputPattern():
    row = 5
    outputs = []

    for i in range(1, 6):
        outputs.append("#" * (6 - i))

    return outputs


def sideWayTriangleOutputPattern():
    row = 7

    for row in range(1, 8):
        formula = (4 - abs(4 - row))

        print("#" * formula, formula)




