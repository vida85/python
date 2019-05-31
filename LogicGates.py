# 7 Logic Gates by Davi Silveira

def and_gate(n1, n2):
    if n1 and n2:
        return True
    else:
        return False


def nand_gate(n1, n2):
    if n1 and n2:
        return False
    else:
        return True


def not_gate(n1):
    if n1:
        return False
    else:
        return True


def or_gate(n1, n2):
    if n1 == False and n2 == False:
        return False
    else:
        return True


def nor_gate(n1, n2):
    if n1 == False and n2 == False:
        return True
    else:
        return False


def xor_gate(n1, n2):
    if n1 == False and n2 == True or n2 == False and n1 == True:
        return True
    else:
        return False


def xnor_gate(n1, n2):
    if n1 == False and n2 == True or n2 == False and n1 == True:
        return False
    else:
        return True




def light_bulb(n1):
    if n1: # if True
        return "ON"
    else: # if False
        return "OFF"


print(light_bulb(or_gate(not_gate(1), 1)))

