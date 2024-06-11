#### Description

Can you get the flag?  
Download [this binary](./gdbme).  
Here's the test drive instructions:

```bash
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

#### Write-up

We follow the instructions given and get the flag.

<details>
 <summary>Flag</summary>
 picoCTF{d3bugg3r_dr1v3_72bd8355}
</details>
