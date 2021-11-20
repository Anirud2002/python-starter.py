def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return int(weight / 0.45)


class Mammal:
    def talk(self):
        print('Talk')
