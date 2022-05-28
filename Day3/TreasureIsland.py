print("Welcome to the Treasure island.\nYour mission is to Find the treasure.")

c1=input("You are on a cross road where do you want to go ? left or right?\n").lower()

if(c1=='left'):
    c2=input('You Came to the lake, there is an island in the'
             ' middle of the lake. Type "wait" to wait for the boat.Type "swin to swim accross ').lower()
    if c2=="wait":
        c3=input("You Arrived at the island unharmed. There is a house with 3 doors .One Red,one yellow and one blue"
                 ".Choose which color do you choose").lower()
        if c3=="red":
            print("its a room full of fire . Game over")
        elif c3=="yellow":
            print("You found Treasure , YOU WON!!!")
        elif c3=="blue":
            print("its a room full of crockodiles . Game over!")
    else:print("you got attacked by an angry trout.Game over!")


else:
    print("You fell into a hole , Game over!")

