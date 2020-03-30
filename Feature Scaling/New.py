def main():

    gandalf = [10, 11, 13, 43, 22, 11, 10, 33, 22, 22]
    saruman = [10, 66, 12, 43, 12, 10, 44, 23, 12, 22]

    victory_record_gandalf = [] #assign 0 Assign 0 to each variable that stores the victories
    victory_record_saruman = []

    def gandalf_win (score):
        print("Raund:", score, ":", "Gandalf wins.")
        victory_record_gandalf.append(0)

    def saruman_win (score):
        print("Raund:", score, ":", "Saruman wins")
        victory_record_saruman.append(0)

    def total_win(victory_record_gandalf,  victory_record_saruman):
        print(" ")
        if len(victory_record_saruman) > len(victory_record_gandalf):
            print("Match Result: Saruman won the match.")
        elif len(victory_record_gandalf) > len(victory_record_saruman):
            print("Match Result: Gandalf won the match.")
        else:
            print("Match Result: Tie.")


    for score in range(len(gandalf)):
        if gandalf[score] > saruman[score]:
            gandalf_win(score)
        elif gandalf[score] < saruman[score]:
            saruman_win(score)
        else:
            print("Raund:",score,":","Tie.")

    total_win(victory_record_gandalf,victory_record_saruman)





if __name__ == '__main__':
    main()


