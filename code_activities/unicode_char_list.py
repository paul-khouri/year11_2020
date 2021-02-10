import binascii
print(binascii.a2b_uu("h"))
print(binascii.a2b_qp("h", header=False))
print(chr(57344))

def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)

for i in range(0,128):
    char =  chr(i)
    print(char)
    print(ord(char))
    binary = make_bitseq(char)
    print(binary)
    print(int(binary,2))


    
