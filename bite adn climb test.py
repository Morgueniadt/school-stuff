mode = int(input("would you like to use \n(1)Simple mode\n(2)Long mode\n please enter the number of the mode you wish to play:"))

if mode == 1:

    snakes =  {
        8: 4,
        18: 1,
        26: 10,
        39: 5,
        51: 6,
        54: 36,
        56: 1,
        60: 23,
        75: 28,
        83: 45,
        85: 59,
        90: 48,
        92: 25,
        97: 87,
        99: 63
    }
    # ladders dictionaries , deifning where ladders go
    ladders = {
        3: 20,
        6: 14,
        11: 28,
        15: 34,
        17: 74,
        22: 37,
        38: 59,
        49: 67,
        57: 76,
        61: 78,
        73: 86,
        81: 98,
        88: 91
    }
elif mode == 2:
    snakes  = {
        18: 1,
        26: 10,
        51: 6,
        54: 36,
        60: 23,
        83: 45,
        85: 59,
        90: 48,
        97: 87,
    }
    # ladders dictionaries , deifning where ladders go
    ladders ={
        3: 20,
        6: 14,
        11: 28,
        15: 34,
        17: 74,
        22: 37,
        38: 59,
        49: 67,
        57: 76,
        61: 78,
        73: 86,
    }




