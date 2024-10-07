def is_match(message, pattern):
   
    if len(pattern) == 0:
        return len(message) == 0

   
    if pattern[0] == '*':
       
        return is_match(message, pattern[1:]) or (len(message) > 0 and is_match(message[1:], pattern))

   
    if pattern[0] == '?' or pattern[0] == message[0]:
        return is_match(message[1:], pattern[1:])

   
    return False


print(is_match("aa", "a"))
print(is_match("aa", "*"))     
print(is_match("cb", "?a"))      
print(is_match("abcd", "a*d"))  
print(is_match("abcd", "?b*d")) 
print(is_match("abcd", "?b?*"))  
