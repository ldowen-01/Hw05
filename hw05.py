"""
Name: Langley Owen
Peers: Prof. Hia Ghosh
References: (anything you checked to solve this)
"""

def get_letter():
    """ this function gets a letter input from user and prints
     the corresponding Error, otherwise letter is stored  """

    #while loop
    while True:
        
        #ask for user input for a letter
        user_letter = input("Give an single uppercase letter: ")
        
        #if the length isn't a single letter try again
        if len(user_letter) != 1:
            print("Error: it needs to be a single character.")
            continue #continue?
        
        #if the letter isn't uppercase A, B, or C, try again
        
        letters = ["A", "B", "C"]
        if user_letter not in letters:
            print("Error: You provided the wrong character.")
            
            
        #if the letter is uppercase A, B, or C, return the letter
        else:
            return user_letter    
    

def get_digit():
    """ This function gets a letter input from user
and prints corresponding Error, otherwise digit is stored"""

    #while loop
    while True:
    
        #ask for user input for a number
        user_digit = input("Give an single number character: ")
        
        #if user_digit is digit, go to next check
        if user_digit.isdigit() == True:
            
            #if digit check if it's in the range 1-3
            if int(user_digit) not in [1,2,3]:
                print ("Error: a single digit needs to be in [1,3].")
                continue
            
            #if digit is in range 1 - 3, return digit
            else: #elif user_digit == [1,3]:
                #because while loop we cant use return?
                return user_digit
           
        #if user_digit is not a digit, print error
        else:
            print("Error: your input should be only digits.")
            continue
        
def check_pattern(letter, digit, lst):
    #this function accepts three input parameters
    """ This function has three parameters: letter, digit, and list """
    
    #print message before checking the list
    print("Strings with the pattern:")
    
    #for each item in the list check  
    for item in lst:
        
        #check if letter is in the item
        if letter in item:
            
            #check if number is in item, only after number
            if digit in item:
                
                #print the item the letter and number show up in
                print(item, end=" ")
    
    #this cold only works with C3 bcause the only items in the list with C and 3 also follow the letter first rule
    #need to figure out a way to check for order of number and letters as well as for the @ symbol
    
    #check order, only print when it goes letter THEN number
    #Ideas:
        #could use multiple for loops
        #could add more parameters in line 73
        
    #have to sort if letter goes before number AND only print once
    #print words only once if they have the pattern more than once 
        

#  The function main is INCOMPLETE, you must finish it
# before you submit


def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    letter = get_letter()
    
    digit= get_digit()
    
    check_pattern(letter, digit, st_list)

    results = input("\nTry Again? (y/n): ")
    
    while True:
        if results == "y":
            main()
            
        else:
            break           
            
  
    # -------------------------------------------------
    # No need to modify anything Below this line
    
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()