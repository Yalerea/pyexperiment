## 1
nice = 0
naughty = 0
for month in data:
    for day in data[month]:
        if data[month][day] == 'Nice':
            nice += 1
        else:
            naughty += 1
if nice >= naughty:
    return 'Nice!'
else:
    return 'Naughty!'

# # 2
from itertools import product
from itertools import product
def get_pins(observed):
    key = {
            "1" : ["1", "2", "4"],
            "2" : ["1", "2", "3", "5"],
            "3" : ["2", "3", "6"],
            "4" : ["1", "4", "5", "7"],
            "5" : ["2", "4", "5", "6", "8"],
            "6" : ["3", "5", "6", "9"],
            "7" : ["4", "7", "8"],
            "8" : ["5", "7", "8", "9", "0"],
            "9" : ["6", "8", "9"],
            "0" : ["8", "0"]
    }
    list = [ key[ch] for ch in observed]
    return [''.join(item) for item in product(*list)]

# # 3
lists = [rna[i:i+3] for i in range(0, len(rna), 3)]
chain = []
for list in lists:
    if PROTEIN_DICT[list] != 'Stop':
        chain.append(PROTEIN_DICT[list])
    else:
        break
return ''.join(chain)

# 4
return stock.get(merch,0)>=n

# 5
MORSE_CODE['_'] = ' '
def decode_bits(bits):
    bits = bits.strip('0')
    
    if '0' not in bits:
        return '.'
    
    minone = min(len(one) for one in bits.split('0') if one)
    minzero = min(len(zero) for zero in bits.split('1') if zero)
    m = min(minone,minzero)
    
    return bits.replace('111'*m, '-').replace('000000'*m,' _ ').replace('000'*m, ' ').replace('1'*m, '.').replace('0'*m, '')

def decode_morse(morseCode):
    return ''.join(MORSE_CODE[c] for c in morseCode.split())
