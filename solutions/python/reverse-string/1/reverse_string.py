text =["","robot","Ramen","I'm hungry!","racecar","drawer","子猫"]

def reverse(text):
    return text[::-1]
    
    reversed_text = [word[::-1] for word in text]
    print(reversed_text)
