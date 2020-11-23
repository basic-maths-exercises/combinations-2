# General combinations

You hopefully didn't find the previous exercise too difficult as we are now going to extend on this.  You now need to complete the function called `gencombinations`.  This function takes two arguments:

`N` -  an integer that tells you the length of each of the lists that will be output.
`R` - the first element in the list tells you how many zeros are in the output lists, the second element tells you how many ones, the third element the number of twos and so on.

To complete this task you need to generate all the possible lists that you can form with `len(R)`  symbols by converting the non-negative integers that are less than `len(R)**N` to base `len(R)`.  This is a simple modification of the algorithm that we have used for the previous exercise.  Within the loop that generates all these lists you then need to have some logic that selects only the relevant lists i.e. those that have the right numbers of each of the symbols.
