def encodecode(ins,shift,ende):
    answer=""
    if ende =='decode':
            shift*=-1
    for i in ins:
        if i in alpha:
            position=alpha.index(i)
            newposition=position+shift
            newl=alpha[newposition]
            answer+=newl
        else:
            answer+=i
    print(f"The {ende.upper()}D word is:{answer}")

# def decode(ins,shift):
#     decoded=""
#     for i in ins:
#         position=alpha.index(i)
#         newposition=position-shift
#         newl=alpha[newposition]
#         decoded+=newl
#     print("Decryted:",decoded)

print("Caesar Cipher.\nBe Screte!!!")
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a='yes'

while a=='yes' or a=='y':
    ende=input("What do you want to do Encoding type'Encode' or Decoding type 'Decode'?\n").lower()
    # if ende=='e':
    ins=input("Enter word:").lower()
    shift=int(input("enter shift:"))
    shift= shift%len(alpha)
    encodecode(ins,shift,ende)
    # elif ende=='d':
        
        # ins=input("What do you want to decode:").lower()
        # shift=int(input("enter shift:"))
        # decode(ins,shift)
    # else:
    #     print("Invalid!!!")
    a=input("\n\nDo you like to again encode or decode type 'yes' or 'no':").lower()
    print("============================================================================================")
