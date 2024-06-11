#### Description

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](VaultDoor1.java)

#### Write-up

Inspecting the code we see

```java
public boolean checkPassword(String password) {
        return password.length() == 32 &&
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
               password.charAt(31) == '4';
    }
}
```

This code essentially says that the length of the password is 32 characters and a specific character has its specific position. We just need to sort all the charAt from 0 to 31 and then get the respective order of the characters. That will be the flag.

First we take the java code for the scrambled password into a string.

```python
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
```

Let's split the string into a list.

```python
lines = java_code.strip().split('\n')
```

Let's create an array of 32 characters and we can then use the index to put the characters into their respective places.

```python
arr = [''] * 32
```

Let's iterate each item in the `lines` array and get the indices and the values from each item and then place the characters into their respective indices.

```python
for line in lines:
  char_index = int(line[line.index('(')+1:line.index(')')])
  char_value = line.split("'")[1]
  arr[char_index] = char_value
```

Let's simply join out array and get the flag.

```python
print("picoCTF{" + ''.join(arr) + "}")
```

<details>
 <summary>Flag</summary>
 picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}
</details>
