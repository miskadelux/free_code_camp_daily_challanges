Problem: I have to create a script that converts deciaml intgers to binary
What am I given?: vinary numbers contain only of 1 and 0, to convert number to binary, devide the number by 2.

Need to find:
- how to find the remiander
- how to find the 

My approach:
1.  I set the decimal number that I put in as decimal, then I use a while loop to devide the deciaml until it is 0 


What confused me:
...

What I learned:
- when adding to a sting it is simply to use the sting ``` binary = name + "test" ```
- to get the reaminder simply use the ``` rest = decimal % 2 ```
- to get the decimal use the ``` decimal = decimal // 2```
- to turn a number around ```binary[::-1]```

Useful Python:
```
def to_binary(decimal):
    binary = ""
    
    while decimal != 0:
        rest = decimal % 2
        decimal = decimal // 2
        binary = binary + str(rest)
        
    return str(binary[::-1])

```
