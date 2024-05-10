# Turing Machine Generator

Generate Cool Gifs of Turing Machines using this project

Here is a turing machine render generated using this code:  

![](https://github.com/kolbeMosh/TuringMachineGenerator/blob/master/mod3TM.gif)

This program can also generate static images in your desired format  
(as long as the format is supported by Pillow)   


Here is an example of that:  

![](https://github.com/kolbeMosh/TuringMachineGenerator/blob/master/mod3TM.svg)

## Setup

##### Necessary Python Packages

[Graphviz](https://graphviz.readthedocs.io/en/stable/manual.html#installation): 

```
  pip install graphviz
```
[Pillow](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)
```
  pip install Pillow
```

##### How to Format your TM:
mod3 TM 
```
a
B
d
a0a0R
a1b1R
b0c0R
c1c1R
c0b0R
b1a1R
aBdBR
```
lines 1-3 are as follows:  
  1. start state
  2. blank character
  3. accepting state(s)  
  
lines 4-end are: 
  1. current state
  2. read character
  3. next state
  4. write character
  5. direction ("L" | "R")

##### Running the program

Use the following syntax to run the program
```
  python main.py [PATH/TO/TM] [Input you want to test]
```

here is an example using the input displayed in the gif
```
python3 main.py TMs/Tmod3.txt 01010111
```

