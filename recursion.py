def recursion(level):
    if level == 100:
        print("done")
    else:
        print("my level is %s" % level)
        recursion(level+1)

recursion(1)
