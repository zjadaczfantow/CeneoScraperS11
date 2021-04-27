import os
import pprint
import pandas as pd

pd.set_option('display.max_columns', None)

print(*[x.split('.')[0] for x in os.listdir("opinions")], sep="\n") #<- list comprehension

product_id = input("Enter product ID: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

#opinions['stars']
#opinions.stars

opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avarage_score = opinions.stars.mean()


#print(opinions_count)
#print(pros_count)
#print(cons_count)
#print(avarage_score)


print(f"""There are {opinions_count} opinions in data set.
For {pros_count} opinions in list of advantages is avalible.
For {cons_count} opionis list of disadvanages is avalible.
Avarage score is {avarage_score:.1f}""")


recommendations = opinions.recommendation.value_counts(dropna=False)
print(recommendations)
print(type(recommendations))
#print(type(opinions))
#print(type(opinions.stars))