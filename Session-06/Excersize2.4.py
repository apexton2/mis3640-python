def movetower(height, frompole, topole, withpole):
    if height >= 1
        movetower(height-1, frompole, withpole, topole)
        movedisk(frompole, topole)
        movetower(height-1, withpole, topole, frompole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")
