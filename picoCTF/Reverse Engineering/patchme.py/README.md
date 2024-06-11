#### Description

A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](./run).

#### Write-up

Reading the `patchme.flag.py` we see the block that condition that checks for the password it the following one.

```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")
```

We can simply remove the input function, condition check and run the code inside the `if` block always in the following way.

```python
def level_1_pw_check():
    print("Welcome back... your flag, user:")
    decryption = str_xor(flag_enc.decode(), "utilitarian")
    print(decryption)
    return
```



When we run the python script again it gives us the flag.

<details>
 <summary>Flag</summary>
 picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
</details>

