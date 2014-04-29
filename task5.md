# Task 5 Question

1. The additional module that i will need to import into the program is the datetime
2. 
3. date.strftime(%day/%month/%Year)

## Additional Task - Variable roles

1. Fixed Variable - a variable that programs without any calculation and the variable wont be changed
   Stepper - A variable which keeps count of the number being repeated in the program
   Most Recent Holder - a Variable used to record the last thing that is being inputed by the user or the latest value from an array
   Most Wanted Holder - A variable that keeps track of the lowest or highest values in the inputs
   Gatherer - A variable that accumalates or tallies up set of data and inputs, its used for calculating totals
   Transformation - used to store the result of a calculation involving more than one variable
   Follower - used to keep check of a previous value of a variable so the new value is compared
   Temporary - used for storing something for a very short period of time

2. Fixed Variable -  noOfSwaps (98)
   Stepper - for count in range, NoOfSwapsMadeSoFar
   Most Recent Holder - Choice (197), LineFromFile (87), LastCard(187)
   Most Wanted Holder - NextCard (188)
   Gatherer - 
   Transformations - Higher (124), FoundSpace (171)
   Follower - LastCard (187)
   Temporary - SwapSpace (97)
   
## Additional Task - Functions and Parameters

1. pass by value creates a copy of the original variable and when changes are made it will have no effect on the original variable and it is lost when the program execution returns to the code,
and pass by reference is when the variable inside the routine uses a reference to the same memory location as the variable passed and any changes to the contents of the variable are accessible to the program code

2. pass by value - Rank(53), Suit (65), Score(139)
   pass by reference - Deck (83), ThisCard(109)