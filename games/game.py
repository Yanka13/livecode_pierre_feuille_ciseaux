import random

class Shifumi():
    def __init__(self, max_score=3):
        self.machine_score = 0
        self.user_score = 0
        self.score = 0
        self.max_score = max_score
        self.HANDS = ["pierre", "feuille", "ciseaux"]


    def compare_hands(self):
        if self.user_result == self.machine_result:
                    print("égalite!")
        elif self.user_result == "pierre" and self.machine_result == "feuille":
            print("machine gagne!")
            self.machine_score += 1

        elif self.user_result == "pierre" and self.machine_result == "ciseaux":
            print("utilisateur gagne!")
            self.user_score += 1
        elif self.user_result == "ciseaux" and self.machine_result == "feuille":
            print("utilisateur gagne!")
            self.user_score += 1
        elif self.user_result == "ciseaux" and self.machine_result == "pierre":
            print("machine gagne!")
            self.machine_score += 1
        elif self.user_result == "feuille" and self.machine_result == "pierre":
            print("utilisateur gagne!")
            self.user_score += 1
        else:
            print("machine gagne!")
            self.machine_score += 1

    def play(self):
        while self.score != self.max_score:

            self.user_result = input("Svp, veuillez choisir entre pierre, feuille, ciseaux")
            self.user_result = self.user_result.lower()

            if self.user_result in self.HANDS:
                # stocker le résultat de la machine, lui faire tirer au résultat
                self.machine_result = random.choices(self.HANDS)[0]
                print(f"Voici le résultat de la machine : {self.machine_result}")

                self.compare_hands()

                self.score = max(self.machine_score, self.user_score)
                print(f"Votre score est : {self.user_score}, celui de la machine est {self.machine_score}")

            else:
                print(f"Attention, veuillez saisir une valeur valide parmi cette liste : {self.HANDS}")
                continue


        if self.score == self.user_score and self.score > 0:
            print("Bravo, vous avez gagné")
        else:
            print("dommage, la prochaine fois!")



if __name__ == "__main__":
    game = Shifumi()
    game.play()
