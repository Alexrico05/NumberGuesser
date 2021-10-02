#NumberGuess
import random
            
def juego():
    #Variables initialisation
    solution = 0
    y = 0

    print "Hi welcome to the Number Guess!.I ll think a number and you wil have to try to guess it.First you ll have to give me the interval in which the number will be.Select the lower number"
    lower_number = input()
    print 'Now select the maximum number'
    max_number = input()
    print 'If you dont know the number enter: solution'

    generated_number = random.randint(lower_number, max_number)

    def attemps():
        print 'Whats your choice?'
        sele_num = input()
    
        if sele_num == generated_number:
            print 'Congratulations you guessed the number!!'
            print 'press y if you want ot play again'
            restart = input()
            if restart == y:
                if __name__ == '__main__':
                    juego()



        elif sele_num == solution:
            print 'The number was',generated_number

        else:
            print 'Ohh that was not the number!'
            if __name__ == '__main__':
                attemps()

    if __name__ == '__main__':
            attemps()

        
if __name__ == '__main__':
            juego()
