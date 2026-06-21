import art
print(art.caesarlogo)


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(orginal_text, shift_amount, encode_or_decode):
    output_text = "" 
    
    if encode_or_decode == "decode":
            shift_amount *= -1
            
    for letter in orginal_text:
        
        if letter not in alphabet:
            output_text += letter
            
        else:    
            shifted_postion = alphabet.index(letter) + shift_amount
            shifted_postion %= len(alphabet)
            output_text += alphabet[shifted_postion]
        
    print(f"here is the {encode_or_decode}d result:{output_text}") 
    
    
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))
        
    caesar(orgial_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want continue. Otherwise type 'no'.").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
     