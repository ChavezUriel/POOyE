class star:
    def __init__(self, UVMag, blueMag,  AbsMag, typeStar):
        self.UVMag = UVMag
        self.blueMag = blueMag
        self.AbsMag = AbsMag
        self.typeStar = typeStar

    def typeStar(blueMag,AbsMag):
        difMag = blueMag - AbsMag
        typeStar = ''
        if (difMag < -0.31):
            typeStar = 'O5'
        elif (difMag < -0.16):
            typeStar = 'BO'
        elif (difMag < 0):
            typeStar = 'B5'
        elif (difMag < 0.13):
            typeStar = 'AO'
        elif (difMag < 0.27):
            typeStar = 'A5'
        elif (difMag < 0.42):
            typeStar = 'F0'
        elif (difMag < 0.58):
            typeStar = 'F5'
        elif (difMag < 0.70):
            typeStar = 'GO'
        elif (difMag < 0.89):
            typeStar = 'G5'
        elif (difMag < 1.18):
            typeStar = 'KO'
        elif (difMag < 1.45):
            typeStar = 'K5'
        elif (difMag < 1.63):
            typeStar = 'MO'
        elif (difMag < 1.80):
            typeStar = 'M5'
        else:
            typeStar = 'M8'
        return typeStar