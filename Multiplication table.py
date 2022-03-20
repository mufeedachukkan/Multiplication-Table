import pyttsx3
#engine = pyttsx3.init()
#engine.say("hi hoe are you")
#engine.runAndWait()
n = input("Enter a number :")
#9
#one nines are nine
dic = {
    "1" : "ones",
    "2" : "twos",
    "3" : "threes",
    "4" : "fours",
    "5" : "fives",
    "6" : "sixes",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10" : "tens"
}
txt = ""
#1 nines are 9
    #2 nines are 18
for i in range(1,11):
    mul =  i*int(n)
    txt+= str(i) + " " + dic[n] + " are " + str(mul)+"\n"
#print(txt)
engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()
    

