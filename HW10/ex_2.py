from my_library.pet import Pet
from my_library.human import Human
from my_library.human_with_pet import HumanWithPet


my_pet1 = Pet("Mauricio", "Cat", "mamaliga")
my_pet2 = Pet("Kesha", "Parrot", "euros")
my_pet3 = Pet("Spike", "Dog", "steaks")
my_human = Human("Marius", "Tricolici", "29/12/2001")

human_with_pets = HumanWithPet(my_human)
print(human_with_pets)

human_with_pets.adopt_new_pet(my_pet1)
print(human_with_pets)
human_with_pets.adopt_new_pet(my_pet2)
print(human_with_pets)
human_with_pets.adopt_new_pet(my_pet3)
print(human_with_pets)
