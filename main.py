#import
# Python program to illustrate reassignment of functions and how they can be treated as objects

def really_long_annoying_name_PleaseBeQuiet(t):
    return t.lower()

in_voice = input("Please say something. Quiet! This is library: ")

print(in_voice)

# Assign function really_long_annoying_name_PleaseBeQuiet to a var whisper
whisper = really_long_annoying_name_PleaseBeQuiet

if in_voice != whisper(in_voice):
    print(f"*whispers* THAT'S NOT A WHISPER!, what you meant to say was: '{whisper(in_voice)}'")
else:
    print("Thank you for whispering.")
