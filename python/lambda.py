from pprint import pprint
from utils import start_section

people = [
    {"name": "Pedro", "age": 20},
    {"name": "María", "age": 30},
    {"name": "Luis", "age": 50}
]


def by_name(person):
    return person["name"]


def by_age(person):
    return person["age"]


def pretty_print():
    pprint(people, indent=2, width=1)


people.sort(key=by_name)
pretty_print()

people.sort(key=by_age)
pretty_print()

start_section("Using lambdas")
people.sort(key=lambda person: person["name"])
pretty_print()

people.sort(key=lambda person: person["age"])
pretty_print()
