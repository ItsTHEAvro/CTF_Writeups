Author: madStacks

#### Description
I wonder what this really is... [enc](./enc)

`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

#### Write-up
Got the flag using the **magic** function in [Cyberchef](https://gchq.github.io/CyberChef/)

<details>
 <summary>Flag</summary>
 ```picoCTF{16_bits_inst34d_of_8_d52c6b93}```
</details>

From [Cyberchef](https://gchq.github.io/CyberChef/) it is clear that if the character encoding is changed to UTF-16BE, we will get the flag.  

To do this in python, 
```python
encoded_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"
print(encoded_flag.encode('utf-16-be'))
```