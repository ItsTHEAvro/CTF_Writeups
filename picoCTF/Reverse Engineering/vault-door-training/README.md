#### Description

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](./VaultDoorTraining.java)

#### Writeup

Taking a look at `VaultDoorTraining.java` we see the program takes an input into the variable `input` and then checks the input against another string in the `checkPassword` method.  
Below is the `checkPassword` method definition.

```java
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46");
}
```

The flag is given as plaintext in the code.

<details>
 <summary>Flag</summary>
 `picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}`
</details>
