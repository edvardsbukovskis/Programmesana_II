class Augs:
    def __init__(self, augstums, tips):
        if augstums > 150 or augstums < 5:
            print("Nederīgs augstums")
            self.augstums = ""
        else:
            self.augstums = augstums
        if isinstance(tips, str):
            if " " in tips:
                print("Nederīgs tips")
            else: 
                self.tips = tips
        else:
            print("Nederīgs tips")

    def aprekinat_auga_tilpums(self):
        return self.augstums * 1 * 1
    
    def __del__(self):
       print("Augs tika izdzēsts")


class AuguBloks(Augs):
    def __init__(self, augstums, tips, skaits, forma):
        super().__init__(augstums, tips)
        self.skaits = None
        self.derigums = 0
        if isinstance(skaits, int):
            if skaits < 1 or skaits > 4:
                print("Nederīgs skaits")
            else:
                self.skaits = skaits
        else:
            print("Nederīgs skaits")
        self.forma = None
        if forma not in [11, 12, 13, 14, 22]:
            print("Nederīgs forma")
            self.derigums = 1
        else:
            self.forma = forma
        self.nosaukums = tips+str(self.skaits)

    def tilpums(self):
        return self.aprekinat_auga_tilpums()*self.skaits


ab1 = AuguBloks(50, "Tomāts", 3, 13)
print(ab1.nosaukums, ab1.tilpums())

ab2 = AuguBloks(40, "Pipars", 5, 23)
print(ab2.derigums, ab2.nosaukums)
ab2.forma = 12

print(ab2.nosaukums, ab2.derigums)

