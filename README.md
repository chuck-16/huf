# huf
huf is a Esoteric programming language similar to brainfuck. Try it if you dare!

Check out docs.txt for Documentation
  
# Idea of huf
    The 'temp' is a number that the whole line or statement adds up to
    Each temp is adds up to be one number
    Use multiple temps in a row to use functionlity
    You can stretch each temp into its own row

# How to run .huf programs
    --offline:
      --go to chosen text editor and create new file
      --make the extension on this file .huf
      --put your .huf in the same folder as the interpreter (huf.py)
      --open command line in that directory and run "python huf.py"
      --Then type your file name in when prompted
      
      --online:
      --just use run or edit HelloWorld.huf on repl.it:
[![Run on Repl.it](https://repl.it/badge/github/Charmaster16/huf)](https://repl.it/github/Charmaster16/huf)

      

# Marks or Temp markers:
    +   --adds 1 to the temp
    |   --starts a multiplying temp
    !   --ends multiplication temp
    >   --records temp in output and creates new temp
    #   --opens print statement
    @   --closes print statement

# Examples
    Code:  #++++++++++|++++++++++!>@
    Output:  d
    Explanation:  10*10 = 100,  ASCII "d" = 100

    Code:  #++++++++|++++++++++!+++++++++>+++++++|++++++++++!+++++++++>@
    Output:  YO
    Explanation:  8*10+9=89, 7*10+9=79,  ASCII "Y" = 89,  ASCII "O" = 79
    
 # Hello World
    #++++++++++|+++++++!++>
    ++++++++++|++++++++++!+>
    ++++++++++|++++++++++!++++++++>
    ++++++++++|++++++++++!++++++++>
    ++++++++++|+++++++++++!+>
    ++++++|+++++!++>
    ++++++++++|++++++++!+++++++>
    ++++++++++|+++++++++++!+>
    ++++++++++|+++++++++++!++++>
    ++++++++++|++++++++++!++++++++>
    ++++++++++|++++++++++!>@
    
    Output:  Hello World

