#### Description

Can you get the flag? Reverse engineer this Python [program](./unpackme.flag.py).

#### Writeup

When we run the program it asks for a password. Reading the program we can see that the `payload` is being decrypted and then run.  
We can comment out the `exec` line to prevent the script from running and add the following line at the end.  
We get the flag in the output when we run the program.  
After modifying, out program looks like the following.

```python
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
# exec(plain.decode())
print(plain.decode())

```

When we run the program we can see the original decoded program.

```python
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_cd82f94c}')
else:
  print('That password is incorrect.')
```

We get the flag in the code. We also get the password which is `batteryhorse`.

<details>
 <summary>Flag</summary>
 picoCTF{175_chr157m45_cd82f94c}
</details>
