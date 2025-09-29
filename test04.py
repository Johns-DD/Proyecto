from faker import Faker
fake = Faker()
print (fake.random_choices(elements=('a', 'b', 'c', 'd')) )