alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = []

def Encr(char):
    if char in alpha:
        position = alpha.index(char)
        calc_position = (position + 6) % 26
        return str(calc_position)
    else:
        return ''
    
def Decr(key):
    try:
        position = int(key)
        calc_position = (position - 6) % 26
        return alpha[calc_position]
    except:
        return ''

def display_encr(userInput):
    spaced_input = ' '.join(userInput)
    #print(f'Your text is: {spaced_input}')

    words = spaced_input.split()
    
    for char in words:
        enc_characters = Encr(char)
        code.append(enc_characters)
    
    clean_results = ' '.join(code)
    print(f'You entered: -> ** {userInput} **') 
    print(f'Your key is ready -> ** {clean_results} **')
    code.clear()
    
def display_decr(userInput):
    keys = userInput.split()
    decrypted = []
    for key in keys:
        decrypted_characters = Decr(key)
        decrypted.append(decrypted_characters)
    
    clean_results = ''.join(decrypted)
    print(f'Your decrypted text is ready : {clean_results}')
    decrypted.clear()
    

for _ in range(1):
    condition = input('Encryption or Decryption (e/d): ').lower()
    
    if condition == 'e':
        userInput = input('Enter your text: ').lower()
        display_encr(userInput)
    elif condition == 'd':
        userInput = input('Enter your key: ').lower()
        display_decr(userInput)
    else:
        print('Enter valid character ("e" for encryption / "d" for decryption)')
        
