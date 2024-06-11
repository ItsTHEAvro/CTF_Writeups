#### Writeup

This is the function that checks the key.

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True
```

We can see that the function basically uses `hashlib.sha256().hexdigest()` method on `username_trial` and checks the characters in the order `4, 5, 3, 6, 2, 7, 1, 8`. So we can simply use the same method on `username_trial` which is `FRASER` and generate the sha256 hash and get the flag with the given character order.

Using `username_trial` gives us the following error.

```python
generated_hash = hashlib.sha256(username_trial).hexdigest()
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Strings must be encoded before hashing
```

So, we use `bUsername_trial` which is set to `b"FRASER"` which is a byte string. Now if we run the solver script we get the flag.

<details>
 <summary>Flag</summary>
 ```picoCTF{1n_7h3_|<3y_of_ac73dc29}```
</details>
