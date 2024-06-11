#### Description

Can you open this safe?  
I forgot the key to my safe but this [program](SafeOpener.java) is supposed to help me with retrieving the lost key.
Can you help me unlock my safe?  
Put the password you recover into the picoCTF flag format like:

picoCTF{password}

#### Write-up

From the file `SafeOpener.java` we see that a string is input into the program and then it is encoded using `Base64.Encoder`. After encoding, the encoded string is compared to a variable named `encodedkey`. If our input is the correct password, we get `sesame open`.

So, what we can conclude is that the string `encodedkey` is encoded using Base64. We can simply use a Base64 decoder to get the correct password.

We can use any online tool, or Python to decode the string.  
Here is the python code to decode a base64 encoded string.

```python
import base64
encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

print(base64.b64decode(encodedkey))
```

<details>
 <summary>Flag</summary>
 picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
</details>
