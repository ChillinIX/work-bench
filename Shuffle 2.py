from typing import Collection


import random

ll = ['Tony ','Stephen ','Alex ','Emily ','Jana ']
random.shuffle(ll)
for i in range(len(ll)):
    print(''.join(ll[i:]))

