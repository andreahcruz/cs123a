import os

def print_grna(filename):
    # function returns list of grna's from text file
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, filename)

    with open(filename, "r") as f:
        next(f)  # skip first line in file
        # removes newline/comments starting with ">" and puts gRNA seqs in list
        grna_list = [line.strip() for line in f if not line.startswith(">")]

    # print(grna_list)
    return grna_list


def gc_content(list):
    # function returns a dict with grna seqs & scores based on gc percent
    scores = {}  # key: grna seq, value: score (100 potency upon init)
    gc_dict = {}  # maps values of seq to gc percent

    for grna in list:  # takes a grna
        # init base counts
        c = a = g = t = 0

        for elem in str(grna).upper():  # take each char from the grna
            if elem == "C":
                c += 1
            elif elem == "G":
                g += 1
            elif elem == "A":
                a += 1
            elif elem == "T":
                t += 1

        # print("C=%d, G=%d, A=%d, T=%d" % (c, g, a, t))  # print base counts
        gc_content = (g + c) * 100 / (a + t + g + c)  # get gc percent from total
        # print("gc_content= %f" % (gc_content))
        gc_dict[grna] = gc_content
        scores[grna] = 100  # init scores to 100

    print(gc_dict)  # print gc percent of each sequence
    print(scores)

    # decrease goodness score if gc content is higher than 57%
    for key in gc_dict:
        # print(key)
        # print(gc_dict.get(key))
        if gc_dict.get(key) > 57:
            scores[key] = scores.get(key) - 1

    print(scores)

    return scores


if __name__ == '__main__':
    grna_list = print_grna('test')
    grna_scores = gc_content(grna_list)
