class Pet:
    all=[]
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    def __init__(self,name, pet_type=None, owner=None):
        self.name= name
        self.pet_type= pet_type
        Pet.all.append(self)
        self._owner=owner
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, value):
        if not isinstance(value,Owner):
            raise Exception("Owner must be an instance of Owner class")
        self._owner= value
        
    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_entry):
        if pet_entry in Pet.PET_TYPES:
            self._pet_type= pet_entry
        else:
            raise Exception('Input a valid pet-type')
    
class Owner:
    def __init__(self,name):
        self.name= name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be instance of pet class")
        pet.owner= self
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)