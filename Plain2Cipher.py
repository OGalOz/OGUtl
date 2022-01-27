
from getpass import getpass

'''
Aleph cipher rotates values of input string
around the alphabet varying amounts, depending
on the input string.
If key == "1aAb2" then the rotation amounts
would be [1,10,37,11,2],
then you'd only need to rotate the string characters those
amounts until the end of the string.
You would rotate them back.
Alphabet needs to be a fixed list.
'''


def Aleph_convert_to_ciphertext(inp_str, alphabet, key=None):
    '''
    Algo Aleph convert to cipher from plain text
    '''
    if not isinstance(inp_str, str) :
        raise Exception("Input must be string.")
    if key is None:
        key = getpass("Please enter key")
    else:
        if not isinstance(key, str):
            raise Exception("Key must be string.")
    rot_list = get_rot_list(key, alphabet)
    ciphertext = rotate_string(rot_list, inp_str, alphabet, direc="f")
    return ciphertext

def Aleph_convert_to_plaintext(inp_str, alphabet, key=None):
    '''
    Algo Aleph convert to plain text from cipher
    '''
    if not isinstance(inp_str, str) :
        raise Exception("Input must be string.")
    if key is None:
        key = getpass("Please enter key")
    else:
        if not isinstance(key, str) :
            raise Exception("Key must be string.")
    rot_list = get_rot_list(key, alphabet)
    plaintext = rotate_string(rot_list, inp_str, alphabet, direc="r")
    return plaintext


def rotate_string(rot_list, inp_str, alphabet, direc="f"):
    # direc "f" for "forward" or "r" for "reverse"
    check_str_in_alphabet(inp_str, alphabet)
    c2ix_rot_map, ix2c_rot_map = get_rotation_maps(alphabet)
    if direc == "f":
        factor = -1
    elif direc == "r":
        factor = 1
    else:
        raise Exception("direc must be one of 'f' or 'r'.")
    A = len(alphabet)
    R = len(rot_list)
    rot_ix = 0
    op_str = ""
    for cr in inp_str:
        crt_ix = c2ix_rot_map[cr]
        rot_amount = factor*rot_list[rot_ix]
        next_val = (crt_ix + rot_amount) % A
        next_char = ix2c_rot_map[next_val]
        op_str += next_char
        if rot_ix == R - 1:
            rot_ix = 0
        else:
            rot_ix += 1

    return op_str

def get_rot_list(inp_str, alphabet):
    check_str_in_alphabet(inp_str, alphabet)
    c2ix_rot_map, ix2c_rot_map = get_rotation_maps(alphabet)
    rot_list = []
    for x in inp_str:
        rot_list.append(c2ix_rot_map[x])

    return rot_list

def check_str_in_alphabet(inp_str, alphabet):
    a_set = set(alphabet)
    for x in inp_str:
        if x not in a_set:
            raise Exception(f"Character {x} not in alphabet.")
    return None

def get_rotation_maps(alphabet):
    '''
    Args:
        alphabet list<str>: List of characters in an alphabet.
    '''
    # Returns two maps  - num to char, char to num
    n2c = {}
    c2n = {}
    for i in range(len(alphabet)):
        n2c[i] = alphabet[i]
        c2n[alphabet[i]] = i

    return c2n, n2c

def get_classic_alphabet():

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    al = list(alphabet)
    return al

def main():
    al = get_classic_alphabet()
    #print(inp_str)
    ciph = Aleph_convert_to_ciphertext(inp_str, al, key=None)
    #print("cipher:", ciph)
    plain = Aleph_convert_to_plaintext(ciph, al, key=None)
    #print("plaintext:", plain)


if __name__ == "__main__":
    main()
