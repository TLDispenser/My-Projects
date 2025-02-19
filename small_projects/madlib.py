print("Welcome to the Madlib Game!")
print("Please fill in the blanks with the requested words.")
print("Once you have filled in all the blanks, the Madlib will be generated.\n")
def proper_noun(word):
    return word.capitalize()
def all_other(word):
    return word.lower()

import time

nouns = []
verbs = []
other = []
name = input('Input a Name: ')
other.append(name)
verb1 = input('Input a Verb: ')
verbs.append(verb1)
verb2 = input('Input a Verb (ing): ')
verbs.append(verb2)
pronoun1 = input('Input a Pronoun: ')
other.append(pronoun1)
noun1 = input('Input a Noun: ')
nouns.append(noun1)
noun_plural1 = input('Input a Noun (Plural): ')
nouns.append(noun_plural1)
place1 = input('Input a Place: ')
other.append(place1)
noun2 = input('Input a Noun: ')
nouns.append(noun2)
verb3 = input('Input a Verb: ')
verbs.append(verb3)
adjective1 = input('Input an Adjective: ')
other.append(adjective1)
noun3 = input('Input a Noun: ')
nouns.append(noun3)
noun4 = input('Input a Noun: ')
nouns.append(noun4)
determiner1 = input('Input a Determiner: ')
other.append(determiner1)
verb_past1 = input('Input a Verb (Past tense): ')
verbs.append(verb_past1)
adjective2 = input('Input an Adjective: ')
other.append(adjective2)
noun_plural2 = input('Input a Noun (Plural): ')
nouns.append(noun_plural2)
adjective3 = input('Input an Adjective: ')
other.append(adjective3)
noun_plural3 = input('Input a Noun (Plural): ')
nouns.append(noun_plural3)
adjective4 = input('Input an Adjective: ')
other.append(adjective4)
verb_ing1 = input('Input a Verb (ing): ')
verbs.append(verb_ing1)
verb4 = input('Input a Verb: ')
verbs.append(verb4)
noun5 = input('Input a Noun: ')
nouns.append(noun5)
adjective5 = input('Input an Adjective: ')
other.append(adjective5)
noun6 = input('Input a Noun: ')
nouns.append(noun6)
noun7 = input('Input a Noun: ')
nouns.append(noun7)
fun_activity1 = input('Input a fun activity: ')
other.append(fun_activity1)
something_to_wear1 = input('Input a Something to wear: ')
other.append(something_to_wear1)
pronoun2 = input('Input a Pronoun: ')
other.append(pronoun2)
verb_past2 = input('Input a Verb (Past tense): ')
verbs.append(verb_past2)
noun_plural4 = input('Input a Noun (Plural): ')
nouns.append(noun_plural4)
adverb1 = input('Input an Adverb: ')
other.append(adverb1)
verb5 = input('Input a Verb: ')
verbs.append(verb5)
verb_ing2 = input('Input a Verb (ing): ')
verbs.append(verb_ing2)

for i in range(len(nouns)):
    nouns[i] = all_other(nouns[i])
for i in range(len(verbs)):
    verbs[i] = all_other(verbs[i])
for i in range(len(other)):
    other[i] = all_other(other[i])
    

sentences = [
    f"Hello {proper_noun(other[0])}! Before you {verbs[0]} for Halloween {verbs[1]}, make a list of {other[1]} you will need.",
    f"A list will keep you from having to make several trips to the {nouns[0]} while you are trying to get {nouns[1]} ready for trick or treating or trying to get your {other[2]} ready for the Halloween party.",
    f"The price of {nouns[2]} increases as the holiday {verbs[2]}.",
    f"Write the name of the store with the best prices for each item on {other[3]} list.",
    f"This will not only make your shopping easier, but it will also save you {nouns[3]}.",
    f"Remember to check your Sunday {nouns[4]} for coupons you can use for a discount on Halloween {other[4]}.",
    f"You can buy new decorations {verbs[3]} year and keep them {other[5]} in {nouns[5]} bins.",
    f"Color-code the bins for different holidays to stay {other[6]}.",
    f"Get all of your fall and Halloween {nouns[6]} together and sort through them and throw away the ones that are {other[7]} or just look worn.",
    f"Before you begin {verbs[4]}, make sure you {verbs[5]} your home and remove all {nouns[7]}.",
    f"This will make it much {other[8]} to decorate for Halloween, Thanksgiving, and Christmas.",
    f"Look for fun {nouns[8]} and {nouns[9]} such as haunted houses, hayrides, and {other[9]}.",
    f"Mark the dates and locations on the family calendar to avoid scheduling conflicts.",
    f"Getting the right {other[10]} for your children and yourself can be the most time-consuming and expensive part of Halloween.",
    f"If you are making costumes from scratch, you need to allow {other[11]} plenty of time to get them {verbs[6]}.",
    f"You don't want to be rushing around trying to put last-minute details on the {nouns[10]}.",
    f"If you are buying costumes, you should get them {other[12]} as possible.",
    f"It may be more cost-effective to {verbs[7]} costumes instead of {verbs[8]} them."
]

for sentence in sentences:
    print(sentence)
    time.sleep(1.5)
