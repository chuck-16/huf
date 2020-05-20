# huf
huf is a Esoteric programming language similar to brainfuck. Try it if you dare!

Check out docs.txt for Documentation
  
# Idea of huf
    The 'temp' is a number that correlates to the http://www.asciitable.com/
    Each temp is one letter, or any other ASCII symbol
    Use multiple temps in a row to print something!
    You can stretch each temp into its own row

# Marks or Temp markers:
    +   --adds 1 to the temp
    |   --starts a multiplying temp
    !   --ends multiplication temp
    >   --records temp in output and creates new temp

# Examples
    Code:  ++++++++++|++++++++++!>
    Output:  d
    Explanation:  10*10 = 100,  ASCII "d" = 100

    Code:  ++++++++|++++++++++!+++++++++>+++++++|++++++++++!+++++++++>
    Output:  YO
    Explanation:  8*10+9=89, 7*10+9=79,  ASCII "Y" = 89,  ASCII "O" = 79

