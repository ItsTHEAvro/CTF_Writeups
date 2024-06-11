#### Writeup

If we look at `crackme.py` we see that there is a function named `decode_secret` which is defined but not called. Also, we see two strings `bezos_cc_secret` and `alphabet` which are initialized but not used.

```python
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)
```

Running `crackme.py` calls the `choose_greatest` function. We can simply comment it out and run the function `decode_secret` with the parameter `bezos_cc_secret` and run the file to get the flag.

<details>
 <summary>Flag</summary>
 `picoCTF{1|\/|_4_p34|\|ut_f3bc410e}`
</details>
