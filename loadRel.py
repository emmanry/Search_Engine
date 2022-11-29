def loadRel(filename):
    relDocsInQuery = {}
    lines = open(filename, encoding="utf-8").readlines()

    for i in range(len(lines)):
        tokens = lines[i].strip().split()

        idQuery = tokens[0]
        if idQuery in relDocsInQuery.keys():
            relDocsInQuery[idQuery].append(tokens[1])
        else :
            relDocsInQuery[idQuery] = [tokens[1]]

    return relDocsInQuery