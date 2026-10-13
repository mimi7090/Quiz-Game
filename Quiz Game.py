while True :
    print("\n=====Quiz Game=====")
    score = 0 
    # Question 1
    print("Question 1.What is the planet that is knowm as red planet ?")
    print("a.Jupiter")
    print("b.Earth")
    print("c.Mars")
    print("d.Venus")
    options = input("a/b/c/d =").lower()
    if options == "a" :
        print("Wrong")
    elif options == "b" :
        print("Wrong")
    elif options == "c" :
        print("Correct")
        score+=1
    elif options == "d" :
        print("Wrong")
    else :
        print("Invalid choice")
    print("score=",score)
    # Question 2
    print("Question 2.Which is one of the biggest mammal on the earth.")
    print("a.Elephants")
    print("b.Lions")
    print("c.Sharks")
    print("d.Whale")
    options = input("a/b/c/d =").lower()
    if options == "a" :
        print("Wrong")
    elif options == "b" :
        print("Wrong")
    elif options == "c" :
        print("Wrong")
    elif options == "d" :
        print("Correct")
        score+=1
    else :
        print("Invalid choice")
    print("score=",score)
    # Question 3
    print("Question 3.Who was the First scientists who try to invant Time machine?")
    print("a.Tesla")
    print("b.Newton")
    print("c.Mendela")
    print("d.Da vin chi")
    options = input("a/b/c/d =").lower()
    if options == "a" :
        print("Correct")
        score+=1
    elif options == "b" :
        print("Wrong")
    elif options == "c" :
        print("Wrong")
    elif options == "d" :
        print("Wrong")
    else :
        print("Invalid choice")
    print("score =",score)
    # Question 4
    print("Question 4.What is the frquency of universe in Herz ?")
    print("a.375")
    print("b.369")
    print("c.372")
    print("d.345")
    options = input("a/b/c/d =").lower()
    if options == "a" :
        print("Wrong")
    elif options == "b" :
        print("Correct")
        score+=1
    elif options == "c" :
        print("Wrong")
    elif options == "d" :
        print("Wrong")
    else :
        print("Invalid choice")
    print("score =",score)
    # Question 5
    print("Question 5.Atomic bomb was first invented by which country.")
    print("a.Japan")
    print("b.Germany")
    print("c.America")
    print("d.Russia")
    options = input("a/b/c/d =").lower()
    if options == "a" :
        print("Wrong")
    elif options == "b" :
        print("Wrong")
    elif options == "c" :
        print("Correct")
        score+=1
    elif options == "d" :
        print("Wrong")
    else :
        print("Invald choice")
    print("score =",score)
    print("Score =",score,"/5")
    ask = input("Do you want to play again?(Yes/NO) :").upper()
    if ask == "NO" :
        print("Thanks for playing")
        break