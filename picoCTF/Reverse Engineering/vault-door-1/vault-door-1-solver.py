java_code = """
    password.charAt(0)  == 'd' &&
    password.charAt(29) == 'a' &&
    password.charAt(4)  == 'r' &&
    password.charAt(2)  == '5' &&
    password.charAt(23) == 'r' &&
    password.charAt(3)  == 'c' &&
    password.charAt(17) == '4' &&
    password.charAt(1)  == '3' &&
    password.charAt(7)  == 'b' &&
    password.charAt(10) == '_' &&
    password.charAt(5)  == '4' &&
    password.charAt(9)  == '3' &&
    password.charAt(11) == 't' &&
    password.charAt(15) == 'c' &&
    password.charAt(8)  == 'l' &&
    password.charAt(12) == 'H' &&
    password.charAt(20) == 'c' &&
    password.charAt(14) == '_' &&
    password.charAt(6)  == 'm' &&
    password.charAt(24) == '5' &&
    password.charAt(18) == 'r' &&
    password.charAt(13) == '3' &&
    password.charAt(19) == '4' &&
    password.charAt(21) == 'T' &&
    password.charAt(16) == 'H' &&
    password.charAt(27) == '6' &&
    password.charAt(30) == 'f' &&
    password.charAt(25) == '_' &&
    password.charAt(22) == '3' &&
    password.charAt(28) == 'd' &&
    password.charAt(26) == 'f' &&
    password.charAt(31) == '4'
"""

lines = java_code.strip().split('\n')

arr = [''] * 32

for line in lines:
  char_index = int(line[line.index('(')+1:line.index(')')])
  char_value = line.split("'")[1]
  arr[char_index] = char_value

print("picoCTF{" + ''.join(arr) + "}")