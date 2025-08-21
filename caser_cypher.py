#message = "Hello, World!" #The plain text
#shift = 7 #the key 
Last_char_code = 90
char_range =26
def caeser_shift(message,shift): #define a funtion to put message and shift the char  
    result = "" #printing result using string 
    for char in message.upper(): #because after 90 the Ascii values start with small a,b,c etc
        if char.isalpha(): #to check if the char is an aplha 
            char_code = ord(char) #Ascii code for each character 
            new_char_code = char_code + shift #shifting charter and putting it in new_char_code it prints Ascii value 
            if new_char_code >Last_char_code: #so the after 90 which is value of Z it goes to A i.e 65
                new_char_code -= char_range #subtract it to go to caps A 
            new_char = chr(new_char_code) #charcter value of the shifted code 
            #print(char,char_code , new_char_code, new_char) #prints everything instead of just the letters + ascii code (just for understanding)
            result +=new_char
        else:
            result += char
    print(result)
caeser_shift("Hello,World" ,7)
caeser_shift("Abhay is Black" ,4)
caeser_shift("Kashif is Nepali" ,6)
caeser_shift("Ali is Afgani" ,3)
#Hope Everyone Understood Caeser_Cypher Using Python its just small code lol ill be putting in Github; 