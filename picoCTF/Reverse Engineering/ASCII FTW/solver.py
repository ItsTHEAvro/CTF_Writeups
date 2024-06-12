values = """        
        00101184 c6 45 d0 70     MOV        byte ptr [RBP + local_38],0x70
        00101188 c6 45 d1 69     MOV        byte ptr [RBP + local_37],0x69
        0010118c c6 45 d2 63     MOV        byte ptr [RBP + local_36],0x63
        00101190 c6 45 d3 6f     MOV        byte ptr [RBP + local_35],0x6f
        00101194 c6 45 d4 43     MOV        byte ptr [RBP + local_34],0x43
        00101198 c6 45 d5 54     MOV        byte ptr [RBP + local_33],0x54
        0010119c c6 45 d6 46     MOV        byte ptr [RBP + local_32],0x46
        001011a0 c6 45 d7 7b     MOV        byte ptr [RBP + local_31],0x7b
        001011a4 c6 45 d8 41     MOV        byte ptr [RBP + local_30],0x41
        001011a8 c6 45 d9 53     MOV        byte ptr [RBP + local_2f],0x53
        001011ac c6 45 da 43     MOV        byte ptr [RBP + local_2e],0x43
        001011b0 c6 45 db 49     MOV        byte ptr [RBP + local_2d],0x49
        001011b4 c6 45 dc 49     MOV        byte ptr [RBP + local_2c],0x49
        001011b8 c6 45 dd 5f     MOV        byte ptr [RBP + local_2b],0x5f
        001011bc c6 45 de 49     MOV        byte ptr [RBP + local_2a],0x49
        001011c0 c6 45 df 53     MOV        byte ptr [RBP + local_29],0x53
        001011c4 c6 45 e0 5f     MOV        byte ptr [RBP + local_28],0x5f
        001011c8 c6 45 e1 45     MOV        byte ptr [RBP + local_27],0x45
        001011cc c6 45 e2 41     MOV        byte ptr [RBP + local_26],0x41
        001011d0 c6 45 e3 53     MOV        byte ptr [RBP + local_25],0x53
        001011d4 c6 45 e4 59     MOV        byte ptr [RBP + local_24],0x59
        001011d8 c6 45 e5 5f     MOV        byte ptr [RBP + local_23],0x5f
        001011dc c6 45 e6 33     MOV        byte ptr [RBP + local_22],0x33
        001011e0 c6 45 e7 43     MOV        byte ptr [RBP + local_21],0x43
        001011e4 c6 45 e8 46     MOV        byte ptr [RBP + local_20],0x46
        001011e8 c6 45 e9 34     MOV        byte ptr [RBP + local_1f],0x34
        001011ec c6 45 ea 42     MOV        byte ptr [RBP + local_1e],0x42
        001011f0 c6 45 eb 46     MOV        byte ptr [RBP + local_1d],0x46
        001011f4 c6 45 ec 41     MOV        byte ptr [RBP + local_1c],0x41
        001011f8 c6 45 ed 44     MOV        byte ptr [RBP + local_1b],0x44
        001011fc c6 45 ee 7d     MOV        byte ptr [RBP + local_1a],0x7d
"""
characters = []

for line in values.strip().split("\n"):
 characters.append(line.split("0x")[1])

x = ''.join(characters)

print(bytearray.fromhex(x).decode())
