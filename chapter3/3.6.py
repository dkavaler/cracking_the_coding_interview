# Pretends list is a linked list and uses it accordingly
from enum import Enum

class AnimalType(Enum):
	DOG = 1
	CAT = 2


class Animal:

	def __init__(self, typ, name):
		self.type = typ
		self.name = name


class AnimalShelter:

	def __init__(self):
		self.animals = []
		self.dogs = []
		self.cats = []

	def enqueue(self, animal):
		self.animals.append(animal)
		if animal.type == AnimalType.DOG:
			self.dogs.append(animal)
		elif animal.type == AnimalType.CAT:
			self.cats.append(animal)


	def dequeue_any(self):
		if len(self.animals) == 0:
			return None

		animal = self.animals.pop(0)
		if animal.type == AnimalType.DOG:
			self.dogs.pop(0)
		elif animal.type == AnimalType.CAT:
			self.cats.pop(0)

		return animal

	def dequeue_cat(self):
		if len(self.cats) == 0:
			return None

		animal = self.cats.pop(0)
		for i, a in enumerate(self.animals):
			if a.type == AnimalType.CAT:
				self.animals.pop(i)
				return animal


	def dequeue_dog(self):
		if len(self.dogs) == 0:
			return None

		animal = self.dogs.pop(0)
		for i, a in enumerate(self.animals):
			if a.type == AnimalType.DOG:
				self.animals.pop(i)
				return animal


if __name__ == '__main__':
	animal_shelter = AnimalShelter()
	animal_shelter.enqueue(Animal(AnimalType.CAT, 'cat1'))
	animal_shelter.enqueue(Animal(AnimalType.CAT, 'cat2'))
	animal_shelter.enqueue(Animal(AnimalType.CAT, 'cat3'))
	animal_shelter.enqueue(Animal(AnimalType.DOG, 'dog1'))
	animal_shelter.enqueue(Animal(AnimalType.CAT, 'cat4'))
	animal_shelter.enqueue(Animal(AnimalType.DOG, 'dog2'))
	animal_shelter.enqueue(Animal(AnimalType.DOG, 'dog3'))
	animal_shelter.enqueue(Animal(AnimalType.CAT, 'cat5'))

	assert animal_shelter.dequeue_any().name == 'cat1'
	assert animal_shelter.dequeue_dog().name == 'dog1'
	assert animal_shelter.dequeue_any().name == 'cat2'
	assert animal_shelter.dequeue_cat().name == 'cat3'
	assert animal_shelter.dequeue_dog().name == 'dog2'
	assert animal_shelter.dequeue_dog().name == 'dog3'
	assert animal_shelter.dequeue_dog() == None
	assert animal_shelter.dequeue_cat().name == 'cat4'
	assert animal_shelter.dequeue_any().name == 'cat5'
	assert animal_shelter.dequeue_any() == None

