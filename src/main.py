import pandas as pd
import numpy as np
from utils import suma, resta, mult
from module1 import city

def main():
    print(f'resultado suma #2 es: ', suma(10,9))
    print(f'resultado resta #2 es: ', resta(10,40))
    print(f'resultado multiplicacion #2: ', mult(6,8))

    print('='*64)

    print(f'The city is Colombia: ', city('Colombia') )

if __name__=='__main__':
    main()


