import math

superHungry = 4
hungry = 2
classic = 1


def small_box_of_pizza():
    return 4


def big_box_of_pizza():
    return 10


def medium_box_of_pizza():
    return 6


def super_hungry(people):
    return people * superHungry


def hungry_people(people):
    return people * hungry


def classic_people(people):
    return people * classic


def total_number_of_slices(superHungryTotal, hungryTotal, classicTotal):
    superHungrySum = super_hungry(superHungryTotal)
    hungrySum = hungry_people(hungryTotal)
    classicSum = classic_people(classicTotal)
    return superHungrySum + hungrySum + classicSum


def total_number_of_big_boxes(superHungryTotal, hungryTotal, classicTotal):
    superHungrySum = super_hungry(superHungryTotal)
    hungrySum = hungry_people(hungryTotal)
    classicSum = classic_people(classicTotal)
    result = superHungrySum + hungrySum + classicSum
    return math.ceil(result / big_box_of_pizza())


def total_number_of_medium_boxes(superHungryTotal, hungryTotal, classicTotal):
    superHungrySum = super_hungry(superHungryTotal)
    hungrySum = hungry_people(hungryTotal)
    classicSum = classic_people(classicTotal)
    result = superHungrySum + hungrySum + classicSum
    return math.ceil(result / medium_box_of_pizza())


def total_number_of_small_boxes(superHungryTotal, hungryTotal, classicTotal):
    superHungrySum = super_hungry(superHungryTotal)
    hungrySum = hungry_people(hungryTotal)
    classicSum = classic_people(classicTotal)
    result = superHungrySum + hungrySum + classicSum
    return math.ceil(result / small_box_of_pizza())



