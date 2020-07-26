import random
import array

#Maximum length for password
max_len = 12

# Declare characters array for password
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
char_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
  
char_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<'] 

mixed_out1 = char_lower + char_upper + num + symbols

# Select characters randomly from set
rand_num = random.choice(num)
rand_lower = random.choice(char_lower)
rand_upper = random.choice(char_upper)
rand_symobls = random.choice(symbols)

mixed_out2 = rand_num + rand_lower + rand_upper + rand_symobls

# Fill the password length
for x in range(max_len - 4):
    mixed_out2 = mixed_out2 + random.choice(mixed_out1)

    # Convert pass into array
    pass_list = array.array( 'u', mixed_out2)

# Create final password from the temporary list
password = ""
for x in pass_list:
    password += x

print(password)






